# 🧠 AI-Powered Medical Chatbot with Image & Symptom Analysis

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀-green)
![Groq](https://img.shields.io/badge/Groq-API-red)

This medica chatbot is an AI powered web based medical chatbot that allows users to upload **medical images** and describe their symptoms. It then intelligently analyzes both inputs using Groq's Vision Language Models to provide **diagnoses, insights, and explanations**.

---

## 🔍 Features

- 🖼️ Upload retinal/OCT or other medical images
- 🧾 Enter symptoms or ask questions
- 🧠 Uses Groq’s large multimodal language models to generate answers
- 🔐 Secure API key management via `.env`
- 📦 Built with FastAPI and Jinja2 templates
- ⚡ Clean, modular, and ready for deployment

---

## 📸 Demo

> Upload a fundus image and ask:  
> _"What eye disease does this image indicate?"_  
>  

> Response (from LLaMA Vision):  
> _"The image suggests signs of diabetic retinopathy with scattered hemorrhages..."_

---

## 🏗️ Project Structure

├── main.py # FastAPI app (uses multiple models)                                          
├── app.py # Slimmed version (uses one model)                                            
├── templates/                                                                                                                                                                                                └── index.html # Frontend form  
                                                     
├── .env # API keys (not pushed to GitHub)                                           
├── requirements.txt # Dependencies                                                        
└── README.md # This file                                                                 

## 📤 How It Works

- Upload an image and type a query (symptoms or questions)
- The image is verified, converted to base64, and sent along with the query to Groq’s API.
- The selected vision language model (meta-llama/llama-4-scout-17b-16e-instruct) analyzes both inputs.
- The response is displayed to the user.

## 🛠️ Technologies Used

├── main.py # FastAPI app (uses multiple models)  
├── app.py # Slimmed version (uses one model)  
├── templates/ └── index.html # Frontend form

├── .env # API keys (not pushed to GitHub)  
├── requirements.txt # Dependencies  
└── README.md # This file

## 📤 How It Works

- Upload an image and type a query (symptoms or questions)
- The image is verified, converted to base64, and sent along with the query to Groq’s API.
- The selected vision language model (meta-llama/llama-4-scout-17b-16e-instruct) analyzes both inputs.
- The response is displayed to the user.

## 🛠️ Technologies Used

- FastAPI
- Groq API
- Pillow – for image validation
- Requests
- dotenv

## 🧪 To Run

```
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
python app.py
```
