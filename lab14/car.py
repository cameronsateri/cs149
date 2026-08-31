class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year
        self.speed = 0

    def __str__(self):
        str_car = "A {} {} that is going {:.1f} mph"
        return str_car.format(self.year, self.make, self.speed)

    def accelerate(self):
        self.speed += 5
        if self.speed > 150:
            self.speed = 150

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0


if __name__ == '__main__':
    car1 = Car("Ford", 1997)
    car2 = Car("Toyota", 2014)

    print(car1)
    print(car2)
