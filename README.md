
# AI DOCTOR Medical Chatbot - Analyze Image with Vision Models
 
This Medical Chatbot is a web app that allows users to upload medical images and ask questions about them. Using GROQ's LLaMA 3.2 Vision Models, it provides intelligent image analysis and context based responses. Built with FastAPI and Tailwind CSS, it’s designed for educational and diagnostic support.
This chatbot is a lightweight web application that allows users to upload medical-related images and ask questions about them. It uses GROQ's LLaMA 3.2 Vision Models to generate image based responses, making it helpful for educational or diagnostic support scenarios.

---

### Features

- Upload an image and ask contextual questions
- Runs queries through two powerful vision models:
  - llama-3.2-11b-vision-preview
  - llama-3.2-90b-vision-preview
- Side-by-side responses for comparison
- Clean, responsive UI built with Tailwind CSS
- Error handling and image validation
- FastAPI backend

---

### Technologies used

 Backend      - FastAPI, Python, GROQ API      
 Frontend     - HTML, Tailwind CSS, Vanilla JS 
 Image Proc.  - Pillow, base64, io             
 Templating   - Jinja2                         
 Logging      - Python logging module        
 Env Handling - python dotenv                

---

Make sure fastapi, uvicorn, python dotenv, pillow, and requests are included.

### How Chat bot Works

1. Upload an image ( X-ray, chart...)
2. Type a medical or visual question
3. The app sends the image and question to both vision models via GROQ API
4. Responses are displayed on screen in Markdown format


