# Q16: Compare policy-gradient algorithms for autonomous lane keeping.
# Environment: lateral distance from lane center and heading error.
# Actions: steer left, straight, right.

import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

ACTIONS = 3
models = {}

def make_policy():
    return Sequential([
        Dense(32, activation="relu", input_shape=(2,)),
        Dense(32, activation="relu"),
        Dense(ACTIONS, activation="softmax")
    ])

def step(state, action):
    offset, heading = state
    steer = [-0.1, 0.0, 0.1][action]

    heading += steer
    offset += heading

    reward = 1.0 - abs(offset) - 0.2 * abs(heading)
    done = abs(offset) > 2
    return np.array([offset, heading], dtype=np.float32), reward, done

def train(method, episodes=500):
    policy = make_policy()
    opt = tf.keras.optimizers.Adam(0.003)
    gamma = 0.95

    for _ in range(episodes):
        state = np.array([np.random.uniform(-1,1), 0.0], dtype=np.float32)
        logps, rewards = [], []

        for _ in range(50):
            probs = policy(state[None])[0]
            action = int(tf.random.categorical(tf.math.log([probs]), 1)[0,0])
            ns, reward, done = step(state, action)

            logps.append(tf.math.log(probs[action] + 1e-8))
            rewards.append(reward)
            state = ns

            if done:
                break

        returns = []
        G = 0
        for r in reversed(rewards):
            G = r + gamma * G
            returns.insert(0, G)

        returns = np.array(returns)
        if method == "Baseline":
            returns = (returns - returns.mean()) / (returns.std() + 1e-8)

        with tf.GradientTape() as tape:
            loss = -tf.reduce_sum(tf.stack(logps) * returns)

        grads = tape.gradient(loss, policy.trainable_variables)
        opt.apply_gradients(zip(grads, policy.trainable_variables))

    return policy

for method in ["REINFORCE", "Baseline"]:
    models[method] = train(method)

for name, policy in models.items():
    state = np.array([0.8, 0.0], dtype=np.float32)
    total = 0

    for _ in range(50):
        probs = policy.predict(state[None], verbose=0)[0]
        action = int(np.argmax(probs))
        state, reward, done = step(state, action)
        total += reward
        if done:
            break

    print(f"{name}: evaluation reward = {total:.2f}")

print("\nQ16 - Lane Keeping")
print("Higher evaluation reward indicates better stability.")
