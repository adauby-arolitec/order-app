from fastapi import FastAPI

app = FastAPI()

@app.get("/greeting")
def greeting():
    return {"message": "Hello World"}