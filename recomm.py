import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data = {
    'title': ['Inception', 'The Matrix', 'Interstellar', 'The Notebook', 'Titanic'],
    'genre': ['Action Sci-Fi', 'Action Sci-Fi', 'Adventure Sci-Fi', 'Romance Drama', 'Romance Drama']
}

df = pd.DataFrame(data)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df['genre'])

similarity = cosine_similarity(count_matrix)

def recommend(movie):
    if movie not in df['title'].values:
        return "Movie not found."
    idx = df[df['title'] == movie].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:]
    result = [df['title'][i[0]] for i in sorted_scores[:2]]
    return result

# Get user input
movie_title = input("Enter a movie title: ")

# Print recommendations
print(f"Recommendations for '{movie_title}':", recommend(movie_title))
