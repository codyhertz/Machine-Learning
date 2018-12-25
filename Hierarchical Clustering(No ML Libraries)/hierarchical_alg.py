import copy
import sys
from conversion import convertToAPointValuesHierarchical

def distance(pt1, pt2):
    return (((pt2[0] - pt1[0]) ** 2) + ((pt2[1] - pt1[1]) ** 2)) ** .5

def findClosestPair(cluster1, cluster2):
    closest_pair = [cluster1[0], cluster2[0]]
    for i in range(len(cluster1)):
        for k in range(len(cluster2)):
            if distance(closest_pair[0], closest_pair[1]) > distance(cluster1[i], cluster2[k]):
                closest_pair = [cluster1[i], cluster2[k]]
    return closest_pair

def findFurthestPair(cluster1, cluster2):
    furthest_pair = [cluster1[0], cluster2[0]]
    for i in range(len(cluster1)):
        for k in range(len(cluster2)):
            if distance(furthest_pair[0], furthest_pair[1]) < distance(cluster1[i], cluster2[k]):
                furthest_pair = [cluster1[i], cluster2[k]]


    return furthest_pair

def createDistanceMatrix(clusters, length, linkage):
    distance_matrix = [[None for k in range(length)] for i in range(length)]

    if linkage is 'single':
        for i in range(length):
            for k in range(length):
                if clusters[i] != clusters[k]:
                    closest_pair = findClosestPair(clusters[i], clusters[k])
                    distance_matrix[i][k] = distance(closest_pair[0], closest_pair[1])
                else:
                    distance_matrix[i][k] = 0.0

    elif linkage is 'complete':
        for i in range(length):
            for k in range(length):
                if clusters[i] != clusters[k]:
                    furthest_pair = findFurthestPair(clusters[i], clusters[k])
                    distance_matrix[i][k] = distance(furthest_pair[0], furthest_pair[1])
                else:
                    distance_matrix[i][k] = 0.0


    return distance_matrix


def hierarchicalClustering(s, k, linkage):

    s2 = copy.deepcopy(s)

    clusters = [[] in range(len(s2))]
    dendrograph = []

    clusters[0] = copy.deepcopy(s2)

    print('Clusters round 0:')
    for x in s2:
        print('\t', x)
    print()

    for i in range(len(s2)-1):
        distance_matrix = createDistanceMatrix(clusters[i], len(clusters[i]), linkage)

        closest = sys.maxsize
        closest_x = 0
        closest_y = 0

        for j in range(len(clusters[i])):
            l = 0

            while distance_matrix[j][l] != 0.0:
                if closest > distance_matrix[j][l]:
                    closest = distance_matrix[j][l]
                    closest_x = l
                    closest_y = j
                l += 1

        if len(clusters[i]) is not 1:
            for point in s2[closest_y]:
                s2[closest_x].append(point)

        s2.remove(s2[closest_y])

        clusters.append(copy.deepcopy(s2))

        print('Clusters round {i}:'.format(i=i + 1))
        for x in s2:
            print('\t{x}'.format(x=x))
        print('\tClusters', closest_x, 'and', closest_y, 'merged.\n')

    print('Clustering results for k = {k}(points):'.format(k=k))
    for c in clusters[len(clusters) - k]:
        print('\t', c)

    print()
    print('Clustering results for k = {k}(A names):'.format(k=k))
    for c in clusters[len(clusters) - k]:
        print('\t', convertToAPointValuesHierarchical(c))
