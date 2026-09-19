import random

class Behavior:
    def __init__(self, aggressiveness, cowardice, intelligence):

        self.aggressiveness = aggressiveness
        self.cowardice = cowardice
        self.intelligence = intelligence

    def decide_actions(self, enemy, player):

        life_ratio = enemy.life / enemy.max_life

        intelligence_action_chance = self.intelligence * (1 - life_ratio)
        flee_chance = self.cowardice * (1 - life_ratio)
        attack_chance = self.aggressiveness * life_ratio

        possible_actions = ["attack", "flee", "heal"]
        action_weights = [attack_chance, flee_chance, intelligence_action_chance]

        return random.choices(possible_actions, weights=action_weights, k=1)[0]
    
