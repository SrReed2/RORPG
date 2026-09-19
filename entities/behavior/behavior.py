import random

class Behavior:
    def __init__(self, aggressiveness, cowardice, intelligence):
        self.aggressiveness = aggressiveness
        self.cowardice = cowardice
        self.intelligence = intelligence
    def decide_actions(self, enemy, player):
        pass