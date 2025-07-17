from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import json

app= FastAPI()
#CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model= joblib.load('mood_model.pkl')
vectorizer= joblib.load('vectorizer.pkl')

with open('songs.json', "r") as f:
    mood_to_songs= json.load(f)

class TextIn(BaseModel):
    text:str

#defining the input schema using pydantic
class TextIn(BaseModel):
    text:str

#endpoint to predict mood
@app.post("/predict")
def predict(data: TextIn):
    x= vectorizer.transform([data.text])
    mood=model.predict(x)[0]   
    songs= mood_to_songs.get(mood,[])
    return {"mood": mood, "songs": songs}