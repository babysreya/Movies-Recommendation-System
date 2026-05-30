import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity

st.title("Movie Recommendation System")

# Load movies
with open("movies.pickle", "rb") as m:
    movies = pickle.load(m)

# Load vectors
with open("vectors.pkl", "rb") as f:
    vectors = pickle.load(f)

movie_names = movies['title'].values


def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    movie_vector = vectors[movie_index].reshape(1,-1)

    recommendations = cosine_similarity(
        movie_vector,
        vectors
    ).flatten()

    movie_list = sorted(
        enumerate(recommendations),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


name_movie = st.selectbox(
    "Enter the Movie Name",
    movie_names
)

if st.button("Recommend"):

    recommendations = recommend(name_movie)

    st.write("The recommended movies are:")

    for movie in recommendations:
        st.write(movie)