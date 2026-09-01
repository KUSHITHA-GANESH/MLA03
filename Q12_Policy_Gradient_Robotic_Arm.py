# Q12: Policy-based Reinforcement Learning for robotic arm pick-and-place
# REINFORCE-style policy gradient on a simplified 2D arm task.

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

ACTIONS = 4  # left, right, up, down
GOAL = np.array([4.0, 4.0])

model = Sequential([
    Dense(32, activation="relu", input_shape=(2,)),
    Dense(32, activation="relu"),
    Dense(ACTIONS, activation="softmax")
])

optimizer = tf.keras.optimizers.Adam(0.01)

def action_step(pos, action):
    moves = [(-1,0), (1,0), (0,-1), (0,1)]
    nxt = pos + np.array(moves[action], dtype=np.float32)
    nxt = np.clip(nxt, 0, 4)

    distance = np.linalg.norm(GOAL - nxt)
    reward = 10 if distance == 0 else -distance
    done = distance == 0
    return nxt, reward, done

gamma = 0.95

for episode in range(1000):
    pos = np.array([0.0, 0.0])
    log_probs, rewards = [], []

    for _ in range(30):
        with tf.GradientTape() as tape:
            probs = model(pos[None], training=True)[0]
            action = tf.random.categorical(tf.math.log([probs]), 1)[0, 0]
            log_prob = tf.math.log(probs[action] + 1e-8)

        pos, reward, done = action_step(pos, int(action))
        log_probs.append(log_prob)
        rewards.append(reward)

        if done:
            break

    returns = []
    G = 0
    for r in reversed(rewards):
        G = r + gamma * G
        returns.insert(0, G)

    returns = tf.convert_to_tensor(returns, dtype=tf.float32)

    with tf.GradientTape() as tape:
        loss = -tf.reduce_sum(tf.stack(log_probs) * returns)

    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

# Test
pos = np.array([0.0, 0.0])
path = [tuple(pos.astype(int))]

for _ in range(30):
    probs = model.predict(pos[None], verbose=0)[0]
    action = int(np.argmax(probs))
    pos, _, done = action_step(pos, action)
    path.append(tuple(pos.astype(int)))
    if done:
        break

print("Q12 - Policy Gradient Robotic Arm")
print("Pick-and-place path:", path)
print("Reached target:", tuple(pos.astype(int)) == (4, 4))
