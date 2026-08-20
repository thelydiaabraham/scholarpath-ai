from fastapi import FastAPI
from app.routes import auth

app = FastAPI(title="ScholarPath AI")

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "ScholarPath AI API is running"}
    