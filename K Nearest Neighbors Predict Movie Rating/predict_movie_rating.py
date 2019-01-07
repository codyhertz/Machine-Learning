import pandas as pd
import numpy as np
from scipy import spatial
import operator


r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('./ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))

movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.mean(x)))

movieDict = {}
with open('./ml-100k/u.item') as f:
    temp = ''
    for line in f:
        fields = line.rstrip('\n').split('|')

        movieId = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = list(map(int, genres))

        movieDict[movieId] = (name, genres, movieNormalizedNumRatings.loc[movieId].get("size"), movieProperties.loc[movieId].rating.get('mean'))

def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]
    genreDistance = spatial.distance.cosine(genresA, genresB)

    popularityA = a[2]
    popularityB = b[2]

    popularityDistance = abs(popularityA - popularityB)

    return genreDistance + popularityDistance

def getNeighbors(movieId, k):
    distances = []
    for movie in movieDict:
        if movie != movieId:
            dist = ComputeDistance(movieDict[movieId], movieDict[movie])
            distances.append((movie, dist))

    distances.sort(key=operator.itemgetter(1))

    neighbors = []

    for x in range(k):
        neighbors.append(distances[x][0])

    return neighbors

k = 10
avgRating = 0
neighbors = getNeighbors(1, k)
print("Top 10 movies similar to", movieDict[1][0])
for neighbor in neighbors:
    avgRating += movieDict[neighbor][3]
    print(movieDict[neighbor][0] + " " + str(movieDict[neighbor][3]))

avgRating /= float(k)

print()
print("Predicted Rating:", avgRating)
print('Real Rating:', movieDict[1][len(movieDict[1]) - 1])
