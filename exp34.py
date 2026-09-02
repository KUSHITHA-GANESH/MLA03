import random

states = ["Cold", "Comfortable", "Hot"]
actions = ["Heat", "Maintain", "Cool"]

policy = {}

for state in states:
    for action in actions:
        policy[state, action] = 0

for episode in range(1000):

    state = random.choice(states)
    action = random.choice(actions)

    if state == "Cold" and action == "Heat":
        reward = 10
    elif state == "Hot" and action == "Cool":
        reward = 10
    elif state == "Comfortable" and action == "Maintain":
        reward = 10
    else:
        reward = -2

    policy[state, action] += 0.01 * reward

print("SMART HOME ENERGY MANAGEMENT")
print("----------------------------")

for state in states:

    best = max(
        actions,
        key=lambda a: policy[state, a]
    )

    print(state, "->", best)

print("\nREINFORCE training completed.")