from nearest_neighbors_preprocess import normalizeData
from nearest_neighbors_alg import runNN
from Iris import Iris


testing_data = [Iris(4.9, 3.0, 1.4, .2, ''),
                Iris(4.9, 2.4, 3.3, 1.0, ''),
                Iris(4.9, 2.5, 4.5, 1.7, '')
                ]

iris_data = []
max = []
min = []
iris_file = open("iris.txt", "r")

for line in iris_file:
    split_line = line.split(',')
    iris = Iris(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4])
    iris_data.append(iris)

iris_data, max, min = normalizeData(iris_data)

for i in range(3):
    testing_data[i].sepal_length = (testing_data[i].sepal_length - min[0]) / (max[0] - min[0])
    testing_data[i].sepal_width = (testing_data[i].sepal_width - min[1]) / (max[1] - min[1])
    testing_data[i].pedal_length = (testing_data[i].pedal_length - min[2]) / (max[2] - min[2])
    testing_data[i].pedal_width = (testing_data[i].pedal_width - min[3]) / (max[3] - min[3])

print('Nearest neighbors for k value of 3 with testing example 1:')

runNN(3, iris_data, testing_data[0])

print('Nearest neighbors for k value of 3 with testing example 2:')

runNN(3, iris_data, testing_data[1])

print('Nearest neighbors for k value of 3 with testing example 3:')

runNN(3, iris_data, testing_data[2])

print('Nearest neighbors for k value of 5 with testing example 1:')

runNN(5, iris_data, testing_data[0])

print('Nearest neighbors for k value of 5 with testing example 2:')

runNN(5, iris_data, testing_data[1])

print('Nearest neighbors for k value of 5 with testing example 3:')

runNN(5, iris_data, testing_data[2])
