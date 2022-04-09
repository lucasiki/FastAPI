from fastapi import FastAPI
from a2wsgi import ASGIMiddleware

app = FastAPI()

@app.get('/')
def appget():
    return {"text": "hellow mama"}
    
    
    
    
    
    
wsgi_app = ASGIMiddleware(app)
    