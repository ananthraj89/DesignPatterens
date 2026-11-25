"""
A Factory pattern is used for an extra abstraction. it is one of the easiest pattern to implement. adding an extra 
abstraction will also allow you to dynamically choose classes to instantiate based on some kind of logic.
"""

"""New coding concepts: ABCMetaClasses are a developmental tool that will help you to write classes that conform to a
specified interface that you've designed.

ABC refers to Abstract Base Class, The benefits of using ABCMeta classes to createabstract classes is that Your IDE
and pylint will indicate you at the development time whether your inheriting classes conform to class definition that
you,ve asked them to do. 

Abstract class interfaces are not instantiated directly in your code or scripts, but insted implemented in sub classes
that will provide the implementation code for the abstract methods.  """



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
    
#The Factory Class
class ChairFactory:
    "The Factory class"
    @staticmethod
    def get_chair(chair):
        "A ststic method to get a chair"
        if chair == 'BigChair':
            return BigChair()
        if chair == 'MediumChair':
            return MediumChair()
        if chair == 'SmallChair':
            return SmallChair()
        return None
    
#The Client
CHAIR = ChairFactory().get_chair("MediumChair")
print(CHAIR.get_dimensions())
