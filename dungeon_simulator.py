from enums import *
import random

class DungeonSimulator:
    def __init__(self, length=5, slip=0.1, small=2, large=10):
        self.length = length # Length of the dungeon
        self.slip = slip  # probability of 'slipping' an action
        self.small = small  # payout for BACKWARD action
        self.large = large  # payout at end of chain for FORWARD action
        self.state = 0  # Start at beginning of the dungeon

    def take_action(self, action):
        if random.random() < self.slip:
            # agent slipped, reverse action taken
            action = not action
        if action == Actions.BACKWARD:
            # BACKWARD: go back to the beginning, get small reward
            if self.state == 0:
                reward = -1
            else:
                reward = self.small
            self.state = 0
        elif action == Actions.FORWARD:
            # FORWARD: go up along the dungeon
            if self.state < self.length - 1:
                self.state += 1
                if self.state == self.length - 1:
                    reward = self.large
                else:
                    reward = 0
            else:
                reward = -1
        return self.state, reward

    def reset(self):
        # Reset state to zero, the beginning of the dungeon
        self.state = 0
        return self.state

class Actions:
    FORWARD = True
    BACKWARD = False