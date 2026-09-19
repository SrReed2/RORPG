from .item import Item

class weapon(Item):
    def __init__(self, name, new_attack):
        super().__init__(name, "A sharp blade for combat.")
        self.name = name
        self.attack = new_attack  
    def equip(self, character):
        character.attack = self.attack
        print(f"{character.name} equipped a {self.name} and gained {self.attack} attack points.")