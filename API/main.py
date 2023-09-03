# Importing necessary libraries
import uvicorn
import dill as pickle
import pandas as pd
import numpy as np
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import bz2

# Initializing the fast API server
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Loading up the model
with open('../model/movieRecommendations.pkl', 'rb') as file:
    model = pickle.load(file)
with open('../model/movieRecommendations2.pkl', 'rb') as f:
    indices = pickle.load(f)
with open('../model/movieRecommendations3.pkl', 'rb') as fi:
    movies_cleaned = pickle.load(fi)
with open('../model/movieRecommendations4.pkl', 'rb') as fil:
    setup = pickle.load(fil)
with bz2.BZ2File('../model/movieRecommendations5.pkl', 'rb') as new:
    sig = pickle.load(new)
    
# Defining the model input types
class Recommendation(BaseModel):
    title: str

# Setting up the home route
@app.get("/")
def read_root():
    return {"data": "This is a machine learning movie recommendation model"}

# Setting up the recommend route
@app.post("/recommend/")
async def get_recommendations(data: Recommendation):

    
    recommendations = model(setup(data.title))

    return {
        "data": {
            'movie1': recommendations[0],
            'movie2': recommendations[1],
            'movie3': recommendations[2],
            'movie4': recommendations[3],
            'movie5': recommendations[4],
            'movie6': recommendations[5],
            'movie7': recommendations[6],
            'movie8': recommendations[7],
            'movie9': recommendations[8],
            'movie10': recommendations[9]
        }
    }

# Configuring the server host and port
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
    
