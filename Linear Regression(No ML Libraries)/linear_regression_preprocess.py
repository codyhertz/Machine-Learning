def normalizeDataLR(car_data):
    min_mpg = car_data[0].mpg
    max_mpg = car_data[0].mpg
    min_cylinders = car_data[0].cylinders
    max_cylinders = car_data[0].cylinders
    min_dis = car_data[0].displacement
    max_dis = car_data[0].displacement
    min_hor = car_data[0].horsepower
    max_hor = car_data[0].horsepower
    min_weight = car_data[0].weight
    max_weight = car_data[0].weight
    min_acc = car_data[0].acceleration
    max_acc = car_data[0].acceleration

    for car in car_data:
        if min_mpg > car.mpg:
            min_mpg = car.mpg
        elif max_mpg < car.mpg:
            max_mpg = car.mpg

        if min_cylinders > car.cylinders:
            min_cylinders = car.cylinders
        elif max_cylinders < car.cylinders:
            max_cylinders = car.cylinders

        if min_dis > car.displacement:
            min_dis = car.displacement
        elif max_dis < car.displacement:
            max_dis = car.displacement

        if min_hor > car.horsepower:
            min_hor = car.horsepower
        elif max_hor < car.horsepower:
            max_hor = car.horsepower

        if min_weight > car.weight:
            min_weight = car.weight
        elif max_weight < car.weight:
            max_weight = car.weight

        if min_acc > car.acceleration:
            min_acc = car.acceleration
        elif max_acc < car.acceleration:
            max_acc = car.acceleration

    for car in car_data:
        car.mpg = (car.mpg - min_mpg) / (max_mpg - min_mpg)
        car.cylinders = (car.cylinders - min_cylinders) / (max_cylinders - min_cylinders)
        car.displacement = (car.displacement - min_dis) / (max_dis - min_dis)
        car.horsepower = (car.horsepower - min_hor) / (max_hor - min_hor)
        car.weight = (car.weight - min_weight) / (max_weight - min_weight)
        car.acceleration = (car.acceleration - min_acc) / (max_acc - min_acc)

    max = [max_mpg, max_cylinders, max_dis, max_hor, max_weight, max_acc]
    min = [min_mpg, min_cylinders, min_dis, min_hor, min_weight, min_acc]

    return car_data, max, min
