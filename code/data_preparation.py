# importing necessary libraries
import pandas as pd
import numpy as np

# importing load functions created in my load_data file
from load_data import load_bom_movie_gross, load_sqlite_db, load_tmdb_movies, load_tn_movie_budgets

# importing my created merging function
import merge_data as md

# cleaning the bom_movie_gross dataset
def clean_bom_movie_gross(df):
    # filling the minimal nan values in foreign_gross after replacing special characters
    df['foreign_gross'] = df['foreign_gross'].str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['foreign_gross'] = df['foreign_gross'].fillna(0)
    df['studio'] = df['studio'].fillna('Unknown')
    df = df.dropna(subset=['domestic_gross'])
    return df

# cleaning the im.db selected tables
def clean_imdb_data(movie_basics_df, movie_ratings_df):
    # filling nan values where its needed with most logical methods
    movie_basics_df['runtime_minutes'] = movie_basics_df['runtime_minutes'].fillna(movie_basics_df['runtime_minutes'].median())
    movie_basics_df['genres'] = movie_basics_df['genres'].fillna('Unknown')
    movie_basics_df['original_title'] = movie_basics_df['original_title'].fillna(movie_basics_df['primary_title'])
    return movie_basics_df, movie_ratings_df

# cleaning tn_movie_budgets dataset
def clean_tn_movie_budgets(df):
    # replacing special characters
    df['production_budget'] = df['production_budget'].str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['domestic_gross'] = df['domestic_gross'].str.replace(r'[^\d.]+', '', regex=True).astype(float)
    df['worldwide_gross'] = df['worldwide_gross'].str.replace(r'[^\d.]+', '', regex=True).astype(float)
    return df

# cleaning tmdb_movies dataset
def clean_tmdb_movies(df):
    # dropping the index column that is not needed
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')
    # modifying datatypes to be accurate
    df['popularity'] = pd.to_numeric(df['popularity'], errors='coerce')
    df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
    df['vote_count'] = pd.to_numeric(df['vote_count'], errors='coerce')
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    return df

# specifying what columns to keep for analysis
def clean_columns(df):
    columns_to_keep = [
        'title_x', 'studio', 'domestic_gross_x', 'foreign_gross', 'production_budget', 'year',
        'runtime_minutes', 'genres', 'averagerating', 'numvotes', 'popularity', 'vote_average',
        'vote_count', 'worldwide_gross'
    ]
    
    df = df[columns_to_keep]
    
    # renaming columns to keep formatting
    df = df.rename(columns={
        'title_x': 'title',
        'domestic_gross_x': 'domestic_gross',
        'vote_average': 'tmdb_vote_average',
        'vote_count': 'tmdb_vote_count',
        'averagerating': 'average_rating',
        'numvotes': 'num_votes'
    })
    # handling zero values before log transformation
    df.loc[df['production_budget'] == 0, 'production_budget'] = 1
    df.loc[df['domestic_gross'] == 0, 'domestic_gross'] = 1
    df.loc[df['foreign_gross'] == 0, 'foreign_gross'] = 1
    df.loc[df['worldwide_gross'] == 0, 'worldwide_gross'] = 1
    df.loc[df['popularity'] == 0, 'popularity'] = 1
    
    # applying log1p transformation
    df['log_production_budget'] = np.log1p(df['production_budget'])
    df['log_domestic_gross'] = np.log1p(df['domestic_gross'])
    df['log_foreign_gross'] = np.log1p(df['foreign_gross'])
    df['log_worldwide_gross'] = np.log1p(df['worldwide_gross'])
    df['log_popularity'] = np.log1p(df['popularity'])
    df['log_num_votes'] = np.log1p(df['num_votes'])
    
    return df

# full clean function for EDA
def full_clean():
    # loading datasets
    bom_movie_gross_df = load_bom_movie_gross()
    movie_basics_df, movie_ratings_df = load_sqlite_db()
    tmdb_movies_df = load_tmdb_movies()
    tn_movie_budgets_df = load_tn_movie_budgets()
    
    # cleaning datasets using above functions
    bom_movie_gross_df = clean_bom_movie_gross(bom_movie_gross_df)
    movie_basics_df, movie_ratings_df = clean_imdb_data(movie_basics_df, movie_ratings_df)
    tn_movie_budgets_df = clean_tn_movie_budgets(tn_movie_budgets_df)
    tmdb_movies_df = clean_tmdb_movies(tmdb_movies_df)
    
    # merging cleaned datasets using the created merge function in merge_data.py
    merged_df = md.merge_data(bom_movie_gross_df, movie_basics_df, movie_ratings_df, tmdb_movies_df, tn_movie_budgets_df)
    merged_df = clean_columns(merged_df)
    
    return merged_df