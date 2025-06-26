import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import quiz
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

ENV = os.getenv("ENV", "development")

if ENV == "production":
    allowed_origins = ["https://cutie-utensil-quiz.vercel.app"]
else:
    allowed_origins = [
        "http://localhost:8080",
        "https://cutie-utensil-quiz.vercel.app"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(quiz.router, prefix="/quiz")