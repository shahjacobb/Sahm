from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import stock
from app.services.openai_service import initialize_openai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="OpenAI Stock Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

initialize_openai(os.getenv("OPENAI_API_KEY"))

app.include_router(stock.router, prefix="/api", tags=["stock"])

@app.get("/")
async def root():
    return {"message": "Welcome to the OpenAI Stock Analysis API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)