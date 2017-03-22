class Director:
    builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.paint_house()

    def get_house(self):
        return self.builder.house


class House:
    walls = None
    roof = None
    colour = None

class Builder:
    house = None

    def build_walls(self):
        pass

    def build_roof(self):
        pass

    def paint_house(self):
        pass

class WhiteHouseBuilder(Builder):
    house = House()

    def build_walls(self):
        self.house.walls = 'Walls are built'

    def build_roof(self):
        self.house.roof = 'Roof is built'

    def paint_house(self):
        self.house.colour = 'white'


class PinkHouseWithoutRoofBuilder(Builder):
    house = House()

    def build_walls(self):
        self.house.walls = 'walls are built'

    def build_roof(self):
        self.house.roof = 'Roof is not built'

    def paint_house(self):
        self.house.colour = 'Pink'


director = Director()
normal_builder = WhiteHouseBuilder()
director.set_builder(normal_builder)
director.construct_house()
white_house = director.get_house()
print('White house is painted in %s' % white_house.colour)
print(white_house.roof)
print(white_house.walls)

dumm_builder = PinkHouseWithoutRoofBuilder()
director.set_builder(dumm_builder)
director.construct_house()
white_house = director.get_house()
print('Dumm house is painted in %s' % white_house.colour)
print(white_house.roof)
print(white_house.walls)

