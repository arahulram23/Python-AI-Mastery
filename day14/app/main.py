from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/about")
def about():
    return {"app": "FastAPI Application", "version": "1.0.0"}   