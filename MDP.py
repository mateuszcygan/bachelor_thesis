import random
import pickle
import mdp_sets

class MDP:
    def __init__(self, states, actions, rewards, probabilities):
        self.states = states
        self.actions = actions
        self.rewards = rewards
        self.probabilities = probabilities
    
    def get_states(self):
        return self.states

    def get_actions(self):
        return self.actions
    
    def get_rewards(self):
        return self.rewards
    
    def get_probabilities(self):
        return self.probabilities

def createMDP():
    S = ['s0', 's1', 's2'] #state space
    A = ['a0', 'a1'] #action space
    # S = mdp_sets.generate_states()
    # A = mdp_sets.generate_actions()

    R = mdp_sets.generate_rewards(S, A)
    P = mdp_sets.generate_prob(S, A)

    # print(R)
    # print(P)

    return MDP(S, A, R, P) 

    # Doesn't work properly
    # with open("generated_R.txt", "w") as file:
    #     pickle.dump(R, file)

