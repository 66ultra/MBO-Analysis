# importing necessary libraries
import pandas as pd

# merging datasets for analysis in my EDA file
def merge_data(bom_movie_gross_df, movie_basics_df, movie_ratings_df, tmdb_movies_df, tn_movie_budgets_df):
    # merging based off most logical joining methods
    # merging im.db data
    imdb_df = pd.merge(movie_basics_df, movie_ratings_df, on='movie_id')
    # merging bom_movie data with merged im.db data
    merged_df = pd.merge(bom_movie_gross_df, imdb_df, left_on='title', right_on='primary_title', how='inner')
    # merging merged data result with tmdb_movies data
    merged_df = pd.merge(merged_df, tmdb_movies_df, left_on='primary_title', right_on='title', how='inner')
    # merging merged data result with tn_movie_budgets data
    merged_df = pd.merge(merged_df, tn_movie_budgets_df, left_on='primary_title', right_on='movie', how='inner')
    
    return merged_df