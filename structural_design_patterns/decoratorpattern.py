'''
A Decorator pattern is the structural design pattern that allows you to attatch additional
responsibilities to the object at the run time.
It can used in both oject oriented as well as functional paradigms.
decorator pattern != Python decorators

best example is pizza toppings in the base pizza class, coffe maker design, car , electronics etc

COMPONENT INTERFACE: That interfaces the objects
COMPONENT: The object that may be decorated
DECORATOR: The class that applies extra responsibilites to the component being decorated
           also implements same components interface
'''


from abc import  abstractmethod,ABCMeta

class IComponent(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def method():
        'A method to implement'
        pass

class Component():
    'A component that can be decorated or not'
    def method(self): # An example method
        return "component method"

class Decorator(IComponent):
    'The decorator also implements I component'
    def __init__(self,obj):
        self.object = obj
    def method(self):
        'A method to implement'
        return f"Decorator Method ({self.object.method()})"

#The Client
COMPONENT = Component()
print(COMPONENT.method())
print(Decorator(COMPONENT).method())