import pandas as pd
import numpy as np

def getRecommendation(x, rating):
    if rating >= 3:
        return x * rating
    else:
        return x * (-1 * rating)

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))

m_cols = ['movie_id', 'title']
movies = pd.read_csv('./ml-100k/u.item', sep='|', names=m_cols, usecols=range(2), encoding='latin1')

# combine dataframes
ratings = pd.merge(movies, ratings)

# make new dataframe where x=user_id, y=title, values in table=ratings
userRatings = ratings.pivot_table(index=['user_id'], columns=['title'], values='rating')

corrMatrix = userRatings.corr(method='pearson', min_periods=100) # only the pairs of movies rated by 100 people

myRatings = userRatings.loc[0].dropna()

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print("Addings sims for " + myRatings.index[i] + "...")

    sims = corrMatrix[myRatings.index[i]].dropna() # retrieve similar movies to each movie i rated
    sims = sims.map(lambda x: getRecommendation(x, myRatings[i])) # scale by how well the movie i rated was rated
    simCandidates = simCandidates.append(sims)

print('Sorting...')
simCandidates.sort_values(inplace=True, ascending=False)
simCandidates = simCandidates.groupby(simCandidates.index).sum() # if a moveie is recommended more than once, make it more recommended
simCandidates.sort_values(inplace=True, ascending=False)

filteredSims = simCandidates.drop(myRatings.index) # remove movies ive already watched
print(filteredSims.head(10)) # top 10 recommended
