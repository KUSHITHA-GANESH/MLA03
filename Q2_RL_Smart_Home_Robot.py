# Q2: Reinforcement Learning agent for smart-home robot navigation
# Q-learning on a small grid.

import random
import numpy as np

GRID = 5
START = (0, 0)
GOAL = (4, 4)
OBSTACLES = {(1, 1), (2, 1), (3, 3)}

ACTIONS = [(-1,0), (1,0), (0,-1), (0,1)]
Q = np.zeros((GRID, GRID, 4))

alpha, gamma = 0.1, 0.95
epsilon = 1.0
epsilon_decay = 0.995
epsilon_min = 0.05

def step(state, action):
    r, c = state
    dr, dc = ACTIONS[action]
    nr, nc = r + dr, c + dc

    if nr < 0 or nr >= GRID or nc < 0 or nc >= GRID:
        return state, -5, False
    if (nr, nc) in OBSTACLES:
        return state, -5, False
    if (nr, nc) == GOAL:
        return (nr, nc), 20, True
    return (nr, nc), -1, False

for episode in range(2000):
    state = START

    for _ in range(100):
        if random.random() < epsilon:
            action = random.randrange(4)
        else:
            action = np.argmax(Q[state[0], state[1]])

        next_state, reward, done = step(state, action)

        old = Q[state[0], state[1], action]
        best_next = np.max(Q[next_state[0], next_state[1]])

        Q[state[0], state[1], action] = old + alpha * (
            reward + gamma * best_next - old
        )

        state = next_state
        if done:
            break

    epsilon = max(epsilon_min, epsilon * epsilon_decay)

# Test learned route
state = START
path = [state]

for _ in range(30):
    action = np.argmax(Q[state[0], state[1]])
    state, _, done = step(state, action)
    path.append(state)
    if done:
        break

print("Q2 - Smart Home Robot")
print("Learned path:", path)
print("Reached goal:", state == GOAL)
