class Iris():
    def __init__(self, sepal_length, sepal_width, pedal_length, pedal_width, classification):
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.pedal_length = float(pedal_length)
        self.pedal_width = float(pedal_width)

        if "Iris-virginica" in classification:
            self.classification = 2
        elif"Iris-versicolor" in classification:
            self.classification = 1
        elif "Iris-setosa" in classification:
            self.classification = 0
        else:
            self.classification = None

    def __repr__(self):
        return '%s' % self.classification
