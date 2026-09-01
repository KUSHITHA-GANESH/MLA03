# Q9: TD(0), SARSA and Q-Learning for warehouse robot navigation

import numpy as np
import random

GRID = 5
START = (0, 0)
GOAL = (4, 4)
OBSTACLES = {(1, 1), (2, 1), (3, 3)}

ACTIONS = [(-1,0), (1,0), (0,-1), (0,1)]

def step(state, action):
    r, c = state
    dr, dc = ACTIONS[action]
    nr, nc = r + dr, c + dc

    if not (0 <= nr < GRID and 0 <= nc < GRID):
        return state, -5, False

    if (nr, nc) in OBSTACLES:
        return state, -5, False

    if (nr, nc) == GOAL:
        return (nr, nc), 20, True

    return (nr, nc), -1, False

def choose(Q, state, epsilon):
    if random.random() < epsilon:
        return random.randrange(4)
    return int(np.argmax(Q[state[0], state[1]]))

def train_td0(episodes=2000):
    # TD(0) state-value learning
    V = np.zeros((GRID, GRID))
    alpha, gamma, epsilon = 0.1, 0.95, 0.1

    for _ in range(episodes):
        state = START

        for _ in range(100):
            action = random.randrange(4)
            ns, reward, done = step(state, action)

            td_target = reward if done else reward + gamma * V[ns[0], ns[1]]
            V[state[0], state[1]] += alpha * (
                td_target - V[state[0], state[1]]
            )

            state = ns
            if done:
                break

    return V

def train_sarsa(episodes=2000):
    Q = np.zeros((GRID, GRID, 4))
    alpha, gamma, epsilon = 0.1, 0.95, 0.1

    for _ in range(episodes):
        state = START
        action = choose(Q, state, epsilon)

        for _ in range(100):
            ns, reward, done = step(state, action)

            if done:
                target = reward
            else:
                na = choose(Q, ns, epsilon)
                target = reward + gamma * Q[ns[0], ns[1], na]

            Q[state[0], state[1], action] += alpha * (
                target - Q[state[0], state[1], action]
            )

            if done:
                break

            state, action = ns, na

    return Q

def train_qlearning(episodes=2000):
    Q = np.zeros((GRID, GRID, 4))
    alpha, gamma, epsilon = 0.1, 0.95, 0.1

    for _ in range(episodes):
        state = START

        for _ in range(100):
            action = choose(Q, state, epsilon)
            ns, reward, done = step(state, action)

            target = reward if done else (
                reward + gamma * np.max(Q[ns[0], ns[1]])
            )

            Q[state[0], state[1], action] += alpha * (
                target - Q[state[0], state[1], action]
            )

            state = ns
            if done:
                break

    return Q

V = train_td0()
Q_sarsa = train_sarsa()
Q_qlearn = train_qlearning()

print("Q9 - TD(0), SARSA and Q-Learning")
print("\nTD(0) state value at start:", round(V[START], 3))
print("SARSA best Q at start:", round(np.max(Q_sarsa[START]), 3))
print("Q-Learning best Q at start:", round(np.max(Q_qlearn[START]), 3))

print("\nSARSA best action at start:", int(np.argmax(Q_sarsa[START])))
print("Q-Learning best action at start:", int(np.argmax(Q_qlearn[START])))
