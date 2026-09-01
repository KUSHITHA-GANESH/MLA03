# Q7: Dynamic Programming for autonomous taxi routing
# Value Iteration computes the optimal driving policy.

import math

states = ["A", "B", "C", "D", "E", "TaxiStand"]
goal = "TaxiStand"

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("A", 4), ("D", 5)],
    "C": [("A", 2), ("D", 3)],
    "D": [("B", 5), ("C", 3), ("E", 2)],
    "E": [("D", 2), ("TaxiStand", 4)],
    "TaxiStand": []
}

V = {s: math.inf for s in states}
V[goal] = 0
policy = {}

# Bellman optimality equation for shortest path
for _ in range(100):
    newV = V.copy()

    for s in states:
        if s == goal:
            continue

        best = math.inf
        best_next = None

        for ns, cost in graph[s]:
            value = cost + V[ns]
            if value < best:
                best = value
                best_next = ns

        newV[s] = best
        policy[s] = best_next

    if newV == V:
        break
    V = newV

print("Q7 - Taxi Routing using Dynamic Programming")
print("\nOptimal cost:")
for s in states:
    print(s, ":", V[s])

print("\nOptimal policy:")
for s in states:
    if s != goal:
        print(s, "->", policy[s])

start = "A"
path = [start]
current = start

while current != goal:
    current = policy[current]
    path.append(current)

print("\nOptimal route:", " -> ".join(path))
print("Total driving cost:", V[start])
