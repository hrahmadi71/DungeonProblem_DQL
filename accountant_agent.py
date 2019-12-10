from enums import *
from dungeon_simulator import Actions
import random

class Accountant:
    def __init__(self):
        # Spreadsheet (Q-table) for rewards accounting
        self.q_table = [[0,0,0,0,0], [0,0,0,0,0]]

    def get_next_action(self, state):
        # Is FORWARD reward is bigger?
        if self.q_table[Actions.FORWARD][state] > self.q_table[Actions.BACKWARD][state]:
            return Actions.FORWARD

        # Is BACKWARD reward is bigger?
        elif self.q_table[Actions.BACKWARD][state] > self.q_table[Actions.FORWARD][state]:
            return Actions.BACKWARD

        # Rewards are equal, take random action
        return Actions.FORWARD if random.random() < 0.5 else Actions.BACKWARD

    def update(self, old_state, new_state, action, reward):
        self.q_table[action][old_state] += reward