import random

states = [
    "Low Patient Load",
    "Medium Patient Load",
    "High Patient Load"
]

actions = [
    "Normal Staff",
    "Add Staff",
    "Add Emergency Staff"
]

Q = {}

for state in states:
    for action in actions:
        Q[state, action] = 0

for episode in range(1000):

    state = random.choice(states)

    for step in range(10):

        action = random.choice(actions)

        if state == "High Patient Load" and action == "Add Emergency Staff":
            reward = 10
        elif state == "Medium Patient Load" and action == "Add Staff":
            reward = 8
        elif state == "Low Patient Load" and action == "Normal Staff":
            reward = 6
        else:
            reward = -2

        Q[state, action] += 0.1 * (
            reward - Q[state, action]
        )

print("HEALTHCARE MANAGEMENT")
print("---------------------")

for state in states:

    best = max(
        actions,
        key=lambda a: Q[state, a]
    )

    print(state)
    print("Recommended action:", best)
    print()

print("Training completed.")