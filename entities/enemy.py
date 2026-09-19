from .character import Character

class Enemy(Character):
    def __init__(self, life, attack, defense, strength, speed, reflexes, intelligence, loot = None):
        super().__init__(life, attack, defense, strength, speed, reflexes, intelligence)
        if isinstance(loot, str):
            self.loot = [loot]
        else:
            self.loot = loot or []
    def drop_item(self):
        if self.life <= 0:
            return self.loot
