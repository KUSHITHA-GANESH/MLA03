# Q5: Epsilon-greedy Multi-Armed Bandit
# Online advertisement recommendation system.

import random

true_click_rates = [0.10, 0.20, 0.35, 0.15, 0.25]
n_ads = len(true_click_rates)

counts = [0] * n_ads
values = [0.0] * n_ads

epsilon = 0.1
rounds = 10000
clicks = 0

for t in range(rounds):
    # Exploration vs exploitation
    if random.random() < epsilon:
        ad = random.randrange(n_ads)
    else:
        ad = max(range(n_ads), key=lambda i: values[i])

    # Simulate user click
    reward = 1 if random.random() < true_click_rates[ad] else 0

    counts[ad] += 1
    clicks += reward

    # Incremental average
    values[ad] += (reward - values[ad]) / counts[ad]

print("Q5 - Epsilon-Greedy Advertisement Recommendation")
for i in range(n_ads):
    print(
        f"Ad {i+1}: selections={counts[i]}, "
        f"estimated CTR={values[i]:.4f}, "
        f"true CTR={true_click_rates[i]:.2f}"
    )

print("\nTotal clicks:", clicks)
print("Overall engagement rate:", round(clicks / rounds, 4))
print("Best recommended ad:", values.index(max(values)) + 1)
