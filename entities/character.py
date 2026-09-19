import random

class Character:

    def __init__(self,name, life, attack, defense, strength, speed, reflexes, intelligence):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.strength = strength * 1.25
        self.speed = speed
        self.reflexes = reflexes
        self.intelligence = intelligence
        self.max_life = self.life

    def phisic_attack(self):
        final_attack = self.attack * self.strength
        return final_attack, self.speed
    
    def _damage(self, damage):
        if self.defense <= 0:
            self.life -= damage
        else:
            aux = damage - self.defense
            self.life -= aux

    def dodge(self, AttackSpeed,damage):
        min = self.reflexes * 0.40
        dodge_opportunity = random.randint(int(min), int(self.reflexes))
        if dodge_opportunity >= AttackSpeed:
            self._damage(0)
        else:
            self._damage(damage)
