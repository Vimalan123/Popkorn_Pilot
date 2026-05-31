import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import json
import random

def load_and_prepare_data():
    """Loads, merges, and cleans the movie data with robust error handling."""
    try:
        movies_df = pd.read_csv('tmdb_5000_movies.csv')
        credits_df = pd.read_csv('tmdb_5000_credits.csv')
    except FileNotFoundError:
        print("Error: Make sure 'tmdb_5000_movies.csv' and 'tmdb_5000_credits.csv' are in the same directory.")
        return None

    possible_movie_id_cols = ['id', 'movie_id', 'tmdbId']
    movie_id_col = next((col for col in possible_movie_id_cols if col in movies_df.columns), None)
    
    if movie_id_col is None:
        print(f"Error: Could not find a movie ID column in 'tmdb_5000_movies.csv'. Expected one of {possible_movie_id_cols}.")
        return None

    movies_df.rename(columns={movie_id_col: 'movie_id'}, inplace=True)
    
    if 'movie_id' not in credits_df.columns:
        print("Error: 'movie_id' column not found in 'tmdb_5000_credits.csv'.")
        return None
        
    movies_df['movie_id'] = movies_df['movie_id'].astype(str)
    credits_df['movie_id'] = credits_df['movie_id'].astype(str)

    df = movies_df.merge(credits_df, on='movie_id')
    
    features = ['movie_id', 'title_x', 'overview', 'genres', 'keywords', 'cast', 'crew']
    df = df[features]
    df = df.rename(columns={'title_x': 'title'})

    for feature in ['genres', 'keywords', 'cast', 'crew']:
        df[feature] = df[feature].apply(safe_json_loads)

    df['director'] = df['crew'].apply(get_director)

    for feature in ['genres', 'keywords']:
        df[feature] = df[feature].apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
    df['cast'] = df['cast'].apply(lambda x: [i['name'] for i in x[:3]] if isinstance(x, list) else [])

    for feature in ['cast', 'keywords', 'genres', 'director']:
        df[feature] = df[feature].apply(clean_data)

    df['soup'] = df.apply(create_soup, axis=1)
    
    return df

def safe_json_loads(data):
    """Safely parse JSON strings, returning an empty list on error."""
    if pd.isna(data):
        return []
    try:
        return json.loads(data.replace("'", '"'))
    except (json.JSONDecodeError, TypeError):
        return []

def get_director(crew_list):
    """Extract the director's name from the crew list."""
    if isinstance(crew_list, list):
        for member in crew_list:
            if member.get('job') == 'Director':
                return member.get('name', '')
    return ''

def clean_data(x):
    """Cleans data by removing spaces."""
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    elif isinstance(x, str):
        return str.lower(x.replace(" ", ""))
    else:
        return ''

def create_soup(x):
    """Combines all relevant features into a single string for vectorization."""
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])



def create_recommendation_engine(df):
    """Builds the TF-IDF matrix and cosine similarity matrix."""
    tfidf = TfidfVectorizer(stop_words='english')
    df['soup'] = df['soup'].fillna('')
    tfidf_matrix = tfidf.fit_transform(df['soup'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()
    return cosine_sim, indices

def get_recommendations(title, cosine_sim, indices, df):
    """Fetches recommendations for a given movie title."""
    if title not in indices:
        matching_titles = [t for t in indices.keys() if t.lower() == title.lower()]
        if not matching_titles:
            return f"Sorry, the movie '{title}' was not found in our database."
        title = matching_titles[0]
            
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()



def chatbot():
    """Main function to run the chatbot conversation."""
    print("🎬 Welcome to the Movie Recommendation Chatbot! 🎬")
    print("I can help you find movies similar to one you like.")
    
    movie_data = load_and_prepare_data()
    if movie_data is None:
        print("Could not load data. Exiting chatbot.")
        return
        
    cosine_sim, indices = create_recommendation_engine(movie_data)
    
    random_movies = random.sample(list(movie_data['title'].dropna()), 5)
    print("\nTo get started, you could ask for recommendations based on movies like:")
    for movie in random_movies:
        print(f"  - {movie}")
        
    print("\nType 'quit' or 'exit' to end the chat.")

    while True:
        user_input = input("\nEnter a movie title you like: ").strip()

        if user_input.lower() in ['quit', 'exit']:
            print("Thanks for chatting! Enjoy your movie night! 👋")
            break

        if user_input:
            recommendations = get_recommendations(user_input, cosine_sim, indices, movie_data)
            if isinstance(recommendations, list):
                print(f"\nGreat! If you liked '{user_input}', you might also enjoy these movies:")
                for i, movie in enumerate(recommendations):
                    print(f"  {i+1}. {movie}")
            else:
                print(recommendations)
        else:
            print("Please enter a movie title.")

if __name__ == '__main__':
    chatbot()