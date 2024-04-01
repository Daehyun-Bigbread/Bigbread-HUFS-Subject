import copy
import uuid

class Character:
    def __init__(self):
        self.id = uuid.uuid4()  # 고유한 id 부여
        self.name = None
        self.physical = 'Medium'
        self.defence = 'Medium'
        self.mana = 'Medium'
        self.magic_attack = 'Medium'
        self.agility = 'Medium'
        self.range = 'Medium'
        self.skill = None

    def clone(self):
        clone = copy.deepcopy(self)
        clone.id = uuid.uuid4()  # 새로운 고유한 id 부여
        return clone

    def customize(self, name=None, skill=None):
        if name is not None:
            self.name = name
        if skill is not None:
            self.skill = skill
    
    def __str__(self):
        return f"Character(ID={self.id}, Name={self.name}, Physical={self.physical}, Defence={self.defence}, Mana={self.mana}, MagicAttack={self.magic_attack}, Agility={self.agility}, Range={self.range}, Skill={self.skill})"

class Warrior(Character):
    def __init__(self):
        super().__init__()
        self.pysical = 'High'
        self.defence = 'High'
        self.skill = 'Sword Swing'

class Wizard(Character):
    def __init__(self):
        super().__init__()
        self.physical = 'Medium'
        self.defence = 'Medium'
        self.mana = 'High'
        self.magic_attack = 'High'
        self.skill = 'Fireball'

class Archer(Character):
    def __init__(self):
        super().__init__()
        self.physical = 'Medium'
        self.defence = 'Medium'
        self.agility = 'High'
        self.range = 'High'
        self.skill = 'Precision Shooting'

# 직업별 프로토타입 생성
warrior_prototype = Warrior()
wizard_prototype = Wizard()
archer_prototype = Archer()

# warrior 2개 생성
warrior1 = warrior_prototype.clone()
warrior1.customize(name="Garen")
print(warrior1)

warrior2 = warrior_prototype.clone()
warrior2.customize(name="Riven", skill="Wind Slash")
print(warrior2)

# wizard 2개 생성
wizard1 = wizard_prototype.clone()
wizard1.customize(name="Syndra", skill="Unleashed Power")
print(wizard1)

wizard2 = wizard_prototype.clone()
wizard2.customize(name="Azir", skill="Emperor's Divide")
print(wizard2)

# archer 2개 생성
archer1 = archer_prototype.clone()
archer1.customize(name="Ashe")
print(archer1)

archer2 = archer_prototype.clone()
archer2.customize(name="Senna", skill="Dawning Shadow")
print(archer2)
