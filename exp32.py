import random

states = ["A", "B", "C", "D"]
actions = ["Up", "Down", "Left", "Right"]

value = {}
advantage = {}

for state in states:
    value[state] = 0

    for action in actions:
        advantage[state, action] = 0

for episode in range(1000):

    state = random.choice(states)

    for action in actions:

        reward = random.choice([-1, 1, 5])

        value[state] += 0.01 * reward
        advantage[state, action] += 0.01 * reward

print("DUELING DQN")
print("-----------")

for state in states:

    q_values = {}

    for action in actions:
        q_values[action] = (
            value[state] +
            advantage[state, action]
        )

    best = max(q_values, key=q_values.get)

    print(state, "->", best)

print("\nDueling DQN training completed.")