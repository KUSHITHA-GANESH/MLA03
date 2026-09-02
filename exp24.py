import random

actions = ["Buy", "Hold", "Sell"]
prices = [100, 102, 98, 105, 110, 108, 115, 112]

policy = {
    "Buy": 1,
    "Hold": 1,
    "Sell": 1
}

for episode in range(500):

    money = 1000
    shares = 0

    for i in range(len(prices) - 1):

        action = random.choice(actions)

        if action == "Buy" and money >= prices[i]:
            shares += 1
            money -= prices[i]

        elif action == "Sell" and shares > 0:
            money += prices[i]
            shares -= 1

    final_money = money + shares * prices[-1]
    profit = final_money - 1000

    for action in actions:
        policy[action] += 0.001 * profit

print("REINFORCE TRADING SYSTEM")
print("------------------------")

for action in actions:
    print(action, ":", round(policy[action], 2))

best = max(actions, key=lambda a: policy[a])

print("\nBest trading action:", best)