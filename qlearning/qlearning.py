import os
import time
from operator import itemgetter

import numpy as np
from pandas import DataFrame

# from medium_qlearning_env import Env
from qlearning.enviroment import MAPS, Environment


class Qlearning:
    def __init__(
        self,
        epochs=5000,
        init_zeros=True,
        print_steps=False,
        print_max_reward=True,
        gamma=0.9,
        alpha=0.1,
        base_map=MAPS["6x10"],
        pos_init=None,
        pos_end=None,
    ):

        # hyperparameters
        # TODO tiene que ser mayor que 1
        self.epochs = epochs

        self.gamma = gamma
        self.alpha = alpha  # learning rate

        self.epsilon = 0.1
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01
        self.decay_rate = 0.01

        self.epochs_data = dict()

        self.print_steps = print_steps
        self.print_max_reward = print_max_reward

        self.base_map = base_map
        print(pos_init)
        print(pos_end)
        # create environment
        # TODO: pasar posición de inicio y fin
        self.env = env = Environment(
            pos_init=pos_init, pos_end=pos_end, base_map=base_map
        )

        # QTable : contains the Q-Values for every (state,action) pair
        if init_zeros:
            self.qtable = np.zeros([env.state_count, env.action_count])
        else:
            self.qtable = np.random.rand(env.state_count, env.action_count)

    def _render(self, res):
        maps = list()
        new_map = self.base_map
        cont = 0
        for step in res["path"]:
            aux = step[0]
            new_map[aux[0]][aux[1]] = "X | {}".format(self.base_map[aux[0]][aux[1]])
            if cont == 0:
                new_map[self.env.pos_init[0]][self.env.pos_init[1]] = "I | {}".format(
                    self.base_map[self.env.pos_init[0]][self.env.pos_init[1]]
                )
                new_map[self.env.pos_end[0]][self.env.pos_end[1]] = "F | {}".format(
                    self.base_map[self.env.pos_end[0]][self.env.pos_end[1]]
                )
            maps.append(DataFrame(new_map).to_html())
            cont += 1
        return maps

    def call(self):
        # training loop
        for i in range(self.epochs):

            state, reward, done = self.env.reset()
            steps = 0
            reward_count = 0
            path = []
            while not done:
                if self.print_steps:
                    os.system("clear")
                    print("epoch #", i + 1, "/", self.epochs)
                    self.env.render()
                    time.sleep(0.5)
                    os.system("clear")
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
        result = dict()
        if self.print_max_reward:
            result["maps"] = self._render(res)
        result["result"] = res
        return result
