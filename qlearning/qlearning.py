from operator import itemgetter

# from medium_qlearning_env import Env
from enviroment import Environment, MAPS
from pandas import DataFrame
import numpy as np
import time
import os


class Qlearning:
    def __init__(
        self, epochs=5000, init_zeros=True, print_steps=False, print_max_reward=True
    ):
        # create environment
        self.env = env = Environment()

        # QTable : contains the Q-Values for every (state,action) pair
        if init_zeros:
            self.qtable = np.zeros([env.state_count, env.action_count])
        else:
            self.qtable = np.random.rand(env.state_count, env.action_count)

        # hyperparameters
        self.epochs = epochs

        self.gamma = 0.9
        self.alpha = 0.1  # learning rate

        self.epsilon = 0.1
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01
        self.decay_rate = 0.01

        self.epochs_data = dict()

        self.print_steps = print_steps
        self.print_max_reward = print_max_reward

    def _render(self, res):
        new_map = MAPS["6x10"]
        for step in res["path"]:
            aux = step[0]
            new_map[aux[0]][aux[1]] = "X"
            print(DataFrame(new_map))
            print()
        time.sleep(0.8)

    def call(self):
        # training loop
        for i in range(self.epochs):

            state, reward, done = self.env.reset()
            steps = 0
            reward_count = 0
            path = []
            while not done:
                if self.print_steps:
                    os.system('clear')
                    print("epoch #", i + 1, "/", self.epochs)
                    self.env.render()
                    time.sleep(0.5)
                    os.system('clear')
                # count steps to finish game
                steps += 1

                # act randomly sometimes to allow exploration
                if np.random.uniform() < self.epsilon:
                    action = self.env.random_action()
                # if not select max action in Qtable (act greedy)
                else:
                    action = np.argmax(self.qtable[state])

                # take action
                next_state, reward, done, step = self.env.step(action)

                # update qtable value with Bellman equation
                # qtable[state][action] = reward + gamma * max(qtable[next_state])
                next_max = np.max(self.qtable[next_state])

                self.qtable[state, action] = self.qtable[state, action] + self.alpha * (
                    reward + self.gamma * next_max - self.qtable[state, action]
                )
                reward_count += reward
                # update state
                state = next_state
                path.append(step)
            # The more we learn, the less we take random actions
            self.epsilon = self.min_epsilon + (
                self.max_epsilon - self.min_epsilon
            ) * np.exp(-0.1 * self.epsilon)
            self.epochs_data[i] = {"steps": steps, "reward": reward_count, "path": path}

        res = self.epochs_data[
            max(
                range(len(self.epochs_data)),
                key=lambda index: self.epochs_data[index]["reward"],
            )
        ]
        if self.print_max_reward:
            self._render(res)
        print(res)
