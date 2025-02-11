import faiss
import numpy as np
from sqlalchemy.orm import Session
from models import SessionLocal, Movie
from embedding import get_embedding
from sklearn.metrics.pairwise import cosine_similarity

def get_faiss_index():
    session = SessionLocal()
    movies = session.query(Movie).all()
    
    embeddings = np.array([m.embedding for m in movies], dtype=np.float32)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    
    return index, movies

def compute_genre_overlap(genres1, genres2):
    set1, set2 = set(genres1.split(", ")), set(genres2.split(", "))
    common_genres = set1.intersection(set2)
    return len(common_genres), list(common_genres)

def find_similar_movies(new_movie_summary, new_movie_genres):
    index, movies = get_faiss_index()
    query_embedding = np.array([get_embedding(new_movie_summary)], dtype=np.float32)

    distances, indices = index.search(query_embedding, k=2)

    results = []
    for j, i in enumerate(indices[0]):
        movie = movies[i]
        score = round(100 - distances[0][j], 2)  
        genre_overlap_count, common_genres = compute_genre_overlap(new_movie_genres, movie.genres)

        
        query_emb = np.array(get_embedding(new_movie_summary)).reshape(1, -1)
        movie_emb = np.array(movie.embedding).reshape(1, -1)
        storyline_similarity = round(float(cosine_similarity(query_emb, movie_emb)[0][0]) * 100, 2)

        results.append({
            "title": movie.title,
            "similarity_score": score,
            "common_genres": common_genres,
            "genre_match_count": genre_overlap_count,
            "storyline_similarity": storyline_similarity
        })
    
    return results
