import random

prices = [80, 100, 120]

probability = {
    80: 0.80,
    100: 0.60,
    120: 0.40
}

revenue = {price: 0 for price in prices}
count = {price: 0 for price in prices}

for i in range(1000):

    if random.random() < 0.1:
        price = random.choice(prices)
    else:
        price = max(
            prices,
            key=lambda p: revenue[p] / max(count[p], 1)
        )

    count[price] += 1

    if random.random() < probability[price]:
        revenue[price] += price

print("DYNAMIC PRICING")
print("----------------")

for price in prices:
    print(
        "Price:", price,
        "Revenue:", round(revenue[price], 2)
    )

best = max(prices, key=lambda p: revenue[p])

print("\nBest price:", best)