# SARSA algorithm to solve the maze environmen, Compute the arrays Q(s, a) & π(s) using keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import random
import numpy as np
import maze_v1


# SARSA algorithm to solve the maze environmen, Compute the arrays Q(s, a) & π(s)

class SarsaAgent:
    def __init__(self, env, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

        self.Q = np.zeros((env.height, env.width, 4))
        self.policy = np.zeros((env.height, env.width), dtype=int)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            action = random.randint(0,3)
        else:
            action = np.argmax(self.Q[state[0], state[1]])
        return action

    def update(self, state, action, next_state, reward, next_action):
        self.Q[state[0], state[1], action] = self.Q[state[0], state[1], action] + self.alpha * (reward + self.gamma * self.Q[next_state[0], next_state[1], next_action] - self.Q[state[0], state[1], action])
        self.policy[state[0], state[1]] = np.argmax(self.Q[state[0], state[1]])

    def train(self, iterations=10000):
        for i in range(iterations):
            state = self.env.start_loc
            action = self.choose_action(state)
            reward = 0
            next_state = state
            next_action = action

            while self.env.maze[next_state[0], next_state[1]] == False:
                self.update(state, action, next_state, reward, next_action)
                state = next_state
                action = next_action
                next_state = state
                next_action = self.choose_action(next_state)
                reward = 0
                if self.env.maze[next_state[0], next_state[1]] == True:
                    reward = 1
    
def main():
    env = maze_v1.MazeMDP()
    env.maze, env.width, env.height = env.make_maze(width=100, height=100, complexity=.05, density =.1)
    env.start_loc = np.array([0,0])
    x,y = np.where(env.maze == True)

    agent = SarsaAgent(env)
    agent.train()

    plt.figure(figsize=(10,10))
    plt.imshow(env.maze.T, origin='lower', cmap='gray')
    plt.xticks([]), plt.yticks([])

    plt.figure(figsize=(10,10))
    plt.plot(np.arange(0,10000), np.cumsum(np.ones(10000)), label='Cumulative Reward')
    plt.plot(np.arange(0,10000), np.ones(10000)*np.max(agent.Q), label='Optimal Policy')
    plt.xlabel('Time Steps')
    plt.ylabel('Reward')
    plt.legend()    

if __name__ == "__main__":
    main()