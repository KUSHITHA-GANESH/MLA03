import random

lanes = ["Left", "Middle", "Right"]
actions = ["Stay", "Left", "Right"]

policy = {}

for lane in lanes:
    for action in actions:
        policy[lane, action] = 0

for episode in range(1000):

    lane = random.choice(lanes)

    for step in range(10):

        action = random.choice(actions)

        if lane == "Middle" and action == "Left":
            reward = 5
        elif lane == "Middle" and action == "Right":
            reward = 5
        elif action == "Stay":
            reward = 1
        else:
            reward = -1

        policy[lane, action] += 0.1 * (
            reward - policy[lane, action]
        )

print("AUTONOMOUS VEHICLE - PPO")
print("------------------------")

for lane in lanes:
    best = max(actions, key=lambda a: policy[lane, a])
    print("Lane:", lane)
    print("Best action:", best)