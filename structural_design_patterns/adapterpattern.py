'''
A Adapter design pattern will solve these problems

How to use incompatable classes can work togeather
How to reuse the classes that doesnot have interference with the client
How an alternate interference can be provided for the class?

TARGET: The class that needs to be adapted.
ADAPTER INTERFACE: The interface of the target that is the adapter will need to be implemented
ADAPTER: The concrete adapter class containing the adaption process.
CLIENT: The client application that uses the adapter

It is like a bridge or socket  between the incompatable classes to give the requried client result
'''

from abc import ABCMeta, abstractmethod

class IA(metaclass=ABCMeta):
    'An interface for an object'
    @staticmethod
    @abstractmethod
    def method_a():
        pass
class ClassA(IA):
    def method_a(self):
        print("method A")

class IB(metaclass=ABCMeta):
    'An Interface for the object'
    @staticmethod
    @abstractmethod
    def method_b():
        pass
class ClassB(IB):
    def method_b(self):
        print ("method B")

class ClassBAdapter(IA):  #Implements A Interface
    def __init__(self):
        self.class_b = ClassB()
    def method_a(self):   #defing method a in Class BAdapter
        self.class_b.method_b()

#before the adapter
#THe client
ITEMS = [ClassA(),ClassB()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()   #calling method a does nort print

#after the adapter

ITEMS = [ClassA(),ClassBAdapter() ]
for item in ITEMS:
    item.method_a()    # calling method a