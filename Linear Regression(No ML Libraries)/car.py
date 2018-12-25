class Car():
    def __init__(self, mpg, cylinders, displacement, horsepower, weight, acceleration):
        if mpg is not '':
            self.mpg = float(mpg)
        else:
            self.mpg = None

        self.cylinders = int(cylinders)
        self.displacement = float(displacement)
        self.horsepower = float(horsepower)
        self.weight = float(weight)
        self.acceleration = float(acceleration)

    def __repr__(self):
        return '%s %s %s %s %s %s' % (self.mpg, self.cylinders, self.displacement, self.horsepower, self.weight, self.acceleration)
