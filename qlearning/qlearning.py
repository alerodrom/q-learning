from operator import itemgetter

# from medium_qlearning_env import Env
from enviroment import Environment, MAPS
from pandas import DataFrame
import numpy as np
import time
import os

# create environment
env = Environment()

# QTable : contains the Q-Values for every (state,action) pair
qtable = np.zeros(
    [env.state_count, env.action_count]
)  # np.random.rand(env.state_count, env.action_count).tolist()


# hyperparameters
epochs = 5000

gamma = 0.9
alpha = 0.1  # learning rate

epsilon = 0.1
max_epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.01

epochs_data = dict()

# training loop
for i in range(epochs):

    state, reward, done = env.reset()
    steps = 0
    reward_count = 0
    path = []
    while not done:
        # print("epoch #", i + 1, "/", epochs)
        # env.render()
        # time.sleep(0.05)

        # count steps to finish game
        steps += 1

        # act randomly sometimes to allow exploration
        if np.random.uniform() < epsilon:
            action = env.random_action()
        # if not select max action in Qtable (act greedy)
        else:
            action = np.argmax(qtable[state])

        # take action
        next_state, reward, done, step = env.step(action)

        # update qtable value with Bellman equation
        # qtable[state][action] = reward + gamma * max(qtable[next_state])
        next_max = np.max(qtable[next_state])

        qtable[state, action] = qtable[state, action] + alpha * (
            reward + gamma * next_max - qtable[state, action]
        )
        reward_count += reward
        # update state
        state = next_state
        path.append(step)
    # The more we learn, the less we take random actions
    epsilon = min_epsilon + (max_epsilon - min_epsilon) * np.exp(-0.1 * epsilon)
    # print("\nDone in", steps, "steps".format(steps))
    epochs_data[i] = {"steps": steps, "reward": reward_count, "path": path}

res = epochs_data[
    max(range(len(epochs_data)), key=lambda index: epochs_data[index]["reward"])
]
print(res)

new_map = MAPS["6x10"]
for step in res["path"]:
    aux = step[0]
    new_map[aux[0]][aux[1]] = 'X' 
print(DataFrame(new_map))
print()
time.sleep(0.8)
