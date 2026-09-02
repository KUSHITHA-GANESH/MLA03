import random

ads = ["Ad A", "Ad B", "Ad C"]

click_probability = {
    "Ad A": 0.20,
    "Ad B": 0.40,
    "Ad C": 0.30
}

# Epsilon Greedy
clicks = {ad: 0 for ad in ads}
shown = {ad: 0 for ad in ads}

for i in range(1000):

    if random.random() < 0.1:
        ad = random.choice(ads)
    else:
        ad = max(
            ads,
            key=lambda x: clicks[x] / max(shown[x], 1)
        )

    shown[ad] += 1

    if random.random() < click_probability[ad]:
        clicks[ad] += 1

print("ADVERTISEMENT BANDIT")
print("---------------------")

for ad in ads:
    ctr = clicks[ad] / shown[ad]
    print(ad, "CTR:", round(ctr, 3))

best = max(ads, key=lambda x: clicks[x] / shown[x])

print("\nBest advertisement:", best)