# Importing spacy
import spacy

# Load the dataframes
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Medium spaCy model
nlp = spacy.load('en_core_web_md')

# Tokenisation of the text
def tokenise(text):
   
    tokendoc = nlp(text)
    return [token.text.lower() for token in tokendoc if token.is_alpha]

# Vectorisation of the text
def vectorise(text):
   
    vectordoc = nlp(text)
    return np.array([vectordoc.vector])
    #return vectordoc.vector

# The process of finding similarities in a movie
def recommend_movie(movie_descriptions, target_movie, target_description):
   
    target_description = movie_descriptions[target_movie]
    similarities = {}
    for movie, description in movie_descriptions.items():
        if movie == target_movie:
            continue
        similarities[movie] = cosine_similarity(vectorise(target_description), vectorise(description))
    return max(similarities, key=similarities.get)

# The descriptions of the movies
movie_descriptions = {}
# Opening 'movies.txt' file
with open('movies.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if len(line.strip())==0:
            continue
        # Split using the : to get movie name and description
        parts = line.strip().split(':', 1)
        if len(parts) == 2:  # If both movie name and description are there
            movie, description = parts
            movie_descriptions[movie.strip()] = description.strip()  # Strip lead/trailing space from both movie and description
        else:  # If there is no movie name assume it's for "Planet Hulk"
            movie_descriptions["Planet Hulk"] = line.strip()
            #print(parts, line)
            
# Find similar movie to "Planet Hulk"
target_movie = "Planet Hulk"
target_description = movie_descriptions[target_movie]
recommended_movie = recommend_movie(movie_descriptions, target_movie, target_description)
print(f"Recommended movie to watch after '{target_movie}': {recommended_movie}")