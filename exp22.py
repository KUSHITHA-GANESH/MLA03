import random

grid = [
    ["A", ".", ".", "."],
    [".", "#", ".", "."],
    [".", ".", "F", "."],
    [".", ".", "G", "E"]
]

actions = ["up", "down", "left", "right"]
Q = {}

for r in range(4):
    for c in range(4):
        for action in actions:
            Q[(r, c, action)] = 0

def move(state, action):
    r, c = state

    if action == "up":
        r -= 1
    elif action == "down":
        r += 1
    elif action == "left":
        c -= 1
    elif action == "right":
        c += 1

    if r < 0 or r >= 4 or c < 0 or c >= 4:
        return state

    if grid[r][c] == "#":
        return state

    return (r, c)

def reward(state):
    if state == (2, 2):
        return 10
    if state == (3, 2):
        return -10
    if state == (3, 3):
        return 20
    return -1

# Training
for episode in range(1000):

    state = (0, 0)

    for step in range(50):

        if random.random() < 0.2:
            action = random.choice(actions)
        else:
            action = max(
                actions,
                key=lambda a: Q[state[0], state[1], a]
            )

        next_state = move(state, action)
        r = reward(next_state)

        best = max(
            Q[next_state[0], next_state[1], a]
            for a in actions
        )

        Q[state[0], state[1], action] += 0.1 * (
            r + 0.9 * best -
            Q[state[0], state[1], action]
        )

        state = next_state

        if state == (3, 3) or state == (3, 2):
            break

# Evaluation
state = (0, 0)

print("Q-LEARNING GRID GAME")
print("--------------------")

for step in range(30):

    print("Position:", state)

    action = max(
        actions,
        key=lambda a: Q[state[0], state[1], a]
    )

    state = move(state, action)

    if state == (2, 2):
        print("Food collected!")
    elif state == (3, 2):
        print("Ghost reached! Game over.")
        break
    elif state == (3, 3):
        print("Goal reached! SUCCESS")
        break