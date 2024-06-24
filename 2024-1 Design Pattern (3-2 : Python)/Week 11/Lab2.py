from typing import List

class Command:
    def execute(self):
        pass

class Dog:
    def sit(self):
        print("The dog sat down")
    def stay(self):
        print("The dog is staying")

class DogCommand(Command):
    def __init__(self, dog: Dog, commands: List[str]):
        self.dog = dog
        self.commands = commands

    def execute(self):
        for command in self.commands:
            if command == 'sit':
                self.dog.sit()
            elif command == 'stay':
                self.dog.stay()

class Invoker:
    def __init__(self):
        self.command_list = []

    def addCommand(self, command: Command):
        self.command_list.append(command)

    def runCommands(self):
        for command in self.command_list:
            command.execute()

baduk = Dog()
dog_command = DogCommand(baduk, ['stay', 'sit','sit'])
dog_command.execute()

invoker = Invoker()
invoker.addCommand(dog_command)
# invoker.addCommand(first_command)
# invoker.addCommand(second_command)
invoker.runCommands()
