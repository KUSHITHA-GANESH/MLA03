# Q3: MDP for autonomous warehouse robot
# Defines states, actions, transition probabilities and rewards.

states = [
    "Shelf_A", "Shelf_B", "Shelf_C",
    "Packing", "Charging"
]

actions = ["move", "charge", "wait"]

# Transition model:
# P(next_state | state, action)
P = {
    ("Shelf_A", "move"): {"Shelf_B": 1.0},
    ("Shelf_B", "move"): {"Shelf_C": 0.8, "Packing": 0.2},
    ("Shelf_C", "move"): {"Packing": 1.0},
    ("Packing", "move"): {"Shelf_A": 1.0},
    ("Charging", "move"): {"Shelf_A": 1.0},

    ("Shelf_A", "charge"): {"Charging": 1.0},
    ("Shelf_B", "charge"): {"Charging": 1.0},
    ("Shelf_C", "charge"): {"Charging": 1.0},
    ("Packing", "charge"): {"Charging": 1.0},
    ("Charging", "charge"): {"Charging": 1.0},

    ("Shelf_A", "wait"): {"Shelf_A": 1.0},
    ("Shelf_B", "wait"): {"Shelf_B": 1.0},
    ("Shelf_C", "wait"): {"Shelf_C": 1.0},
    ("Packing", "wait"): {"Packing": 1.0},
    ("Charging", "wait"): {"Charging": 1.0},
}

R = {
    "Shelf_A": -1,
    "Shelf_B": -1,
    "Shelf_C": -1,
    "Packing": 10,
    "Charging": 2
}

actions = ["move", "charge", "wait"]
gamma = 0.9
V = {s: 0.0 for s in states}

for _ in range(100):
    newV = {}
    for s in states:
        values = []
        for a in actions:
            expected = 0
            for ns, prob in P[(s, a)].items():
                expected += prob * (R[ns] + gamma * V[ns])
            values.append(expected)
        newV[s] = max(values)
    V = newV

policy = {}
for s in states:
    policy[s] = max(actions, key=lambda a:
        sum(prob * (R[ns] + gamma * V[ns])
            for ns, prob in P[(s, a)].items()))

print("Q3 - Warehouse Robot MDP")
print("\nStates:", states)
print("Actions:", actions)
print("\nTransition probabilities:")
for key, value in P.items():
    print(key, "->", value)

print("\nOptimal values:")
for s in states:
    print(s, ":", round(V[s], 3))

print("\nOptimal policy:")
for s in states:
    print(s, "->", policy[s])
