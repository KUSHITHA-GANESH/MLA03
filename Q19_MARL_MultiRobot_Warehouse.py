# Q19: Multi-Agent Reinforcement Learning for warehouse robots
# Two robots cooperatively collect two packages.
#
# Each robot uses Q-learning.
# Reward is shared: +20 when both package goals are completed,
# -1 for each movement, -5 for collision.

import random
from collections import defaultdict

GRID = 5
ACTIONS = [(-1,0), (1,0), (0,-1), (0,1)]

robots = [(0,0), (4,0)]
packages = {(0,4), (4,4)}

Q1 = defaultdict(float)
Q2 = defaultdict(float)

def move(pos, action):
    r, c = pos
    dr, dc = ACTIONS[action]
    return (
        max(0, min(GRID-1, r+dr)),
        max(0, min(GRID-1, c+dc))
    )

def choose(Q, state, epsilon=0.1):
    if random.random() < epsilon:
        return random.randrange(4)
    return max(range(4), key=lambda a: Q[(state, a)])

alpha, gamma = 0.1, 0.95

for episode in range(3000):
    r1, r2 = robots
    collected = set()

    for _ in range(100):
        s1, s2 = r1, r2
        a1 = choose(Q1, s1)
        a2 = choose(Q2, s2)

        nr1 = move(r1, a1)
        nr2 = move(r2, a2)

        collision = nr1 == nr2
        if collision:
            reward = -5
            nr1, nr2 = r1, r2
        else:
            reward = -1

        if nr1 in packages:
            collected.add(nr1)
        if nr2 in packages:
            collected.add(nr2)

        if len(collected) == len(packages):
            reward += 20
            done = True
        else:
            done = False

        target1 = reward + gamma * max(
            Q1[(nr1, a)] for a in range(4)
        )
        target2 = reward + gamma * max(
            Q2[(nr2, a)] for a in range(4)
        )

        Q1[(s1, a1)] += alpha * (target1 - Q1[(s1, a1)])
        Q2[(s2, a2)] += alpha * (target2 - Q2[(s2, a2)])

        r1, r2 = nr1, nr2
        if done:
            break

# Demonstration
r1, r2 = robots
path1, path2 = [r1], [r2]
collected = set()

for _ in range(50):
    a1 = choose(Q1, r1, epsilon=0)
    a2 = choose(Q2, r2, epsilon=0)

    nr1, nr2 = move(r1, a1), move(r2, a2)

    if nr1 == nr2:
        break

    r1, r2 = nr1, nr2
    path1.append(r1)
    path2.append(r2)

    collected.update([r1, r2])
    if packages.issubset(collected):
        break

print("Q19 - Multi-Agent Reinforcement Learning")
print("Robot 1 path:", path1)
print("Robot 2 path:", path2)
print("Packages reached:", packages.intersection(collected))
print("Cooperative completion:", packages.issubset(collected))
