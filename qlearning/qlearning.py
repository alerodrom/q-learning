import os
import time
from operator import itemgetter

import numpy as np
from pandas import DataFrame

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

        # Número de épocas
        self.epochs = epochs
        # Tasa de recompensa a corto plazo
        self.gamma = gamma
        # Tasa de aprendizaje
        self.alpha = alpha
        # Tasa de aleatoriedad
        self.epsilon = 0.1
        self.max_epsilon = 1.0
        self.min_epsilon = 0.01

        self.epochs_data = dict()

        self.print_steps = print_steps
        self.print_max_reward = print_max_reward

        self.base_map = base_map

        self.env = env = Environment(
            pos_init=pos_init, pos_end=pos_end, base_map=base_map
        )

        # qtable: continene los valores para cada pareja de estado y acción
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
            if not "X" in self.base_map[aux[0]][aux[1]]:
                # Añade por donde esta pasando el algoritmo
                new_map[aux[0]][aux[1]] = "X | {}".format(self.base_map[aux[0]][aux[1]])
            if cont == 0:
                # Añade la posición de inicio y fin al mapa
                new_map[self.env.pos_init[0]][self.env.pos_init[1]] = "I | {}".format(
                    self.base_map[self.env.pos_init[0]][self.env.pos_init[1]]
                )
                new_map[self.env.pos_end[0]][self.env.pos_end[1]] = "F | {}".format(
                    self.base_map[self.env.pos_end[0]][self.env.pos_end[1]]
                )
            # Almacena los mapas generados para cada paso
            maps.append(DataFrame(new_map).to_html())
            cont += 1
        return maps

    def call(self):
        # Entrenamiento
        for i in range(self.epochs):
            # Iniciamos el problema
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

                # Contamos los pasos
                steps += 1

                # Actualizamos aleatoriamente las acciones, si no cogemos la acción máxima de qtable
                if np.random.uniform() < self.epsilon:
                    action = self.env.random_action()
                else:
                    action = np.argmax(self.qtable[state])

                # Proxima acción
                next_state, reward, done, step = self.env.step(action)

                # Actualizamos el valor de qtable con la ecuación de Bellman
                next_max = np.max(self.qtable[next_state])

                self.qtable[state, action] = self.qtable[state, action] + self.alpha * (
                    reward + self.gamma * next_max - self.qtable[state, action]
                )
                # Acumulamos la recompensa
                reward_count += reward
                # Actualizamos el estado
                state = next_state
                # Añadimos el paso que se ha dado a path
                path.append(step)
            # Mientras más se aprende menos acciones aleatorias vamos a ir tomando
            self.epsilon = self.min_epsilon + (
                self.max_epsilon - self.min_epsilon
            ) * np.exp(-0.1 * self.epsilon)
            # Añadimos al diccioario general los pasos, recomensa y camino seguidos en esta época
            self.epochs_data[i] = {"steps": steps, "reward": reward_count, "path": path}

        # Nos quedamos con la época que mayor recompensa tenga
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
