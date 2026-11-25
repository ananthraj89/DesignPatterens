"""
This is themiddle men between the main class or database to the client so that we cannot
loose the data, it has big lengthy code but it is easy
"""
from abc import ABCMeta, abstractmethod

@abstractmethod
class IPerson(metaclass=ABCMeta):
    def person_method(self):
        pass
    'Implemented in the child class'

class Person(IPerson):
    def person_method(self):
        print(f"I am a Ananth whose age is 34, i love my life!!")

class ProxyPerson(IPerson):
    def __init__(self):
        print(f"I am proxy of the following:")
        self.person = Person()
        self.person.person_method()

P1 = Person()
P1.person_method()

P2 = ProxyPerson()
P2.person_method()



#2nd program from book
class ISubject(metaclass=ABCMeta):

    @staticmethod
    def request():
        "A method to implement"

class RealSubject(ISubject):
    def __init__(self):
        self.enormous_data = [1,2,3]
    def request(self):
        return self.enormous_data

class Proxy(ISubject):
    def __init__(self):
        self.enormous_data = []
        self.real_subject = RealSubject()
    def request(self):
        if self.enormous_data == []:
            print(f"Pulling data from RealSubject")
            self.enormous_data = self.real_subject.request()
            return self.enormous_data
        print(f"Pulling data from Proxy Cache")
        return self.enormous_data
SUBJECT = Proxy()
print(id(SUBJECT))
print(SUBJECT.request())

print(SUBJECT.request()) #showing data again , but this time it retrives from local cache