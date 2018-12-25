def distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def findClosest(arr, point):
    closest = 0

    for i in range(len(arr)):
        if distance(arr[closest], point) > distance(arr[i], point):
            closest = i

    return arr[closest]

def findCentroid(arr):
    if len(arr) is 0:
        return None

    x_total = 0
    y_total = 0

    for point in arr:
        x_total += point[0]
        y_total += point[1]

    x_total /= len(arr)
    y_total /= len(arr)

    centroid = [x_total, y_total]

    return centroid

def findClusterCenter(arr):
    if not len(arr) is 0:
        centroid = findCentroid(arr)

        cluster_center = findClosest(arr, centroid)

        return cluster_center

    else:
        return None



def findClusters(k, s, a, c):
    distances = []

    for i in range(len(s)):
        for j in range(k):
            distances.append(distance(s[i], c[j]))

        lowest = 0
        for j in range(k):
            if distances[j] < distances[lowest]:
                lowest = j

        a[lowest].append(s[i])
        distances = []

    return a

def kMeansRun(k, s, *args):
    a = [[] for i in range(k)]
    c = list(args)
    change = True
    cluster_times = 1

    print('Original cneters:', c)
    print()

    a = findClusters(k, s, a, c)

    count = 0
    print('Initial clusters:')
    for i in a:
        print('\tCluster', count, i)
        count += 1

    while change:
        count = 0

        for j in range(k):
            cluster_center = findClusterCenter(a[j])
            if cluster_center:
                c[j] = cluster_center

        print('\n\tCenter points after recalculating centers:', c, '\n')

        a2 = [[] for i in range(k)]
        a2 = findClusters(k, s, a2, c)

        if a != a2:
            cluster_times += 1
            a = a2

            print('Round', cluster_times, ':')
            for i in a2:
                print('\tCluster', count, i)
                count += 1
        else:
            print('\nFinal clusters found in {cluster_times} rounds'.format(cluster_times=cluster_times))            
            change = False

    print()
    return a2
