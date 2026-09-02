road = {
    "Start": ["A", "B"],
    "A": ["C"],
    "B": ["D"],
    "C": ["Goal"],
    "D": ["Goal"],
    "Goal": []
}

current = "Start"

print("AUTONOMOUS CAR NAVIGATION")
print("-------------------------")

while current != "Goal":

    print("Current location:", current)

    next_places = road[current]

    # Choose first safe route
    current = next_places[0]

print("Destination reached!")