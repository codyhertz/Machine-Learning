import pandas as pd
import numpy as np


r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))

m_cols = ['movie_id', 'title']
movies = pd.read_csv('./ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding='latin1')

# combine dataframes
ratings = pd.merge(movies, ratings)

# make new dataframe where x=user_id, y=title, values in table=ratings
movieRatings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')

starWarsRatings = movieRatings['Star Wars (1977)']

# get movies that were watched by people who watched star wars
similarMovies = movieRatings.corrwith(starWarsRatings)
similar = similarMovies.dropna()
df = pd.DataFrame(similar)

similarMovies = similar.sort_values(ascending=False)

# clean data
movieStats = ratings.groupby('title').agg({'rating': [np.size, np.mean]}) # check how many people watched a movie and the average rating

popularMovies = movieStats['rating']['size'] >= 100
df = movieStats[popularMovies].join(pd.DataFrame(similarMovies, columns=['similarity'])) # get similar movies that are also popular

df = df.sort_values(['similarity'], ascending=False)[1:] # remove movie the movie from the list
print(df[:15]) #print 15 most similar
