from fastapi import FastAPI
from pydantic import BaseModel
from app.extract_reviews import extract_reviews
from app.process_reviews import process_reviews
from app.load_reviews import load_reviews
import uvicorn

app = FastAPI()

class MovieInput(BaseModel):
    movieID: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Allow get requests to the /sentiment-analysis endpoint
@app.get("/sentiment-analysis")
def sentiment_analysis(movieID: int): 
    reviews   = extract_reviews(movieID)
    processed = process_reviews(reviews)
    # result    = load_reviews(processed)
    return {"result": processed}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)