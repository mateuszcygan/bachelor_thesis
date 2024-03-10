def normalize_and_round(probabilities):
    total = sum(probabilities)
    
    if total == 0:
        return

    normalized_probabilities = [prob / total for prob in probabilities]
    rounded_probabilities = [round(prob, 2) for prob in normalized_probabilities]


    if sum(rounded_probabilities) == 1.0:
        return rounded_probabilities
    # Probabilities after rounding to two decimal places are not exactly equal 1.0
    else:
        surplus = sum(rounded_probabilities) - 1
        for elem in rounded_probabilities:
            if elem != 0:
                elem -= surplus
                return rounded_probabilities
            
def normalize(probabilities):
    total = sum(probabilities)

    if total == 0:
        return
    
    normalized_probabilities = [prob / total for prob in probabilities]
    print(normalized_probabilities)
    return normalized_probabilities

# Example to ask about
test = [0.4, 0.0, 0.45, 0.87, 5, 6]
test_arr = normalize(test)
print(test_arr)
print(sum(test_arr))

# Normalizing probabilities for following states of a certain MDP
def normalize_mdp_probabilities(mdp):

    S = mdp.states
    A = mdp.actions
    P = mdp.probabilities

    for current_state in S:
        for action in A:

            # Calculate the total value of probabilities for certain action
            action_prob = list(P[current_state][action].values())
            total = sum(action_prob)

            for foll_state in S:

                # Normalize the probability of following states
                try:
                    P[current_state][action][foll_state] = P[current_state][action][foll_state]/total
                except ZeroDivisionError:
                    P[current_state][action][foll_state] = 0