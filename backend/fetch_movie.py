import requests
from config import OMDB_API_KEY

def fetch_movie_details(movie_name):
   
    url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={movie_name}"
    response = requests.get(url)
    data = response.json()
    
    
    if data.get("Response", "False") == "False":
        return None

    
    title = data.get("Title")
    summary = data.get("Plot", "No summary available.")
    genres = data.get("Genre", "Unknown")  
    
    return {
        "title": title,
        "summary": summary,
        "genres": genres
    }
