from .character import Character

class Player(Character):
    def __init__(self, name="Player", life=100, attack=1, defense=1, strength=10, speed=10, reflexes=10, intelligence=10, inventory=None):
        super().__init__(name=name, life=life, attack=attack, defense=defense, strength=strength, speed=speed, reflexes=reflexes, intelligence=intelligence)
        self.inventory = inventory or []
    def get_item(self, item):
        self.inventory.append(item)
    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            item.use(self)