class Audi:
    speed = 200

class Volga:
    speed = 120


class AbstractCarFactory:
    funds = 0

    def __init__(self):
        raise NotImplementedError

    @classmethod
    def get_new_car(cls):
        """
        Gets new car depending on funds
        :return: new car instance
        """
        if cls.funds >= 100000:
            return Audi()

        else:
            return Volga()


class CheapCarFactory(AbstractCarFactory):
    funds = 2000


class LuxuryCarFactory(AbstractCarFactory):
    funds = 200000


cheap_car = CheapCarFactory.get_new_car()
luxury_car = LuxuryCarFactory.get_new_car()

if luxury_car.speed > cheap_car.speed:
    print('Done!')
