from dotenv import load_dotenv
import requests
import os

# Get the API key from .env file
dotenv_path = '../.env'
load_dotenv(dotenv_path)
API_KEY = os.getenv('API_KEY')

print(API_KEY)
def extract_reviews(movie_id):
    reviews = []
    for page in range(1, 6):
        url_reviews = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={API_KEY}&page={page}"
        response_reviews = requests.get(url_reviews)
        data_reviews = response_reviews.json()
        for review in data_reviews["results"]:
            reviews.append(review["content"])
    return reviews

if __name__ == "__main__":
    movie_id = "550"
    reviews = extract_reviews(movie_id)
    print(reviews)