from fastapi import FastAPI, Query
from .analyze import analyze_topic
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from all origins (for development only)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict to ["http://localhost:5500"] if using live server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Twitter Sentiment Analysis API is up and running!"}

@app.get("/analyze")
async def analyze(topic: str = Query(..., description="Topic or hashtag to search")):
    result = analyze_topic(topic)
    return result
