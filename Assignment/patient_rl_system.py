import numpy as np
import random
import matplotlib.pyplot as plt

# ==========================================
# RL-BASED PATIENT HEALTH MONITORING SYSTEM
# ==========================================

# 1. Patient States
states = [
    "Stable",
    "Mild",
    "Moderate",
    "Severe",
    "Recovery"
]

# 2. Available Actions
actions = [
    "Monitoring",
    "Medication",
    "Increased Monitoring",
    "Hospital Referral"
]

# 3. Initialize Q-Table
Q = np.zeros((len(states), len(actions)))

learning_rate = 0.2
discount_factor = 0.9

# 4. Patient Environment
def step(state, action):

    # Stable
    if state == 0:
        if action == 0:
            return 0, 2
        else:
            return 0, 0

    # Mild
    elif state == 1:
        if action == 1:
            return 4, 20
        elif action == 2:
            return 2, 1
        elif action == 0:
            return 1, 0
        else:
            return 2, -2

    # Moderate
    elif state == 2:
        if action == 2:
            return 1, 2
        elif action == 1:
            return 1, 1
        else:
            return 3, -5

    # Severe
    elif state == 3:
        if action == 3:
            return 4, 25
        elif action == 2:
            return 3, -5
        else:
            return 3, -10

    # Recovery
    else:
        return 4, 2


# 5. Training
np.random.seed(1)
random.seed(1)

episodes = 5000
episode_rewards = []

for episode in range(episodes):

    # Start from a random patient condition
    current_state = random.choice([0, 1, 2, 3])

    total_reward = 0

    # Exploration decreases during training
    epsilon = max(0.02, 1 - episode / 3500)

    for step_number in range(20):

        # Exploration or exploitation
        if random.random() < epsilon:
            action = random.randrange(len(actions))
        else:
            action = np.argmax(Q[current_state])

        # Perform action
        next_state, reward = step(current_state, action)

        # Bellman Q-learning update
        if next_state == 4:
            target = reward
        else:
            target = reward + discount_factor * np.max(Q[next_state])

        Q[current_state, action] = (
            Q[current_state, action]
            + learning_rate *
            (target - Q[current_state, action])
        )

        total_reward += reward

        # Stop after recovery
        if next_state == 4:
            break

        current_state = next_state

    episode_rewards.append(total_reward)


# ==========================================
# 6. LEARNED Q-TABLE
# ==========================================

print("=" * 55)
print("RL-BASED PATIENT HEALTH MONITORING SYSTEM")
print("=" * 55)

print("\nTraining completed successfully.")
print("Training Episodes:", episodes)

print("\nLearned Q-Table")
print("-" * 55)

print(
    f"{'State':<12}"
    f"{'Monitoring':>14}"
    f"{'Medication':>14}"
    f"{'Increased':>14}"
    f"{'Hospital':>14}"
)

for i in range(len(states)):
    print(
        f"{states[i]:<12}"
        f"{Q[i,0]:>14.2f}"
        f"{Q[i,1]:>14.2f}"
        f"{Q[i,2]:>14.2f}"
        f"{Q[i,3]:>14.2f}"
    )


# ==========================================
# 7. OPTIMAL POLICY
# ==========================================

optimal_policy = np.argmax(Q, axis=1)

print("\nOptimal Policy")
print("-" * 55)

for i in range(len(states)):
    print(
        f"{states[i]:<12} -> "
        f"{actions[optimal_policy[i]]}"
    )


# ==========================================
# 8. POLICY TESTING
# ==========================================

print("\nPolicy Testing")
print("-" * 55)

total_recoveries = 0
total_tests = 0
intervention_recoveries = 0
intervention_tests = 0

for start_state in range(4):

    recoveries = 0

    for test in range(100):

        current_state = start_state

        for step_number in range(20):

            action = optimal_policy[current_state]

            next_state, reward = step(
                current_state,
                action
            )

            if next_state == 4:
                recoveries += 1
                break

            current_state = next_state

    total_recoveries += recoveries
    total_tests += 100

    # Exclude Stable state from intervention recovery
    if start_state != 0:
        intervention_recoveries += recoveries
        intervention_tests += 100

    print(
        f"{states[start_state]:<12} | "
        f"Action: {actions[optimal_policy[start_state]]:<22} | "
        f"Recovery: {recoveries}/100"
    )


# ==========================================
# 9. PERFORMANCE METRICS
# ==========================================

overall_recovery_rate = (
    total_recoveries / total_tests
) * 100

intervention_recovery_rate = (
    intervention_recoveries / intervention_tests
) * 100

average_reward = np.mean(
    episode_rewards[-100:]
)

# Treatment effectiveness:
# Percentage of intervention states successfully reaching recovery
treatment_effectiveness = intervention_recovery_rate


print("\nPerformance Results")
print("-" * 55)

print(
    f"Overall Recovery Rate: "
    f"{overall_recovery_rate:.2f}%"
)

print(
    f"Intervention Recovery Rate: "
    f"{intervention_recovery_rate:.2f}%"
)

print(
    f"Treatment Effectiveness: "
    f"{treatment_effectiveness:.2f}%"
)

print(
    f"Average Cumulative Reward: "
    f"{average_reward:.2f}"
)


# ==========================================
# 10. REWARD GRAPH
# ==========================================

# Moving average for smoother graph
window = 100

moving_average = np.convolve(
    episode_rewards,
    np.ones(window) / window,
    mode="valid"
)

plt.figure(figsize=(10, 5))
plt.plot(moving_average)
plt.xlabel("Training Episodes")
plt.ylabel("Average Cumulative Reward")
plt.title("RL Training Performance")
plt.grid(True)
plt.show()


# ==========================================
# 11. FINAL RESULT
# ==========================================

print("\n" + "=" * 55)
print("FINAL RESULT")
print("=" * 55)

print("The RL agent successfully learned an optimal policy.")
print("The learned policy adapts according to patient condition.")
print("Training and evaluation completed successfully.")