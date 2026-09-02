import random

states = ["Safe", "Slow", "Fast"]
actions = ["Slow Down", "Maintain", "Speed Up"]

Q = {}

for state in states:
    for action in actions:
        Q[state, action] = 0

for episode in range(1000):

    state = random.choice(states)

    for step in range(10):

        action = random.choice(actions)

        if state == "Fast" and action == "Slow Down":
            reward = 10
        elif state == "Slow" and action == "Speed Up":
            reward = 8
        elif state == "Safe" and action == "Maintain":
            reward = 5
        else:
            reward = -2

        Q[state, action] += 0.1 * (
            reward - Q[state, action]
        )

print("DQN AUTONOMOUS VEHICLE")
print("----------------------")

for state in states:
    best = max(actions, key=lambda a: Q[state, a])
    print(state, "->", best)

print("\nTraining completed.")