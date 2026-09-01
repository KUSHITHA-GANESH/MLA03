# Q1: MDP for a simplified chess game
# A tiny 1D chess-like game: White King tries to capture Black King.
# States = (white_position, black_position, turn)
# Actions = move left/right
# Rewards: +10 win, -10 illegal/lose, -1 per move

from collections import defaultdict

BOARD_SIZE = 5
ACTIONS = [-1, 1]  # left, right

def legal_actions(state):
    w, b, turn = state
    actions = []
    for a in ACTIONS:
        nw = w + a if turn == 0 else w
        nb = b + a if turn == 1 else b
        if 0 <= nw < BOARD_SIZE and 0 <= nb < BOARD_SIZE:
            if nw != nb:
                actions.append(a)
    return actions

def transition(state, action):
    w, b, turn = state
    if turn == 0:
        w += action
    else:
        b += action
    return (w, b, 1 - turn)

def reward(next_state):
    w, b, _ = next_state
    return 10 if w == b else -1

states = [(w, b, t) for w in range(BOARD_SIZE)
          for b in range(BOARD_SIZE) if w != b
          for t in (0, 1)]

# Value iteration
V = defaultdict(float)
gamma = 0.9

for _ in range(100):
    newV = V.copy()
    for s in states:
        acts = legal_actions(s)
        if not acts:
            continue
        values = []
        for a in acts:
            ns = transition(s, a)
            values.append(reward(ns) + gamma * V[ns])
        newV[s] = max(values)
    V = newV

# Derive optimal policy
policy = {}
for s in states:
    acts = legal_actions(s)
    if acts:
        policy[s] = max(acts, key=lambda a:
                         reward(transition(s, a)) + gamma * V[transition(s, a)])

start = (0, 4, 0)
print("Q1 - Simplified Chess MDP")
print("Start state:", start)
print("Optimal action from start:", policy.get(start))
print("Estimated value:", round(V[start], 3))
print("\nSample optimal policy:")
for s in list(policy)[:10]:
    print(s, "->", policy[s])
