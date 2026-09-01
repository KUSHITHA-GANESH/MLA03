# Q8: Monte Carlo prediction and control for robot vacuum cleaner
# Grid cells are rooms. Goal is to clean all required cells.
# Reward = +10 for cleaning a new room, -1 for movement,
# and -2 for revisiting a cleaned room.

import random
from collections import defaultdict

GRID = 3
START = (0, 0)
ALL_CELLS = {(r, c) for r in range(GRID) for c in range(GRID)}
ACTIONS = [(-1,0), (1,0), (0,-1), (0,1)]

Q = defaultdict(lambda: defaultdict(float))
returns = defaultdict(list)
policy = {}

def move(pos, action):
    r, c = pos
    dr, dc = action
    nr, nc = r + dr, c + dc

    if 0 <= nr < GRID and 0 <= nc < GRID:
        return (nr, nc)
    return pos

def choose_action(state, epsilon=0.2):
    if random.random() < epsilon:
        return random.choice(ACTIONS)
    return max(ACTIONS, key=lambda a: Q[state][a])

def generate_episode(epsilon=0.2):
    pos = START
    cleaned = {START}
    episode = []

    for _ in range(50):
        state = (pos, frozenset(cleaned))
        action = choose_action(state, epsilon)
        next_pos = move(pos, action)

        if next_pos not in cleaned:
            reward = 10
            cleaned.add(next_pos)
        else:
            reward = -2

        reward -= 1  # movement/energy cost
        episode.append((state, action, reward))
        pos = next_pos

        if cleaned == ALL_CELLS:
            break

    return episode

# Monte Carlo control: first-visit update
for episode_no in range(5000):
    episode = generate_episode(epsilon=max(0.05, 1 - episode_no / 5000))
    G = 0
    visited = set()

    for state, action, reward in reversed(episode):
        G += reward
        key = (state, action)

        if key not in visited:
            returns[key].append(G)
            Q[state][action] = sum(returns[key]) / len(returns[key])
            visited.add(key)

# Test learned policy
pos = START
cleaned = {START}
path = [pos]

for _ in range(50):
    state = (pos, frozenset(cleaned))
    action = max(ACTIONS, key=lambda a: Q[state][a])
    pos = move(pos, action)
    cleaned.add(pos)
    path.append(pos)

    if cleaned == ALL_CELLS:
        break

print("Q8 - Monte Carlo Robot Vacuum")
print("Cleaning path:", path)
print("Rooms cleaned:", len(cleaned), "/", len(ALL_CELLS))
print("All rooms cleaned:", cleaned == ALL_CELLS)
