import numpy as np

# States: 0 and 1
# Actions: 0 and 1

# Transition probabilities: P[s][a][s']
P = {
    0: {0: [0.8, 0.2], 1: [0.5, 0.5]},
    1: {0: [0.1, 0.9], 1: [0.7, 0.3]}
}

# Rewards: R[s][a]
R = {
    0: {0: 5, 1: 10},
    1: {0: -1, 1: 2}
}

gamma = 0.9  # Discount factor
V = np.zeros(2)  # Initialize value function

# Value Iteration
for _ in range(10):
    new_V = np.zeros(2)
    for s in range(2):
        values = []
        for a in range(2):
            value = R[s][a] + gamma * sum(P[s][a][s_next] * V[s_next] for s_next in range(2))
            values.append(value)
        new_V[s] = max(values)
    V = new_V

print("Optimal state values:", V)