from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

app = FastAPI(title="StudySphere Backend - DeepSeek")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"


@app.post("/ask")
async def ask_ai(payload: dict):
    question = payload.get("question", "")

    if not question:
        return {"answer": "Please provide a valid question."}

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": question}]
    }

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(DEEPSEEK_URL, json=data, headers=headers)
        result = response.json()

        # DeepSeek returns: result["choices"][0]["message"]["content"]
        answer = result["choices"][0]["message"]["content"]
        return {"answer": answer}

    except Exception as e:
        return {"answer": f"Backend error: {str(e)}"}


@app.post("/quiz")
async def generate_quiz(payload: dict = None):

    prompt = """
    Generate exactly 3 MCQs.
    Each must include:
    - Question
    - Options A, B, C, D
    - Correct answer (just the letter).
    """

    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}]
    }

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(DEEPSEEK_URL, json=data, headers=headers)
        result = response.json()
        
        answer = result["choices"][0]["message"]["content"]
        return {"answer": answer}

    except Exception as e:
        return {"answer": f"Backend error: {str(e)}"}


@app.get("/")
async def root():
    return {"message": "StudySphere DeepSeek backend running!"}
