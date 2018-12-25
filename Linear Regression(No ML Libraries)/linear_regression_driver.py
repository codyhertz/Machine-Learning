from car import Car
from linear_regression_preprocess import normalizeDataLR
from linear_regression_alg import gradientDescent, hypothesis
from copy import deepcopy

car_data = []
max = []
min = []
car_file = open("cars.txt", "r")

testing_data = [Car('', 4, 95, 92, 2043, 19.1),
                Car('', 6, 168, 96, 2981, 14.7),
                Car('', 4 ,98, 68, 2147, 18.3)
                ]

original_test = deepcopy(testing_data)

for line in car_file:
    line = line.replace('\n', '')
    split_line = line.split('\t')
    car = Car(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5])
    car_data.append(car)

car_data, max, min = normalizeDataLR(car_data)

for i in range(3):
    testing_data[i].cylinders = (testing_data[i].cylinders - min[1]) / (max[1] - min[1])
    testing_data[i].displacement = (testing_data[i].displacement - min[2]) / (max[2] - min[2])
    testing_data[i].horsepower = (testing_data[i].horsepower - min[3]) / (max[3] - min[3])
    testing_data[i].weight = (testing_data[i].weight - min[4]) / (max[4] - min[4])
    testing_data[i].acceleration = (testing_data[i].acceleration - min[5]) / (max[5] - min[5])

thetas = []

thetas = gradientDescent(car_data)

for i in range(3):
    print('Predicted mpg for vehicle(traing example {i}) with {cylinders} cylinders,\n\t {displacement} displacement,\n\t {horsepower} horsepower,\n\t {weight} weight,\n\t and {acceleration} acceleration: {prediction}\n'
        .format(cylinders=original_test[i].cylinders, displacement=original_test[i].displacement, horsepower=original_test[i].horsepower,
                weight=original_test[i].weight, acceleration=original_test[i].acceleration, i=i, prediction=hypothesis(thetas, testing_data[i]) * (max[0] - min[0]) + min[0]))
