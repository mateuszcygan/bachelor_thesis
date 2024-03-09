import mdp
import random
import mdp_files_generator as mfg
import print_mdp
import math_functions as math

# Function that outputs how many states have the probability 0.0 (are unreachable)
def unreachable_states(mdp_object):
    states = mdp_object.states
    actions = mdp_object.actions
    P = mdp_object.probabilities
    print("Number of possible states:", len(states))

    unreachable_overall = 0

    for s in states:
        for a in actions:
            prob_values = list(P[s][a].values())
            for prob_value in prob_values:
                unreachable = 0
                if prob_value == 0.0:
                    unreachable += 1
            print("Unreachable states:", unreachable)
            unreachable_overall += unreachable

    print("Unreachable states in the whole MDP:", unreachable_overall)

# test_mdp = mdp.createMDPupdated()
# unreachable_states(test_mdp)

# sparse mdps: take already created mdp, go through probabilities, change values some of them to 0
# P = {
#       's0' : {'a0' : { 's0' : 0.75, 's1' : 0.2, 's2' : 0.05},
#               'a1' : { 's0' : 0.3, 's1' : 0.2, 's2' : 0.5}
#               'a2' : { 's0' : 0.9, 's1' : 0.05, 's2' : 0.05}
#       }
#       's1' : {'a0' : { 's0' : 0.0, 's1' : 0.2, 's2' : 0.8},
#              { 'a1' : { ... }}
#       }
#     }

def sparse_prob(mdp, state_sparsity_rate):

    S = mdp.states
    A = mdp.actions
    P = mdp.probabilities
    old_probability_weight = 1 - state_sparsity_rate
    sparsity_weights = [state_sparsity_rate, old_probability_weight] # Sparse weights for probabilities 0.0 and going over to another state

    for current_state in S:
        for action in A:
            for following_state in S:
                possible_prob_values = [0.0] # Array to choose between 0.0 and probability value of going over to another state
                prob_value = P[current_state][action][following_state]

                # If any of the states is already unreachable, don't change it
                if prob_value == 0:
                    continue

                possible_prob_values.append(prob_value)
                new_prob_value = random.choices(possible_prob_values, weights = sparsity_weights)[0]
                P[current_state][action][following_state] = new_prob_value
            
            action_prob = list(P[current_state][action].values())
            print("New probability values for action", action, action_prob)
            math.normalize(action_prob)
            print("New probability values for action after normalization", action, action_prob)

        print("\n")

mdp_test = mfg.read_saved_mdp("mdp_object.pkl")
# print("States:", mdp_test.states)
# print("Actions:", mdp_test.actions)
print("Probabilities:")
print_mdp.print_prob_details(mdp_test.probabilities)
# print("Rewards:", mdp_test.rewards)

sparse_prob(mdp_test, 0.5)
print(mdp_test.probabilities)

# print(mdp_test.probabilities)

    



