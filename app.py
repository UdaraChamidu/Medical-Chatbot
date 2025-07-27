from fastapi import FastAPI, File, UploadFile, Form, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
import base64
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the .env file")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload_and_query")
async def upload_and_query(image: UploadFile = File(...), query: str = Form(...)):
    try:
        image_content = await image.read()
        if not image_content:
            return JSONResponse(status_code=400, content={"response": "Empty image file."})

        # Verify image
        try:
            img = Image.open(io.BytesIO(image_content))
            img.verify()
        except Exception as e:
            logger.error(f"Invalid image format: {str(e)}")
            return JSONResponse(status_code=400, content={"response": f"Invalid image format: {str(e)}"})

        # Encode image
        encoded_image = base64.b64encode(image_content).decode("utf-8")

        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                ]
            }
        ]

        # Inner function to call GROQ API
        def make_api_request(model):
            try:
                response = requests.post(
                    GROQ_API_URL,
                    json={
                        "model": model,
                        "messages": messages,
                        "max_tokens": 1000
                    },
                    headers={
                        "Authorization": f"Bearer {GROQ_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    timeout=30
                )
                return response
            except requests.RequestException as req_err:
                logger.error(f"Request failed: {str(req_err)}")
                return None

        selected_model = "meta-llama/llama-4-scout-17b-16e-instruct"
        response = make_api_request(selected_model)

        if response is None:
            return JSONResponse(status_code=500, content={"response": "Failed to contact the LLM service."})

        if response.status_code == 200:
            result = response.json()
            answer = result.get("choices", [{}])[0].get("message", {}).get("content", "No content returned.")
            logger.info(f"Processed response: {answer[:100]}...")
            return JSONResponse(status_code=200, content={"response": answer})
        else:
            logger.error(f"GROQ API error: {response.status_code} - {response.text}")
            return JSONResponse(
                status_code=response.status_code,
                content={"response": f"GROQ API Error: {response.status_code} - {response.text}"}
            )

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return JSONResponse(status_code=500, content={"response": f"Internal Server Error: {str(e)}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)

