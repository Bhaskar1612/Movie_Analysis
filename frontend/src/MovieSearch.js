// MovieSearch.js
import React, { useState } from "react";
import AsyncSelect from "react-select/async";
import axios from "axios";
import "./MovieSearch.css";

const MovieSearch = ({ onSelect }) => {
  const [inputValue, setInputValue] = useState("");
  const API_KEY = process.env.REACT_APP_OMDB_API_KEY;

  const fetchMovies = async (input) => {
    if (!input) return [];
    try {
      const response = await axios.get(`http://www.omdbapi.com/`, {
        params: {
          apikey: API_KEY, 
          s: input,
        },
      });

      
      if (response.data && response.data.Search) {
        return response.data.Search.map((movie) => ({
          label: movie.Title,
          value: movie.Title,
        }));
      } else {
        return [];
      }
    } catch (error) {
      console.error("Error fetching movie suggestions:", error);
      return [];
    }
  };

  return (
    <div className="movie-search-container">
      <AsyncSelect
        cacheOptions
        loadOptions={fetchMovies}
        onInputChange={(val) => setInputValue(val)}
        onChange={(selected) => onSelect(selected.value)}
        placeholder="Search for a movie..."
        className="movie-search-select"
      />
    </div>
  );
};

export default MovieSearch;
