# Q4: Bellman equations for autonomous delivery robot
# Finds minimum travel cost using Bellman optimality equation.

import math

nodes = ["A", "B", "C", "D", "E"]
edges = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 5), ("E", 10)],
    "C": [("B", 1), ("D", 8)],
    "D": [("E", 2)],
    "E": []
}

goal = "E"
V = {n: math.inf for n in nodes}
V[goal] = 0
policy = {}

# Bellman equation:
# V(s) = min_a [cost(s,a) + V(s')]
for _ in range(len(nodes) - 1):
    for s in nodes:
        if s == goal:
            continue

        best_cost = math.inf
        best_next = None

        for ns, cost in edges[s]:
            value = cost + V[ns]
            if value < best_cost:
                best_cost = value
                best_next = ns

        V[s] = best_cost
        policy[s] = best_next

print("Q4 - Bellman Optimal Path")
print("Minimum costs to destination:")
for n in nodes:
    print(n, "->", V[n])

path = ["A"]
current = "A"

while current != goal:
    current = policy[current]
    path.append(current)

print("\nOptimal path:", " -> ".join(path))
print("Minimum travel cost:", V["A"])
