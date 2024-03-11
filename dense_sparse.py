import mdp
import random
import mdp_files_generator as mfg
import print_mdp
import math_functions as math_fct

# Function that outputs the number of states with a probability of 0.0 (indicating unreachable states)
def unreachable_states(mdp_object):

    states = mdp_object.states
    actions = mdp_object.actions
    P = mdp_object.probabilities

    poss_states_transitions = len(states)*len(states)*len(actions)

    unreachable_overall = 0

    for s in states:
        for a in actions:
            prob_values = list(P[s][a].values())
            unreachable = 0
            for prob_value in prob_values:
                if prob_value == 0.0:
                    unreachable += 1
            print("Unreachable states:", unreachable)
            unreachable_overall += unreachable

    print("Number of transitions to other states:", poss_states_transitions)
    print("Unreachable states in the whole MDP:", unreachable_overall)
    
    unreachable_percentage = unreachable_overall/poss_states_transitions
    print("Percentage of unreachable states:", unreachable_percentage)

# For states without following actions (all probabilities are set to zero) randomly choose one following state
def random_following_state(mdp):
    print("\nrandom following state function")

    S = mdp.states
    A = mdp.actions
    P = mdp.probabilities

    for current_state in S:
        for action in A:
            print(list(P[current_state][action].values()))



# Thinning the reachable states in the MDP by using state_sparsity_rate - percentage of states that should be unreached
def sparse_mdp_states(mdp, state_sparsity_rate):

    S = mdp.states
    A = mdp.actions
    P = mdp.probabilities
    
    old_probability_weight = 1 - state_sparsity_rate
    sparsity_weights = [state_sparsity_rate, old_probability_weight] # Sparse weights for 0.0 probability and probability of going over to following state

    for current_state in S:
        for action in A:
            for following_state in S:

                possible_prob_values = [0.0]  # Array containing 0.0 probability and probability of transitioning to following state (used for decision-making)
                prob_value = P[current_state][action][following_state]

                # If any of the following states is already unreachable, don't change it
                if prob_value == 0:
                    continue

                possible_prob_values.append(prob_value)

                # Choose between 0.0 and old probability of transitioning to following state
                new_prob_value = random.choices(possible_prob_values, weights = sparsity_weights)[0]
                P[current_state][action][following_state] = new_prob_value

    math_fct.normalize_mdp_probabilities(mdp)
    random_following_state(mdp)



    



