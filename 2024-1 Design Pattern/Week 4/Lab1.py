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
        clone.id = uuid.uuid4() # 고유한 id 부여
        return clone
    
    def __str__(self):
        return f"Character(ID={self.id}, Name={self.name}, Skill={self.skill})"

class CharacterBuilder:
    def __init__(self, character_instance):
        self.character = character_instance
    
    def set_name(self, name):
        self.character.name = name
        return self

    def set_physical(self, physical):
        self.character.physical = physical
        return self
    
    def set_defence(self, defence):
        self.character.defence = defence
        return self
    
    def set_skill(self, skill):
        self.character.skill = skill
        return self
    
    def build(self):
        return self.character

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

# 캐릭터 생성 예시
wizard_instance = Wizard()  # Wizard 인스턴스 생성
builder = CharacterBuilder(wizard_instance)
character = builder.set_name("Renata Glasc").set_skill("Hostile Takeover").build()
print(character)

# 캐릭터 복제 예시
clone_character = character.clone()
print(clone_character)