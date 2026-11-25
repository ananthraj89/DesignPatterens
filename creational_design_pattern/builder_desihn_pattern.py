from abc import ABCMeta, abstractmethod


class IHouseBuilder(metaclass=ABCMeta):
    "The house builder interface"
    @staticmethod
    @abstractmethod
    def set_building_type(building_type):
        "Build type"

    @staticmethod
    @abstractmethod
    def set_wall_material(wall_material):
        "Wall material"

    @staticmethod
    @abstractmethod
    def set_number_doors(number):
        "Number of doors"

    @staticmethod
    @abstractmethod
    def set_number_windows(number):
        "Number of windows"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return final product"


class HouseBuilder(IHouseBuilder):
    "Concrete House Builder class"
    def __init__(self):
        self.house = House()

    def set_building_type(self, building_type):
        self.house.building_type = building_type
        return self

    def set_wall_material(self, wall_material):
        self.house.wall_material = wall_material
        return self

    def set_number_doors(self, number):
        self.house.doors = number
        return self

    def set_number_windows(self, number):
        self.house.windows = number
        return self

    def get_result(self):
        return self.house


class House:
    "The product or the concrete house class"
    def __init__(self, building_type="Apartment", doors=0,
                 windows=0, wall_material="Brick"):
        self.wall_material = wall_material
        self.building_type = building_type
        self.doors = doors
        self.windows = windows

    def __str__(self):
        return f"This is a {self.wall_material} {self.building_type} with {self.doors} doors and {self.windows} windows."


class HouseBoatDirector:
    "One of the directors that can build complex representation"
    @staticmethod
    def construct():
        "Constructs and returns a final product"
        return HouseBuilder()\
            .set_building_type("House Boat")\
            .set_wall_material("Wood")\
            .set_number_doors(6)\
            .set_number_windows(8)\
            .get_result()


class CastleDirector:
    "One of the directors which can build a complex representation."
    @staticmethod
    def construct():
        "Constructs and returns a final product"
        return HouseBuilder()\
            .set_building_type('Castle')\
            .set_wall_material('Sandstone')\
            .set_number_doors(100)\
            .set_number_windows(200)\
            .get_result()


class IglooDirector:
    "One of the directors which can build complex representation."
    @staticmethod
    def construct():
        "Constructs and returns a final product."
        return HouseBuilder()\
            .set_building_type('Igloo')\
            .set_wall_material('Ice')\
            .set_number_doors(1)\
            .set_number_windows(0)\
            .get_result()


# The Client
IGLOO = IglooDirector.construct()
CASTLE = CastleDirector.construct()
HOUSEBOAT = HouseBoatDirector.construct()

print(IGLOO)
print(CASTLE)
print(HOUSEBOAT)
