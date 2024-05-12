from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn
from app.routes import router

load_dotenv()

app = FastAPI()

app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=int(os.getenv("PORT", 8000)), reload=True)
