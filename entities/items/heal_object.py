from .item import Item

class heal_object(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name, f"Restores {heal_amount} health points.")
        self.heal_amount = heal_amount

    def use(self, character):
        character.life += self.heal_amount
        print(f"{character.name} used a {self.name} and restored {self.heal_amount} health points.")