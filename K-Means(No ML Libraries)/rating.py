from kmeans_alg import distance, findCentroid

def getRating(clusters):
    cluster_rating = 0
    empty_clusters = 0

    for cluster in clusters:
        centroid = findCentroid(cluster)
        if centroid:
            average_distance_from_center = 0

            for point in cluster:
                average_distance_from_center += distance(point, centroid)

        if len(cluster) is 0:
            empty_clusters += 1
        else:
            average_distance_from_center /= len(cluster)

        cluster_rating += average_distance_from_center

    cluster_rating /= (len(clusters) - empty_clusters)

    return cluster_rating

def highestRating(ratings):
    best = 0

    for i in range(len(ratings)):
        if ratings[best] > ratings[i]:
            best = i

    return best + 1
