import random


class Mercedes:
    pass


class Audi:
    pass


class Ford:
    pass


class Cadillac:
    pass


class CarFactory:
    def get_new_car(self, country):
        if country == 'Germany':
            return random.choice(Mercedes(), Audi())

        elif country == 'USA':
            return random.choice(Cadillac(),Ford())

car_factory = CarFactory()
german_car = car_factory.get_new_car('Germany')
american_car = car_factory.get_new_car('USA')
