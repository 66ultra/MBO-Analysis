# importing necessary libraries
import pandas as pd
import sqlite3

# loading bom_movie_gross from source file
def load_bom_movie_gross(filepath='../zippedData/bom.movie_gross.csv.gz'):
    return pd.read_csv(filepath, compression='gzip')

#loading tmdb_movies from source file
def load_tmdb_movies(filepath='../zippedData/tmdb.movies.csv.gz'):
    return pd.read_csv(filepath, compression='gzip')

# loading tn_movie_budgets from source file
def load_tn_movie_budgets(filepath='../zippedData/tn.movie_budgets.csv.gz'):
    return pd.read_csv(filepath, compression='gzip')

# loading the im.db database from source file
def load_sqlite_db(filepath='../zippedData/im.db'):
    # establishing a connection to the SQLite database
    conn = sqlite3.connect(filepath)
    # reading movie_basics table into a DataFrame
    movie_basics = pd.read_sql("SELECT * FROM movie_basics", conn)
    # reading movie_ratings table into a DataFrame
    movie_ratings = pd.read_sql("SELECT * FROM movie_ratings", conn)
    # closing the connection to the database
    conn.close()
    
    return movie_basics, movie_ratings