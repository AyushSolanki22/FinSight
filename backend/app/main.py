from fastapi import FastAPI

app = FastAPI(
    title="FinSight API",   
    description="API for FinSight application"
)

@app.get("/")
def home():
    return {"message": "Welcome to the FinSight API!", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

