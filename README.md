# Dynamic Movie Similarity Analyzer

## Overview

The Dynamic Movie Similarity Analyzer is a system that dynamically fetches movie details, computes semantic similarities between movies, and recommends the top two most similar movies based on storyline and genre. This project leverages advanced NLP techniques such as Sentence-BERT for generating embeddings and FAISS for efficient similarity search, all exposed via a FastAPI backend with a React frontend.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Workflow](#workflow)
- [Tools and Technologies](#tools-and-technologies)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Design Choices](#design-choices)
- [Usage](#usage)
- [Additional Information](#additional-information)

## Features

- **Dynamic Data Fetching:** Fetch movie details (summary, genres) from the OMDb API.
- **Advanced Embeddings:** Utilize Sentence-BERT to generate semantic embeddings for movie summaries.
- **Efficient Similarity Search:** Use FAISS for fast similarity calculations.
- **Detailed Recommendations:** Return the top 2 similar movies along with similarity scores and justification (storyline similarity and genre overlap).
- **Clean UI with Autocomplete:** React-based user interface with an autocomplete search box using `react-select/async`.
- **Secure API Key Management:** API keys are stored in environment variables to prevent exposure in the source code.

## Workflow

1. **Data Preprocessing and Preloading:**

   - **Database Initialization:** SQLAlchemy is used to create a SQLite (or PostgreSQL) database.
   - **Movie Preloading:** A script fetches details of 20 preselected movies from the OMDb API, generates embeddings using Sentence-BERT, and stores them in the database.
   - **Duplicate Prevention:** The preload script checks if the database already contains movie records to avoid duplicate entries.

2. **Dynamic Movie Processing:**

   - **New Movie Input:** When a user inputs a movie title, the backend fetches its details from the OMDb API.
   - **Similarity Calculation:** The movie's summary is embedded and compared against preloaded embeddings using FAISS.
   - **Recommendation Generation:** The system returns the top 2 similar movies along with similarity scores and detailed justifications.

3. **Frontend UI:**
   - **Movie Search:** An autocomplete-enabled search box allows users to search for movies.
   - **Display Recommendations:** The recommended movies are displayed in a clean, responsive layout with detailed explanations.

## Tools and Technologies

- **Backend:**

  - **FastAPI:** A modern, fast web framework for building RESTful APIs.
  - **SQLAlchemy:** ORM for database interactions.
  - **FAISS:** Efficient similarity search library for high-dimensional data.
  - **Sentence-BERT:** State-of-the-art embeddings for capturing semantic meaning.
  - **OMDb API:** Source for movie data.
  - **python-dotenv:** For managing environment variables.

- **Frontend:**
  - **React.js:** JavaScript library for building user interfaces.
  - **Axios:** For making API requests.
  - **react-select/async:** For implementing an autocomplete search box.
  - **Traditional CSS:** For styling the user interface.

## Setup Instructions

### Backend Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Bhaskar1612/Movie_Analysis.git
   cd backend

   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate

   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

   ```

4. **Set Up Environment Variables:**

   ```env
   OMDB_API_KEY=your_actual_omdb_api_key_here

   ```

5. **Run the Backend Server:**

   ```bash
   uvicorn main:app --reload

   ```

### Backend Setup

1. **Navigate to the Frontend Directory:**

   ```bash
   cd ../frontend

   ```

2. **Install Dependencies:**

   ```bash
   npm install

   ```

3. **Set Up Environment Variables:**

   ```env
   REACT_APP_OMDB_API_KEY=your_actual_omdb_api_key_here

   ```

4. **Run the Frontend Server:**

   ```bash
   npm start

   ```

## Design Choices

### Sentence-BERT for Embeddings:

Chosen for its ability to capture semantic nuances, resulting in more accurate similarity assessments compared to traditional keyword matching.

### FAISS for Similarity Search:

Selected for its efficiency and scalability in performing similarity searches on high-dimensional data, which is crucial as the dataset grows.

### OMDb API:

The OMDb API is used for dynamic movie data fetching due to its accessibility and reliability in providing movie details. It is a good alternative to TMDB, especially in regions where TMDB might be inaccessible.

### React with Autocomplete UI:

A React-based UI with an autocomplete search box (powered by react-select/async) offers a user-friendly experience, making it easy for users to search and select movies.

### Environment Variables for API Keys:

Sensitive API keys are stored in environment variables, loaded via python-dotenv in the backend and prefixed with REACT*APP* in the frontend, ensuring they are not exposed in the source code.

## Usage

### Backend API Endpoints:

- GET / - Returns a welcome message.
- GET /recommend/{movie_name} - Returns movie recommendations for the provided movie title.

### Frontend:

- Use the search box to enter a movie title.
- Autocomplete suggestions will appear as you type.
- After selecting a movie, recommendations along with similarity scores and detailed justifications will be displayed.

## Additional Information

### Error Handling:

The system includes robust error handling for scenarios such as invalid movie names, failed API requests, and duplicate data entries during preload.

### Future Enhancements:

- Adding unit tests for key functionalities.
- Enhancing logging for better debugging and monitoring.
- Integrating additional visualizations for similarity scores.
- Using a backend proxy to further secure API keys used in the frontend.
