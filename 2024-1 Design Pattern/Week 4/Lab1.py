class Character:
    def __init__(self):
        self.pysical = None
        self.defence = None
        self.mana = None
        self.magic_attack = None
        self.agility = None
        self.range = None
        self.skill = None

    def clone(self):
        return copy.deepcopy(self)

class Warrior(Character):
    def __init__(self):
        super().__init__()
        self.ability = 'Physical Strength'
        self.skill = 'Sword Swing'

class Wizard(cjharacter):
    def __init__(self):
        super().__init__()
        self.ability = 'Mana, Magic Attack Power'
        self.skill = 'Fireball'

class Archer(Character):
    def __init__(self):
        super().__init__()
        self.ability = 'Agility, Accuracy'
        self.skill = 'Arrow Rain'