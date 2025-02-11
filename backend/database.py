from sqlalchemy.orm import Session
from models import Movie, SessionLocal
from fetch_movie import fetch_movie_details
from embedding import get_embedding


PRELOADED_MOVIES = [
    "Inception", "The Matrix", "Interstellar", "The Dark Knight",
    "The Godfather", "Forrest Gump", "The Shawshank Redemption", "Pulp Fiction",
    "Fight Club", "Titanic", "Gladiator", "The Lion King", "Avatar",
    "The Avengers", "Parasite", "Joker", "The Social Network", "Whiplash"
]

def preload_movies():
    session = SessionLocal()
    movie_count = session.query(Movie).count()
    if movie_count > 0:
        print("Movies already preloaded, skipping preload.")
        session.close()
        return
    for title in PRELOADED_MOVIES:
        data = fetch_movie_details(title)
        if data:
            embedding = get_embedding(data["summary"])
            movie = Movie(title=data["title"], summary=data["summary"], genres=data["genres"], embedding=embedding)
            session.add(movie)
    session.commit()
    session.close()


