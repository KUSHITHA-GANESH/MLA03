# Q13: REINFORCE for autonomous parking
# Simplified parking environment.
# State = (x, y), goal = parking slot.

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

ACTIONS = 4
GOAL = np.array([4.0, 4.0])

policy = Sequential([
    Dense(32, activation="relu", input_shape=(2,)),
    Dense(32, activation="relu"),
    Dense(ACTIONS, activation="softmax")
])

optimizer = tf.keras.optimizers.Adam(0.005)
gamma = 0.95

def step(state, action):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    ns = np.clip(state + np.array(moves[action]), 0, 4)
    d = np.linalg.norm(GOAL - ns)

    if d == 0:
        return ns, 20, True
    return ns, -1 - 0.5*d, False

for ep in range(1500):
    state = np.array([0.0, 0.0])
    log_probs, rewards = [], []

    for _ in range(40):
        probs = policy(state[None])[0]
        action = int(tf.random.categorical(tf.math.log([probs]), 1)[0,0])

        state2, reward, done = step(state, action)
        log_probs.append(tf.math.log(probs[action] + 1e-8))
        rewards.append(reward)
        state = state2

        if done:
            break

    G = 0
    returns = []
    for r in reversed(rewards):
        G = r + gamma * G
        returns.insert(0, G)

    returns = np.array(returns)
    returns = (returns - returns.mean()) / (returns.std() + 1e-8)

    with tf.GradientTape() as tape:
        # Recompute probabilities for stored state sequence is simplified here.
        loss = -tf.reduce_sum(tf.stack(log_probs) * returns)

    grads = tape.gradient(loss, policy.trainable_variables)
    optimizer.apply_gradients(zip(grads, policy.trainable_variables))

state = np.array([0.0, 0.0])
path = [tuple(state.astype(int))]

for _ in range(40):
    probs = policy.predict(state[None], verbose=0)[0]
    action = int(np.argmax(probs))
    state, _, done = step(state, action)
    path.append(tuple(state.astype(int)))
    if done:
        break

print("Q13 - REINFORCE Autonomous Parking")
print("Parking path:", path)
print("Parked successfully:", np.array_equal(state, GOAL))
