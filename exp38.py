import random

states = ["Room A", "Room B", "Room C"]
actions = ["Forward", "Left", "Right"]

belief = {
    "Room A": 0.33,
    "Room B": 0.33,
    "Room C": 0.34
}

print("POMDP ROBOT NAVIGATION")
print("-----------------------")

for step in range(10):

    action = random.choice(actions)

    print("Step:", step + 1)
    print("Action:", action)

    # Simulated sensor observation
    observation = random.choice(states)

    # Update belief
    for state in states:
        if state == observation:
            belief[state] += 0.1
        else:
            belief[state] -= 0.05

    print("Observation:", observation)

best_state = max(belief, key=belief.get)

print("\nRobot believes it is in:", best_state)
print("Navigation completed.")