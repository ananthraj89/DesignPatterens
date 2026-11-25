"""New coding concepts: Use try, except and optional finally keywords to manage error handling.
try:
    print(my_var)
except:
    print("An unknown error occurred")
finally:
    print("This is an optional and will get called even if there is no error")
"""
"""
Abstract Factory Design Pattern: This Design pattern adds an abstraction layer to an over multiple other creational 
patterns. To begin with a factory that can return factories also you will find examples being used to return builder,
prototypes, singleton, or other DP.
"""
from abc import ABCMeta, abstractmethod


class IChair(metaclass = ABCMeta):
    "The chair interface (product)"

    @staticmethod
    @abstractmethod

    def get_dimensions():
        "A static interface method"
        pass

#small_chair
class SmallChair(IChair):
    "A small chair concrete class implements IChair interface"
    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        return {
            "width" : self._width, 
            "height" : self._height,
            "depth" : self._depth

        }
#medium_chair
class MediumChair(IChair):
    "A medium chair concrete class implements I chair interface"
    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        return{
            "height": self._height,
            "width": self._width,
            "depth": self._depth
        }
#big_chair
class BigChair(IChair):
    "A Big chair concrete class implements IChair interface"
    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimensions(self):
        return{
            "height": self._height,
            "width": self._width,
            "depth": self._depth
        }
#chairfactory
class ChairFactory:
    "A Factory class"
    @staticmethod
    def get_chair(chair):
        "A ststic method to get a chair"
        try:
            if chair == 'BigChair':
                return BigChair()
            if chair == 'MediumChair':
                return MediumChair()
            if chair == 'SmallChair':
                return SmallChair()
            raise Exception('Chair Not found')
        except Exception as _e:
            print(_e)
        return None

#Table Interface class
class ITable(metaclass = ABCMeta):
    "The table interface (product)"
    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface methhod"
        pass

#smalltable 
class SmallTable(ITable):
    "A small table concrete class that implements the ITable interface"
    def __init__(self):
        self._height = 40
        self._width = 100
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "height": self._height,
            "depth": self._depth
        }
#mediumtable
class MediumTable(ITable):
    "A medium table concrete class"
    def __init__(self):
        self._height = 55
        self._width = 120
        self._depth = 70

    def get_dimensions(self):
        return {
            "height" : self._height,
            "width": self._width,
            "depth" : self._depth 
        }
    
#largetable
class LargeTable(ITable):
    "A LargeTable concrete class"
    def __init__(self):
        self._height= 70
        self._width = 150
        self._depth = 90

    def get_dimensions(self):
        return {
            "height": self._height,
            "width": self._width,
            "depth" : self._depth
        }
#Tablefactory
class TableFactory:
    "The Factory class"

    @staticmethod
    def get_table(table):
        "A static method to get a table"
        try:
            if table == 'LargeTable':
                return LargeTable()
            if table == 'MediumTable':
                return MediumTable()
            if table == 'SmallTable':
                return SmallTable()
            raise Exception ('Table not found')
        except Exception as _e:
            print(_e)
        return None

#Interface Furtinute factory  
class IFurnitureFactory(metaclass = ABCMeta):
    "An abstract Factory interface"

    @staticmethod
    @abstractmethod
    def get_furniture(furniture):
        "A static abstract factory interface method"
        pass


#Furniture Factory Abstract Factory design (Multiple factories)
class FurnitureFactory(IFurnitureFactory):
    "The Abstract Factory concrete class"
    @staticmethod
    def get_furniture(furniture):
        "Static get furniture method"
        try: 
            if furniture in ['SmallChair', 'MediumChair', 'BigChair']:
                return ChairFactory().get_chair(furniture)
            if furniture in ['SmallTable', 'MediumTable', 'LargeTable']:
                return TableFactory().get_table(furniture)
            raise Exception ('No factory found')
        except Exception as _e:
            print(_e)
        return None
    

#THE CLIENT
FURNITURE = FurnitureFactory().get_furniture('SmallChair')
print(f"{FURNITURE.__class__}: {FURNITURE.get_dimensions()}")

FURNITURE = FurnitureFactory().get_furniture('MediumTable')
print(f"{FURNITURE.__class__}: {FURNITURE.get_dimensions()}")