states = ["Low Traffic", "High Traffic"]
actions = ["Short Green", "Long Green"]

policy = {
    "Low Traffic": "Short Green",
    "High Traffic": "Long Green"
}

rewards = {
    ("Low Traffic", "Short Green"): 8,
    ("Low Traffic", "Long Green"): 5,
    ("High Traffic", "Short Green"): 3,
    ("High Traffic", "Long Green"): 10
}

for i in range(10):

    changed = False

    for state in states:

        best_action = max(
            actions,
            key=lambda a: rewards[state, a]
        )

        if policy[state] != best_action:
            policy[state] = best_action
            changed = True

    if not changed:
        break

print("TRAFFIC LIGHT OPTIMIZATION")
print("--------------------------")

for state in states:
    print(state, "->", policy[state])

print("\nPolicy iteration completed.")