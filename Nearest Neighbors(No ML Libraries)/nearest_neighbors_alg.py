def distance(iris1, iris2):
    return (((iris1.sepal_length - iris2.sepal_length) ** 2) +
            ((iris1.sepal_width - iris2.sepal_width) ** 2) +
            ((iris1.pedal_length - iris2.pedal_length) ** 2) +
            ((iris1.pedal_width - iris2.pedal_width) ** 2)) ** .5


def createDistanceMatrix(iris_data, iris_to_predict):
    distance_matrix = []

    for iris in iris_data:
        distance_matrix.append([distance(iris, iris_to_predict), iris.classification])

    return distance_matrix


def findKClosest(k, distance_matrix):
    closest = []

    distance_matrix = sorted(distance_matrix, key=lambda x: x[0])

    for i in range(k):
        closest.append(distance_matrix[i])

    closest_counters = [0 for i in range(3)]

    print()
    print('\t', k, 'closest irises:')
    for i in range(k):
        if closest[i][1] is 0:
            closest_counters[0] += 1
            print('\t\tIris-setosa')
        elif closest[i][1] is 1:
            closest_counters[1] += 1
            print('\t\tIris-versicolor')
        elif closest[i][1] is 2:
            closest_counters[2] += 1
            print('\t\tIris-virginica')

    largest = 0
    for i in range(3):
        if closest_counters[largest] < closest_counters[i]:
            largest = i

    if largest is 0:
        print()
        print('\tThis iris is an Iris-setosa.')
    elif largest is 1:
        print()
        print('\tThis iris is an Iris-versicolor.')
    elif largest is 2:
        print()
        print('\tThis iris is an Iris-virginica.')


def runNN(k, iris_data, iris_to_predict):
    distance_matrix = createDistanceMatrix(iris_data, iris_to_predict)
    findKClosest(k, distance_matrix)

    print()
