class Driver():
    def __init__(self, transport):
        self.transport = transport

    def drive(self):
        return self.transport.ride()


class Car():

    distance = 0

    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

    def ride(self):
        self.distance += 10

    def get_distance(self):
        return self.distance

