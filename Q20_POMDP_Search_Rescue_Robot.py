# Q20: Search-and-rescue robot using a POMDP
#
# Hidden state: victim is either in Room A or Room B.
# Observation: noisy sensor result.
# Actions: search A, search B, move/scan.
#
# Belief state b(s) represents probability that victim is in each room.
# Belief update uses Bayes rule.

import numpy as np

states = ["Victim_A", "Victim_B"]
actions = ["Search_A", "Search_B", "Scan"]

# Sensor model:
# P(observation | actual state)
observation_model = {
    ("Victim_A", "Victim_A"): 0.9,
    ("Victim_A", "Victim_B"): 0.1,
    ("Victim_B", "Victim_A"): 0.1,
    ("Victim_B", "Victim_B"): 0.9
}

belief = {
    "Victim_A": 0.5,
    "Victim_B": 0.5
}

def update_belief(belief, observation):
    posterior = {}

    for state in states:
        posterior[state] = (
            observation_model[(state, observation)] * belief[state]
        )

    total = sum(posterior.values())

    for state in states:
        posterior[state] /= total

    return posterior

def choose_action(belief):
    # Search the room with highest current belief.
    if belief["Victim_A"] >= belief["Victim_B"]:
        return "Search_A"
    return "Search_B"

# Simulated observation says victim appears to be in A.
observation = "Victim_A"
new_belief = update_belief(belief, observation)

print("Q20 - POMDP Search and Rescue")
print("Initial belief:")
print(belief)

print("\nObservation:", observation)
print("Updated belief:")
print({k: round(v, 3) for k, v in new_belief.items()})

action = choose_action(new_belief)
print("\nBest action:", action)

# Expected immediate search utility
search_value_A = new_belief["Victim_A"] * 100 - 5
search_value_B = new_belief["Victim_B"] * 100 - 5

print("\nExpected utility:")
print("Search A:", round(search_value_A, 2))
print("Search B:", round(search_value_B, 2))
