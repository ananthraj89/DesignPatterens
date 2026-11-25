'''
The facade pattern is the essentially a reduced or simplified interface to set of other interfaces
abstractions, and implementations with in the system that may be full of complexity
and/or lightly coupled.
    sometimes your system becomes quite complex overtime as more features are added or modified
it may be useful to provide simple API over it. This is called FACADE PATTERN

    Too many classes, for a business enterprise example, or any other can be simplified
in to a Facade or Facade-in-Facade to solve or design the system
'''

class SubsystemClassA:
    'A Hypothetically complicated class'
    @staticmethod
    def method():
        'A complicated method'
        return "A"
class SubSystemClassB:
    'complicated class'
    @staticmethod
    def method(value):
        'A complicated method'
        return value
class SubSystemClassC:
    'complicated class'
    @staticmethod
    def method(value):
        'A complicated method'
        return value

class Facade():
    'A simplified facade offering the services of the syb-systems'
    @staticmethod
    def sub_system_class_a():
        'use subsystems methods respectively'
        return SubsystemClassA.method()
    @staticmethod
    def sub_system_class_b():
        return SubSystemClassB.method(value= 'B')
    @staticmethod
    def sub_system_class_c():
        return SubSystemClassC.method(value= {'c': [100,200,300]})


#THE CLIENT

print(SubsystemClassA.method())
print(SubSystemClassB.method('B'))
print(SubSystemClassC.method({'C': [1,2,3,4]}))

print(Facade.sub_system_class_a())
print(Facade.sub_system_class_b())
print(Facade.sub_system_class_c())
