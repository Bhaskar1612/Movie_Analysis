from fastapi import FastAPI, HTTPException
from fetch_movie import fetch_movie_details
from similarity import find_similar_movies
from models import init_db  
from database import preload_movies
from fastapi.middleware.cors import CORSMiddleware
 
init_db() 
preload_movies()

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Dynamic Movie Similarity Analyzer"}

@app.get("/recommend/{movie_name}")
def recommend_movie(movie_name: str):
    data = fetch_movie_details(movie_name)
    if not data:
        raise HTTPException(status_code=404, detail="Movie not found")

    similar_movies = find_similar_movies(data["summary"], data["genres"])
    
    response = {
        "input_movie": data["title"],
        "top_matches": []
    }
    
    for movie in similar_movies:
        response["top_matches"].append({
            "title": movie["title"],
            "similarity_score": movie["similarity_score"],
            "justification": {
                "storyline_similarity": f"{movie['storyline_similarity']}% storyline similarity",
                "genre_overlap": f"{movie['genre_match_count']} common genres: {', '.join(movie['common_genres'])}" if movie["common_genres"] else "No genre overlap"
            }
        })

    return response
