'''The Chain of responsibility behavioral pattern is used to achieve loose coupling
in software design.
In this pattern the object is passed in to successor depending up on some kind of logic,
will or wont be passed on to the another successor and processed. There can be any number of
successors.


Terminology: Handler Interface: A common interface for handling and passing the objects through
each successor.
Concrete Handler: The class acting as the sucessor handling the requests and passing on to the next.
Client: The application or the class that initiates to call to the first concrete handler.

'''

import sys
from abc import ABCMeta, abstractmethod

class IDispenser(metaclass= ABCMeta):
    @staticmethod
    @abstractmethod
    def next_successor(successor):
        'set the next to handle the chain'
        pass

    @staticmethod
    @abstractmethod
    def handle(amount):
        'handle the event'
        pass

class Dispenser10(IDispenser):
    'Dispenses $10 Bills iff applicable, else contdd.. to next successor'
    def __init__(self):
        self.successor = None

    def next_successor(self, successor):
        'set the next successor'
        self.successor  = successor

    def handle(self, amount):
        'Handle the amount'
        if amount >= 10:
            num = amount // 10
            remainder = amount % 10
            print(f"Dispensing {num} $10 Bills or notes.")
            if remainder != 10:
                self.successor.handle(remainder)
        else:
            self.successor.handle(amount)

class Dispenser20(IDispenser):
    "Dispense $20 Bills if applicable, otherwise contd.. to next successor"
    def __init__(self):
        self.successor = None

    def next_successor(self, successor):
        self.successor = successor

    def handle(self,amount):
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f"Dispensing {num} $20 Bills or notes")
            if remainder != 0:
                self.successor.handle(remainder)
        else:
            self.successor.handle(amount)

class Dispenser50(IDispenser):
    "Dispense $50 if applicable, otherwise cotd.. to next succession"
    def __init__(self):
        self.successor = None

    def next_successor(self, successor):
        self.successor = successor

    def handle(self, amount):
        if amount >= 50:
            num = amount // 50
            remainder = amount % 50
            print(f"Dispense {num} $50 Bills or notes")
            if remainder != 0:
                self.successor.handle(remainder)
        else:
            self.successor.handle(amount)


#Chain of responsibility pattern
class ATMDispenserChain:
    'The Client Chain'

    def __init__(self):
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()

        self.chain1.next_successor(self.chain2)
        self.chain2.next_successor(self.chain3)

ATM = ATMDispenserChain()
Amount = int(input('Enter the value of the amount: '))
if Amount <  10 or Amount %10 != 0:
    print("Amount should be a positive and in multiple of 10's")
    sys.exit()

ATM.chain1.handle(Amount)
