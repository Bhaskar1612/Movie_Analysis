// MovieRecommendations.js
import React, { useState } from "react";
import axios from "axios";
import MovieSearch from "./MovieSearch";
import "./MovieRecommendations.css";

const MovieRecommendations = () => {
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchRecommendations = async (movie) => {
    setLoading(true);
    setError("");
    try {
      const response = await axios.get(`http://localhost:8000/recommend/${movie}`);
      setRecommendations(response.data.top_matches);
    } catch (err) {
      setError("Could not fetch recommendations. Try another movie.");
    }
    setLoading(false);
  };

  return (
    <div className="movie-rec-container">
      <h1 className="movie-rec-heading">Movie Similarity Analyzer</h1>
      <MovieSearch onSelect={fetchRecommendations} />
      
      {loading && <p className="loading-message">Loading...</p>}
      {error && <p className="error-message">{error}</p>}

      <div className="results-container">
        {recommendations.length > 0 && (
          <div>
            <h2 className="results-heading">Top Similar Movies:</h2>
            {recommendations.map((movie, index) => (
              <div key={index} className="movie-card">
                <h3 className="movie-title">{movie.title}</h3>
                <p className="similarity-score">Similarity Score: {movie.similarity_score}%</p>
                <div className="movie-justification">
                  <p>🔹 {movie.justification.storyline_similarity}</p>
                  <p>🔹 {movie.justification.genre_overlap}</p>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default MovieRecommendations;
