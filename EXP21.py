import random

states = ["Low", "Medium", "High"]
actions = ["Reduce", "Maintain", "Increase"]

Q = {}

for state in states:
    for action in actions:
        Q[state, action] = 0

for episode in range(1000):
    state = random.choice(states)

    for step in range(10):
        action = random.choice(actions)

        if state == "High" and action == "Reduce":
            reward = 10
        elif state == "Medium" and action == "Maintain":
            reward = 5
        elif state == "Low" and action == "Increase":
            reward = 3
        else:
            reward = -2

        next_state = random.choice(states)

        best_future = max(Q[next_state, a] for a in actions)

        Q[state, action] += 0.1 * (
            reward + 0.9 * best_future - Q[state, action]
        )

        state = next_state

print("SMART ENERGY MANAGEMENT")
print("-----------------------")

for state in states:
    best = max(actions, key=lambda a: Q[state, a])
    print(state, "->", best)

print("\nTraining completed.")