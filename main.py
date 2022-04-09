from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def appget():
    return {"text": "hellow mama"}