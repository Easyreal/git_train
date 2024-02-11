from .models import Car, Driver



if __name__ == '__main__':
    car_bmw = Car(mark='bmw', model='cx100')
    driver_bmw = Driver(transport=car_bmw)

    for num in range(10):
        driver_bmw.drive()
        print("Расстояние:", driver_bmw.transport.get_distance())