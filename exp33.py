import random

actions = [
    "Gather Resources",
    "Build Unit",
    "Attack"
]

score = {
    "Gather Resources": 0,
    "Build Unit": 0,
    "Attack": 0
}

for episode in range(1000):

    action = random.choice(actions)

    if action == "Gather Resources":
        reward = 5
    elif action == "Build Unit":
        reward = 8
    else:
        reward = 10

    score[action] += reward * 0.01

print("RTS GAME - DDPG")
print("---------------")

for action in actions:
    print(action, ":", round(score[action], 2))

best = max(actions, key=lambda a: score[a])

print("\nBest action:", best)