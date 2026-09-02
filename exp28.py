states = ["A", "B", "C", "D", "Goal"]

values = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "Goal": 10
}

paths = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "Goal"
}

for i in range(10):

    for state in ["D", "C", "B", "A"]:
        next_state = paths[state]
        values[state] = -1 + 0.9 * values[next_state]

print("BELLMAN OPTIMAL VALUES")
print("----------------------")

for state in states:
    print(state, ":", round(values[state], 2))

print("\nOptimal path:")

state = "A"

while state != "Goal":
    print(state, "->", end=" ")
    state = paths[state]

print("Goal")