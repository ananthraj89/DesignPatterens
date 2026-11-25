'''
It is a behavioral pattern in which it follows the command instructions to exceute the pogram
examples: Smart switches ON/OFF
         GUI, Networking, parallel processing or threads

Terminology: Receiver: The object that will receive and exceute the command.
Invoker: The object that sends the command to the receiver eg: Button
Command object: Itself, an object that implements an execute or action method
Client: The application that is aware of the receiver, invoker, and all commands.
'''
from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def execute():
        'The execute method that all the command objects will use'
        pass
class Invoker:
    def __init__(self):
        self._commands = {}  #single underscore on your class is useful indicator to codevelopers saying this is private

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self,command_name):
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognized")

class Receiver:
    @staticmethod
    def run_command_1():
        'A set of instructions to run'
        print("Executing Command 1")
    @staticmethod
    def run_command_2():
        print("Executing Command 2")

class Command1(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver
    def execute(self):
        self._receiver.run_command_1()


class Command2(ICommand):
    def __init__(self, receiver):
        self._receiver = receiver
    def execute(self):
        self._receiver.run_command_2()


#THE CLIENT
#Create a receiver
RECEIVER = Receiver()

#Create Commands
COMMAND1 = Command1(RECEIVER)
COMMAND2 = Command2(RECEIVER)

#Regeister with Invoker
INVOKER = Invoker()
INVOKER.register("1", COMMAND1)
INVOKER.register("2",COMMAND2)

#execute the commands
INVOKER.execute("1")
INVOKER.execute("2")
INVOKER.execute("1")
INVOKER.execute("2")
