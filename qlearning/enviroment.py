import time

import numpy as np
from pandas import DataFrame

# Move
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

# Outside
PLAIN = 1
FOREST = 2
MOUNTAIN = 4
WATER = 0

# REWARDS
R_PLAIN = -20
R_FOREST = -25
R_MOUNTAIN = -75
R_WATER = -500

MAPS = {
    "6x10": [
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 2, 2, 2, 0, 0, 1],
        [1, 1, 1, 2, 2, 4, 2, 2, 1, 1],
        [1, 1, 1, 2, 4, 4, 4, 2, 1, 1],
        [1, 1, 1, 2, 2, 4, 0, 0, 0, 0],
        [1, 1, 1, 1, 2, 2, 0, 0, 0, 0],
    ]
}


class Environment:
    def __init__(self, pos_init=None, pos_end=None):
        # comprobar que pos_init y pos_end sean tuplas y este dentro de los límites.

        scene = MAPS["6x10"]
        self.scene = scene = np.array(scene, dtype="int")
        self.height, self.width = n_row, n_col = scene.shape

        self.pos_init = pos_init if pos_init else (self.height - 1, 0)
        self.pos_end = pos_end if pos_end else (0, self.width - 1)

        self.pos_x, self.pos_y = self.pos_init
        self.pos_end_x, self.pos_end_y = self.pos_end

        self.actions = [i for i in range(4)]
        self.state_count = self.height * self.width
        self.action_count = len(self.actions)

    def reset(self):
        self.done = False
        self.pos_x, self.pos_y = self.pos_init
        return 0, 0, self.done

    # take action
    def step(self, action):
        if action == LEFT:
            self.pos_y = self.pos_y - 1 if self.pos_y > 0 else self.pos_y
        if action == RIGHT:
            self.pos_y = self.pos_y + 1 if self.pos_y < self.width - 1 else self.pos_y
        if action == DOWN:
            self.pos_x = self.pos_x + 1 if self.pos_x < self.height - 1 else self.pos_x
        if action == UP:
            self.pos_x = self.pos_x - 1 if self.pos_x > 0 else self.pos_x

        done = self.pos_x == self.pos_end_x and self.pos_y == self.pos_end_y
        # mapping (x,y) position to number between 0 and 5x5-1=24
        next_state = self.height * self.pos_x + self.pos_y

        outside = self.scene[self.pos_x][self.pos_y]
        if done:
            reward = 1000
        else:
            if outside == PLAIN:
                reward = R_PLAIN
            if outside == FOREST:
                reward = R_FOREST
            if outside == MOUNTAIN:
                reward = R_MOUNTAIN
            if outside == WATER:
                reward = R_WATER
        step = [(self.pos_x, self.pos_y), action]
        return next_state, reward, done, step

    # return a random action
    def random_action(self):
        return np.random.choice(self.actions)

    # display environment
    def render(self):
        new_map = MAPS["6x10"]
        new_map[self.pos_x][self.pos_y] = "X"
        print(DataFrame(new_map))
        print()
        # time.sleep(0.8)


print("")
