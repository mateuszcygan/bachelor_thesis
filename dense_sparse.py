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

            
    



