import streamlit as st
import pandas as pd
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CineMatch - Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# APPLICATION TITLE
# ==========================================

st.title("🎬 CineMatch")
st.subheader("Discover movies you'll love")

st.write(
    "An intelligent movie recommendation system "
    "powered by machine learning."
)

st.divider()

# ==========================================
# LOAD DATASET
# ==========================================

@st.cache_data
def load_data():

    # Load ratings
    ratings = pd.read_csv(
        "dataset/ml-100k/u.data",
        sep="\t",
        names=[
            "user_id",
            "movie_id",
            "rating",
            "timestamp"
        ]
    )

    # Load movie information
    movie_columns = [
        "movie_id", "title", "release_date",
        "video_release_date", "imdb_url", "unknown",
        "Action", "Adventure", "Animation", "Children",
        "Comedy", "Crime", "Documentary", "Drama",
        "Fantasy", "Film-Noir", "Horror", "Musical",
        "Mystery", "Romance", "Sci-Fi", "Thriller",
        "War", "Western"
    ]

    movies = pd.read_csv(
        "dataset/ml-100k/u.item",
        sep="|",
        encoding="latin-1",
        names=movie_columns
    )

    return ratings, movies


ratings, movies = load_data()

st.success("MovieLens dataset loaded successfully!")

# ==========================================
# LOAD DATASET
# ==========================================

@st.cache_data
def load_data():

    # Load ratings
    ratings = pd.read_csv(
        "dataset/ml-100k/u.data",
        sep="\t",
        names=[
            "user_id",
            "movie_id",
            "rating",
            "timestamp"
        ]
    )

    # Load movie information
    movie_columns = [
        "movie_id", "title", "release_date",
        "video_release_date", "imdb_url", "unknown",
        "Action", "Adventure", "Animation", "Children",
        "Comedy", "Crime", "Documentary", "Drama",
        "Fantasy", "Film-Noir", "Horror", "Musical",
        "Mystery", "Romance", "Sci-Fi", "Thriller",
        "War", "Western"
    ]

    movies = pd.read_csv(
        "dataset/ml-100k/u.item",
        sep="|",
        encoding="latin-1",
        names=movie_columns
    )

    return ratings, movies


ratings, movies = load_data()

st.success("MovieLens dataset loaded successfully!")

# ==========================================
# MOVIE STATISTICS
# ==========================================

movie_stats = ratings.groupby("movie_id").agg(
    average_rating=("rating", "mean"),
    total_ratings=("rating", "count")
).reset_index()

# Merge statistics with movie information
movie_stats = movies.merge(
    movie_stats,
    on="movie_id",
    how="left"
)

movie_stats["average_rating"] = (
    movie_stats["average_rating"].fillna(0)
)

movie_stats["total_ratings"] = (
    movie_stats["total_ratings"].fillna(0)
)

# Weighted rating
C = ratings["rating"].mean()
m = 50

movie_stats["weighted_rating"] = (
    (movie_stats["total_ratings"] /
     (movie_stats["total_ratings"] + m))
    * movie_stats["average_rating"]
    +
    (m /
     (movie_stats["total_ratings"] + m))
    * C
)

# ==========================================
# DASHBOARD METRICS
# ==========================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Movies",
    f"{len(movies):,}"
)

col2.metric(
    "Total Ratings",
    f"{len(ratings):,}"
)

col3.metric(
    "Total Users",
    f"{ratings['user_id'].nunique():,}"
)

col4.metric(
    "Average Rating",
    round(ratings["rating"].mean(), 2)
)

st.divider()