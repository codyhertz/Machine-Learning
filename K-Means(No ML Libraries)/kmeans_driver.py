from random import randint
from kmeans_alg import kMeansRun
from rating import getRating, highestRating
from conversion import convertToAPointValuesKMeans

k = 3
s = [[2, 10],
      [2, 5],
      [8, 4],
      [5, 8],
      [7, 5],
      [6, 4],
      [1, 2],
      [4, 9]]

run_ratings = []

print('K-Means with initial centers at A1, A7 and A8\n')
run1 = kMeansRun(3, s, s[0], s[6], s[7])

count = 0

print('Final clusters(points):')
for cluster in run1:
    print('\tCluster', count, cluster)
    count += 1

count = 0

print('Final clusters(A names):')
for cluster in run1:
    print('\tCluster', count, convertToAPointValuesKMeans(cluster))
    count += 1

print()
print('K-Means with initial centers at A2, A6 and A8\n')
run2 = kMeansRun(3, s, s[1], s[5], s[7])

count = 0

print('Final clusters(points):')
for cluster in run2:
    print('\tCluster', count, cluster)
    count += 1

count = 0

print('Final clusters(A names):')
for cluster in run2:
    print('\tCluster', count, convertToAPointValuesKMeans(cluster))
    count += 1

print()
print('K-Means with initial centers at A3, A5 and A6\n')
run3 = kMeansRun(3, s, s[2], s[4], s[5])

count = 0

print('Final clusters(points):')
for cluster in run3:
    print('\tCluster', count, cluster)
    count += 1

count = 0

print('Final clusters(A names):')
for cluster in run3:
    print('\tCluster', count, convertToAPointValuesKMeans(cluster))
    count += 1

print()
print('K-Means with initial centers at A2, A3 and A7\n')
run4 = kMeansRun(3, s, s[1], s[2], s[6])

count = 0

print('Final clusters(points):')
for cluster in run4:
    print('\tCluster', count, cluster)
    count += 1

count = 0

print('Final clusters(A names):')
for cluster in run4:
    print('\tCluster', count, convertToAPointValuesKMeans(cluster))
    count += 1

print()

run_ratings.append(getRating(run1))
run_ratings.append(getRating(run2))
run_ratings.append(getRating(run3))
run_ratings.append(getRating(run4))

stop = False
stopStr = ''

while not stop:
    print('K-Means with random initial centers\n')
    randomRun = kMeansRun(3, s, [randint(0, 10), randint(0, 10)], [randint(0, 10), randint(0, 10)], [randint(0, 10), randint(0, 10)])

    count = 0

    print('Final clusters(points):')
    for cluster in randomRun:
        print('\tCluster', count, cluster)
        count += 1

    run_ratings.append(getRating(randomRun))

    print()
    stopStr = input('Would you like to run k-means another time? (Y/N): ')

    if stopStr is 'y' or stopStr is 'Y':
        stop = False
        print()
    else:
        stop = True

highest_rating = highestRating(run_ratings)

print('\n\nThe best results are from run', highest_rating)
