# Q17: Hierarchical Reinforcement Learning using HAM and MAXQ
# Household robot with high-level tasks:
# Clean -> Kitchen, Clean -> LivingRoom, Recharge.
#
# HAM-style hierarchy is represented by a finite task machine.
# MAXQ decomposes value into subtasks.

import random

rooms = ["Kitchen", "LivingRoom"]
tasks = ["CleanKitchen", "CleanLivingRoom", "Recharge"]

Q = {task: {room: 0.0 for room in rooms} for task in tasks}

def execute_task(task):
    if task == "CleanKitchen":
        return "Kitchen", 10
    if task == "CleanLivingRoom":
        return "LivingRoom", 10
    return "Charger", 5

# MAXQ-style recursive value decomposition
def maxq_value(task, state):
    if task == "CleanKitchen":
        return Q[task]["Kitchen"]
    if task == "CleanLivingRoom":
        return Q[task]["LivingRoom"]
    if task == "Recharge":
        return 5
    return 0

# HAM controller:
# Root -> choose task -> execute primitive action.
for episode in range(500):
    state = random.choice(rooms)

    # Select a subtask using epsilon-greedy policy.
    epsilon = max(0.05, 1 - episode / 500)

    if random.random() < epsilon:
        task = random.choice(tasks)
    else:
        task = max(tasks, key=lambda t: maxq_value(t, state))

    result, reward = execute_task(task)

    # MAXQ component-value update
    if task in Q:
        target = reward
        Q[task][state] += 0.1 * (target - Q[task][state])

print("Q17 - Hierarchical Reinforcement Learning")
print("\nHAM hierarchy:")
print("ROOT")
print(" ├── CleanKitchen")
print(" ├── CleanLivingRoom")
print(" └── Recharge")

print("\nMAXQ learned component values:")
for task in tasks:
    print(task, Q[task])

# Test hierarchical execution
sequence = ["CleanKitchen", "CleanLivingRoom", "Recharge"]

print("\nExample hierarchical task sequence:")
for task in sequence:
    print(task, "->", execute_task(task))
