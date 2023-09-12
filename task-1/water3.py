def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    # Define the capacities of the bottles
    capacities = (8, 5, 3)
    # Define the possible actions
    actions = []
    for i in range(3):
        for j in range(3):
            if i != j:
                # Pour water from bottle i to bottle j
                amount = min(x[i], capacities[j] - x[j])
                state = list(x)
                state[i] -= amount
                state[j] += amount
                actions.append((tuple(state), amount))
    return actions
