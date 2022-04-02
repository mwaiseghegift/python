import math
import numpy as np
from numpy.random import random_integers as rnd
import matplotlib.pyplot as plt

import maze_v1

# Setup maze environment to simulate a 25x25 maze.
env = maze_v1.MazeMDP()
env.maze, env.width, env.height = env.make_maze(width=25, height=25, complexity=.05, density =.1)
env.start_loc = np.array([0,0])
x,y = np.where(env.maze == True)

# SARSA algorithm to solve the maze environmen, Compute the arrays Q(s, a) & π(s)

# parameters
alpha = 0.1
gamma = 0.9
epsilon = 0.1


# Initialize the arrays Q(s, a) & π(s)
Q = np.zeros((env.height, env.width, 4))

# Initialize the policy π(s)
policy = np.zeros((env.height, env.width), dtype=int)

# Function to choose the next action with episolon greedy
def choose_action(state):
    if rnd(0,1) < epsilon:
        action = rnd(0,3)
    else:
        action = np.argmax(Q[state[0], state[1]])
    return action

# Starting the SARSA learning
for i in range(10000):
     # Initialize the state
    state = env.start_loc
    # Initialize the action
    action = choose_action(state)
    # Initialize the reward
    reward = 0
    # Initialize the next state
    next_state = state
    # Initialize the nexttaction
    next_action = action

    while env.maze[next_state[0], next_state[1]] == False:
        # Update the Q(s, a)
        Q[state[0], state[1], action] = Q[state[0], state[1], action] + alpha * (reward + gamma * np.max(Q[next_state[0], next_state[1]]) - Q[state[0], state[1], action])
        # Update the policy
        policy[state[0], state[1]] = np.argmax(Q[state[0], state[1]])
        # Update the state
        state = next_state
        # Update the action
        action = next_action
        # Update the next state
        next_state = state
        # Update the next action
        next_action = choose_action(next_state)
        # Update the reward
        reward = 0
        # Check if the next state is terminal
        if env.maze[next_state[0], next_state[1]] == True:
            reward = 1

# Plot the maze
plt.figure(figsize=(10,10))
plt.imshow(env.maze.T, origin='lower', cmap='gray')
plt.xticks([]), plt.yticks([])


# Plot of reward over time with 𝜖 − 𝑔𝑟𝑒𝑒𝑑𝑦 exploration
plt.figure(figsize=(10,10))
plt.plot(np.arange(0,10000), np.cumsum(np.ones(10000)), label='Cumulative Reward')
plt.plot(np.arange(0,10000), np.ones(10000)*np.max(Q), label='Optimal Policy')
plt.xlabel('Time Steps')
plt.ylabel('Reward')
plt.legend()