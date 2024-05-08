from abc import ABCMeta, abstractmethod

# Move
class Move(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass

class Walk(Move):
    def move(self):
        print("걷다")

class Run(Move):
    def move(self):
        print("뛰다")

# Attack
class Attack(metaclass=ABCMeta):
    @abstractmethod
    def attack(self):
        pass

class Gun(Attack):
    def attack(self):
        print("총을 쏘다")

class Rocket(Attack):
    def attack(self):
        print("로켓을 발사하다")

# Move Strategy
class TakeMoveStrategy:
    def __init__(self, move: Move):
        self.move = move
    
    def setMove(self, move: Move):
        self.move = move

    def performMove(self):
        self.move.move()

# Attack Strategy
class TakeAttackStrategy:
    def __init__(self, attack: Attack):
        self.attack = attack

    def setAttack(self, attack: Attack):
        self.attack = attack

    def performAttack(self):
        self.attack.attack()

# Robot
class Robot:
    def __init__(self, moveStrategy: TakeMoveStrategy, attackStrategy: TakeAttackStrategy):
        self.moveStrategy = moveStrategy
        self.attackStrategy = attackStrategy
    
    def changeMoveStrategy(self, move: Move):
        self.moveStrategy.setMove(move)
    
    def changeAttackStrategy(self, attack: Attack):
        self.attackStrategy.setAttack(attack)
    
    def makeMove(self):
        self.moveStrategy.performMove()
    
    def makeAttack(self):
        self.attackStrategy.performAttack()

# Client Code
moveStrategy = TakeMoveStrategy(Walk())
attackStrategy = TakeAttackStrategy(Gun())
robot = Robot(moveStrategy, attackStrategy)

# 걷고 총을 쏨
robot.makeMove()
robot.makeAttack()

# 뛰기로 변경, 총에서 로켓으로 변경
robot.changeMoveStrategy(Run())
robot.changeAttackStrategy(Rocket())

# 뛰고 로켓 발사
robot.makeMove()
robot.makeAttack()
