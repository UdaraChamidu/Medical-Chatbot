# Medical-Chatbot
This Medical Chatbot is a web app that allows users to upload medical images and ask questions about them. Using GROQ's LLaMA 3.2 Vision Models, it provides intelligent image analysis and context based responses. Built with FastAPI and Tailwind CSS, it’s designed for educational and diagnostic support.

# 🧠 AI-DOCTOR (Medical Chatbot) – Analyze Image with Vision Models

**AI-DOCTOR** is a lightweight web application that allows users to upload medical-related images and ask questions about them. It uses **GROQ's LLaMA 3.2 Vision Models** to generate image-based responses, making it helpful for educational or diagnostic-support scenarios.

---

### 📸 Features

- Upload an image and ask contextual questions
- Runs queries through two powerful vision models:
  - `llama-3.2-11b-vision-preview`
  - `llama-3.2-90b-vision-preview`
- Side-by-side responses for comparison
- Clean, responsive UI built with Tailwind CSS
- Error handling and image validation
- FastAPI backend

---

### 🛠️ Tech Stack

| Layer        | Stack                          |
| ------------ | ------------------------------ |
| Backend      | FastAPI, Python, GROQ API      |
| Frontend     | HTML, Tailwind CSS, Vanilla JS |
| Image Proc.  | Pillow, base64, io             |
| Templating   | Jinja2                         |
| Logging      | Python `logging` module        |
| Env Handling | `python-dotenv`                |

---

### ⚙️ Setup Instructions

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-doctor-chatbot.git
cd ai-doctor-chatbot
```

#### 2. Create `.env` File

Create a `.env` file in the root directory and add your **GROQ API Key**:

```
GROQ_API_KEY=your_groq_api_key_here
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure `fastapi`, `uvicorn`, `python-dotenv`, `pillow`, and `requests` are included.

#### 4. Run the App

```bash
uvicorn main:app --reload
```

Access the web app at [http://localhost:8000](http://localhost:8000)

---

### 🧪 How It Works

1. Upload an image (e.g., X-ray, chart, etc.)
2. Type a medical or visual question
3. The app sends the image and question to both vision models via GROQ's API
4. Responses are displayed on-screen in Markdown format

---

### 📁 File Structure

```
.
├── main.py               # FastAPI app
├── analyze_image.py      # Core logic for processing images
├── templates/
│   └── index.html        # Main HTML template (with Tailwind UI)
├── static/               # Optional static files (JS/CSS if needed)
├── .env                  # Environment variables (not tracked by Git)
├── requirements.txt      # Python dependencies
```

---

### 🛡️ Security Notes

- Your API key is stored in a `.env` file (never commit this file!)
- Always validate and sanitize uploaded content
- For production, ensure HTTPS and use proper access controls

---

### 🚧 TODOs / Future Enhancements

- Add user authentication
- Allow selection between models before submission
- Save and view past queries/responses
- Support more image formats and sizes

---

### 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

### 📄 License

Add your preferred license here (MIT, Apache 2.0, etc.)
