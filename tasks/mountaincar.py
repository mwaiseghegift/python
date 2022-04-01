"""  
Neural Network: Implement approximated TD learning algorithm of your choice (Q-learning or
SARSA) using neural networks from the keras package and apply this algorithm to solve the
environments. Compute the models 𝑄(𝑠, 𝑎, 𝑤 𝑄 ) & 𝜋(𝑠, 𝑤 𝜋 )

"""

from keras.models import Sequential
from keras.layers import Dense, Actication, Flatten
from tensorflow.keras.optimizers import Adam
import numpy as np
import gym
import matplotlib.pyplot as plt

# Initialize the environment
env = gym.make('MountainCar-v0')

# Initialize the model
model = Sequential()
# Add the first layer
model.add(Dense(24, input_dim=2, activation='relu'))
# Add the second layer
model.add(Dense(24, activation='relu'))
# Add the third layer
model.add(Dense(1, activation='linear'))
# Compile the model
model.compile(loss='mse', optimizer=Adam(lr=0.001))

# Initialize the variables
episodes = 1000
max_steps = 200
gamma = 0.99
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995

# Initialize the lists
rewards = []
losses = []

# Run the episodes
for e in range(episodes):
    # Initialize the variables
    state = env.reset()
    state = np.reshape(state, [1, 2])
    total_reward = 0
    loss = 0
    done = False
    # Run the episode
    for step in range(max_steps):
        # Render the environment
        env.render()
        # Choose an action
        if np.random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(model.predict(state))
        # Take the action
        new_state, reward, done, info = env.step(action)
        new_state = np.reshape(new_state, [1, 2])
        # Update the variables
        total_reward += reward
        # Update the model
        target = reward + gamma * np.amax(model.predict(new_state))
        target_f = model.predict(state)
        target_f[0][action] = target
        # Train the model
        loss += model.train_on_batch(state, target_f)
        # Update the variables
        state = new_state
        # Check if the episode is done
        if done:
            break
    # Update the variables
    rewards.append(total_reward)
    losses.append(loss)
    # Update the epsilon
    epsilon = max(epsilon_min, epsilon * epsilon_decay)

    # Print the results
    print('Episode: {}/{}'.format(e, episodes),
            'Total reward: {}'.format(total_reward),
            'Training loss: {:.4f}'.format(loss),
            'Epsilon: {:.4f}'.format(epsilon))
            

# Plot the rewards
plt.plot(rewards)
plt.show()
