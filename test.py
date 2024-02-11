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


car_bmw = Car(mark='bmw', model='cx100')
driver_bmw = Driver(transport=car_bmw)

for num in range(10):
    driver_bmw.drive()
    print("Расстояние:", driver_bmw.transport.get_distance())