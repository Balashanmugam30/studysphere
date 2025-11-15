from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

# Create the FastAPI app
app = FastAPI(title="StudySphere Backend")

# CORS setup (required for your frontend to send requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for hackathon demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")


# -----------------------------
#   CHAT ROUTE (AI Answers)
# -----------------------------
@app.post("/ask")
async def ask_ai(payload: dict):
    question = payload.get("question", "")
    if not question:
        return {"answer": "Please provide a valid question."}

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}],
            max_tokens=400,
            temperature=0.6
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return {"answer": answer}

    except Exception as e:
        return {"answer": f"Backend error: {str(e)}"}


# -----------------------------
#   QUIZ ROUTE (Generate Quiz)
# -----------------------------
@app.post("/quiz")
async def generate_quiz(payload: dict = None):
    prompt = """
    Generate exactly 3 multiple-choice questions (MCQs) based on engineering topics.
    For each question, include:
    - Question
    - 4 options (A, B, C, D)
    - Correct Answer

    Format very cleanly.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return {"answer": answer}

    except Exception as e:
        return {"answer": f"Backend error: {str(e)}"}


# -----------------------------
#   HEALTH CHECK ROUTE
# -----------------------------
@app.get("/")
async def root():
    return {"message": "StudySphere Backend is running successfully!"}
