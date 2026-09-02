import random

states = ["Start", "Middle", "End"]
actions = ["Move 1", "Move 2", "Move 3"]

Q = {}

for state in states:
    for action in actions:
        Q[state, action] = 0

for episode in range(1000):

    state = "Start"

    for step in range(10):

        action = random.choice(actions)

        reward = random.choice([-1, 1, 5])

        next_state = random.choice(states)
        next_action = random.choice(actions)

        # SARSA update
        Q[state, action] += 0.1 * (
            reward +
            0.9 * Q[next_state, next_action] -
            Q[state, action]
        )

        state = next_state

print("SARSA AGENT")
print("-----------")

for state in states:

    best = max(
        actions,
        key=lambda a: Q[state, a]
    )

    print(state, "->", best)

print("\nSARSA training completed.")