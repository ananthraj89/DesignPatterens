''''

A prototype design pattern is good for creating new objects requires more resources than you want to use or have available.
you can save resources just by creating a copy of any existing object that is already in memory:

Eg: A file you've downloaded  from a server may be large, but since it is already in memory, you
could just clone it, and work on the new copy independently of the original

how to clone is entirely up to you , you need to decide to do shallow copy or deep copy
# A shallow copy, copies and creates a new reference one level deep
# A deep copy, copies and creates a new reference at all the levels.

PROTOTYPE INTERFACE: The interface tht describes the clone() method
PROTOTYPE: The obj/Product that implements the Prototype interface
CLIENT: The Client application that uses and creates the Proto Type


when using the shallow technique changing the inner item of OBJ2's list also effected
ObJ1's list

when using level-2 shallow technique the inner item of corresponding obj does not effected

This technique has dis advantages of that it wont deep copy lists in lists, dic in dic , tuples in tuples
or any othet combinations etc
'''

from abc import ABCMeta, abstractmethod

class IProtoType(metaclass=ABCMeta):
    'Interface with clone method'
    @staticmethod
    @abstractmethod
    def clone():
        'This clone can be deep or shallow it is up to you entirely'
        pass

#step2
class MyClass(IProtoType):
    'A concrete class'
    def __init__(self,field):
        self.field = field # any value of any type

    def clone(self):
        'This is while using shallow copy technique'
        return type (self)(
            #self.field   #shallow copy is returned
            self.field.copy()  #This is also a shallow copy with 2 levels deep lists of lists
        )
    def __str__(self):
        return (f"{id(self)}\tfield ={self.field}\ttype = {type(self.field)}")

#step3 THE CLIENT
OBJECT1 = MyClass([1,2,3,4])
print(f"OBJECT1 {OBJECT1}")

OBJECT2 = OBJECT1.clone() #CLONE
OBJECT2.field[1] = 101    #modifying elements in the list after cloning using level 1 shallow

#comparing the output
print(f"OBJECT2 {OBJECT2}")
print(f"OBJECT1 {OBJECT1}")

