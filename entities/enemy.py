from .character import Character
from .behavior.behavior import Behavior

class Enemy(Character):
    def __init__(self, life, attack, defense, strength, speed, reflexes, intelligence, loot = None, behavior = None):
        super().__init__(life, attack, defense, strength, speed, reflexes, intelligence)
        if isinstance(loot, str):
            self.loot = [loot]
        else:
            self.loot = loot or []
        self.behavior = behavior or Behavior(0.5, 0.5, 0.5)
    def drop_item(self):
        if self.life <= 0:
            return self.loot
