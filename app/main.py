from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from language_detection import detect_language
from json_handler import load_data

app = FastAPI()

class UserInput(BaseModel):
    text: str

@app.get('/')
def index():
    return 'Hello World'

@app.get('/load_data')
def load_data_endpoint():
    try:
        return load_data()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post('/detect')
def detect(input: UserInput):
    try:
        return detect_language(input.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))