from copy import deepcopy

def hypothesis(thetas, car):
    return (thetas[0] + (car.cylinders * thetas[1]) +
        (car.displacement * thetas[2]) +
        (car.horsepower * thetas[3]) +
        (car.weight * thetas[4]) +
        (car.acceleration * thetas[5]))


def gradientDescent(car_data):
    thetas = [0, 0, 0, 0, 0, 0]
    error = car_data[0].mpg - hypothesis(thetas, car_data[0])
    learning_rate = .00015

    print('Creating linear function with 3000 iterations of gradient descent and a learning rate of .00015...\n')

    for i in range(3000):
        new_thetas = [0, 0, 0, 0, 0, 0]

        total = 0
        for m in range(len(car_data)):
            total += ((hypothesis(thetas, car_data[m]) - car_data[m].mpg) * 1)

        total *= learning_rate
        total = thetas[0] - total
        new_thetas[0] = total

        total = 0
        for m in range(len(car_data)):
            total += ((hypothesis(thetas, car_data[m]) - car_data[m].mpg) * car_data[m].cylinders)

        total *= learning_rate
        total = thetas[1] - total
        new_thetas[1] = total

        total = 0
        for m in range(len(car_data)):
            total += ((hypothesis(thetas, car_data[m]) - car_data[m].mpg) * car_data[m].displacement)

        total *= learning_rate
        total = thetas[2] - total
        new_thetas[2] = total

        total = 0
        for m in range(len(car_data)):
            total += ((hypothesis(thetas, car_data[m]) - car_data[m].mpg) * car_data[m].horsepower)

        total *= learning_rate
        total = thetas[3] - total
        new_thetas[3] = total

        total = 0
        for m in range(len(car_data)):
            total += ((hypothesis(thetas, car_data[m]) - car_data[m].mpg) * car_data[m].weight)

        total *= learning_rate
        total = thetas[4] - total
        new_thetas[4] = total

        total = 0
        for m in range(len(car_data)):
            total += ((hypothesis(thetas, car_data[m]) - car_data[m].mpg) * car_data[m].acceleration)

        total *= learning_rate
        total = thetas[5] - total
        new_thetas[5] = total

        thetas = deepcopy(new_thetas)

    return thetas
