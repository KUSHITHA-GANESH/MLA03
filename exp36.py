import random

tasks = [
    "Collect Resources",
    "Build Unit",
    "Complete Mission"
]

reward = {}

for task in tasks:
    reward[task] = 0

for episode in range(1000):

    for task in tasks:

        r = random.randint(1, 10)

        reward[task] += 0.01 * r

print("MAXQ HIERARCHICAL LEARNING")
print("--------------------------")

print("\nMain Task: Complete Mission")

for task in tasks:
    print(task, "Score:", round(reward[task], 2))

print("\nHierarchy:")
print("Complete Mission")
print("   |")
print("   +-- Collect Resources")
print("   +-- Build Unit")
print("   +-- Complete Mission")