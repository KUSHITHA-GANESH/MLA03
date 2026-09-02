import random

portfolios = {
    "Portfolio A": [5, 6, 7, 8, 9],
    "Portfolio B": [3, 4, 5, 6, 7],
    "Portfolio C": [8, 5, 10, 6, 11]
}

print("INVESTMENT PORTFOLIO ANALYSIS")
print("-----------------------------")

results = {}

for name, returns in portfolios.items():

    average = sum(returns) / len(returns)

    predicted = average + random.uniform(-1, 1)

    results[name] = predicted

    print(
        name,
        "Average Return:",
        round(average, 2),
        "Predicted:",
        round(predicted, 2)
    )

best = max(results, key=results.get)

print("\nBest predicted portfolio:", best)