import random
import pickle
import mdp_sets
import print_mdp as p

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
    
    def get_properties(self):
        return self.states, self.actions, self.rewards, self.probabilities

# Return an array with rewards for going over to following states through an executed action from a current state
def get_foll_states_rewards_values(R, current_state, executed_action): 
    return list(R[current_state][executed_action].values())

# Return an array with probabilities for going over to following states through an executed action from a current state
def get_foll_states_prob_values(P, current_state, executed_action):
    return [P[current_state][executed_action][prob] for prob in P[current_state][executed_action]]

# Return an array with possibe following states from certain state (based on Rewards set)
# Create a set that to each state assign following states - use this in this function to return following states /upcoming change
def get_following_states(R, current_action, current_state):
    return list(R[current_action][current_state].keys())

# Return an array with possible actions that can be executed from a certain state
def get_possible_actions(P, state):
    return list(P[state].keys())

def createMDP():
    # S = ['s0', 's1', 's2'] #state space
    # A = ['a0', 'a1'] #action space
    S = mdp_sets.generate_states()
    A = mdp_sets.generate_actions()

    R = mdp_sets.generate_rewards(S, A)
    P = mdp_sets.generate_prob(S, A)

    # print(R)
    # print(P)

    return MDP(S, A, R, P)





