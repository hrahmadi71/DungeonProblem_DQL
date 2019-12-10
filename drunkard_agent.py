from enums import *
from dungeon_simulator import Actions
import random

class Drunkard:
    def __init__(self):
        self.q_table = None

    def get_next_action(self, state):
        # Random walk
        return Actions.FORWARD if random.random() < 0.5 else Actions.BACKWARD

    def update(self, old_state, new_state, action, reward):
        pass # I don't care! I'm drunk!!