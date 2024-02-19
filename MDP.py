import random
import pickle
import mdp_sets

def print_transition_details(transition_dict):
    for state, actions_dict in transition_dict.items():
        print(state)
        for action, properties in actions_dict.items():
            print(action, ":", properties)

def createMDP():
    S = ['s0', 's1', 's2'] #state space
    A = ['a0', 'a1'] #action space
    # S = mdp_sets.generate_states()
    # A = mdp_sets.generate_actions()

    R = mdp_sets.generate_rewards(S, A)
    P = mdp_sets.generate_prob(S, A)

    # print(R)
    # print(P)

    return (S, A, R, P) 

    # Doesn't work properly
    # with open("generated_R.txt", "w") as file:
    #     pickle.dump(R, file)

