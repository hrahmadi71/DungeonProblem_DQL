import random
import json
import argparse
import time
from drunkard_agent import Drunkard
from accountant_agent import Accountant
from gambler_agent import Gambler
from dungeon_simulator import DungeonSimulator
from dungeon_simulator import Actions
from deep_gambler import DeepGambler


def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', type=str, default='DEEP-GAMBLER', help='Which agent to use')
    parser.add_argument('--learning_rate', type=float, default=0.1, help='How quickly the algorithm tries to learn')
    parser.add_argument('--discount', type=float, default=0.95, help='Discount for estimated future action')
    parser.add_argument('--iterations', type=int, default=20000, help='Iteration count')
    FLAGS, unparsed = parser.parse_known_args()

    # select agent
    if FLAGS.agent == 'GAMBLER':
        agent = Gambler(learning_rate=FLAGS.learning_rate, discount=FLAGS.discount, iterations=FLAGS.iterations)
    elif FLAGS.agent == 'ACCOUNTANT':
        agent = Accountant()
    elif FLAGS.agent == 'DEEP-GAMBLER':
        agent = DeepGambler()
    else:
        agent = Drunkard()

    # setup simulation
    dungeon = DungeonSimulator()
    dungeon.reset()
    total_reward = 0  # Score keeping

    # main loop
    for step in range(FLAGS.iterations):
        old_state = dungeon.state  # Store current state
        action = agent.get_next_action(old_state)  # Query agent for the next action
        new_state, reward = dungeon.take_action(action)  # Take action, get new state and reward
        agent.update(old_state, new_state, action, reward)  # Let the agent update internals

        total_reward += reward  # Keep score
        if (step+1) % 50 == 0:  # Print out metadata every 100th iteration
            print(json.dumps({'step': step+1, 'total_reward': total_reward}))
            # if agent.q_table is not None:
            #     print('FORWARD: ', agent.q_table[Actions.FORWARD])
            #     print('BACKWARD: ', agent.q_table[Actions.BACKWARD])
            # print('Exploration rate: ', agent.exploration_rate)
            for i in range(5):
                print(agent.get_q(i))

        # time.sleep(0.0001)  # Avoid spamming stdout too fast!


if __name__ == "__main__":
    main()
