from fastapi import FastAPI
from app.routes import auth, profile

app = FastAPI(title="ScholarPath AI")

app.include_router(auth.router)
app.include_router(profile.router)

@app.get("/")
def root():
    return {"message": "ScholarPath AI API is running"}
