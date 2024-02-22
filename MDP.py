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

def get_foll_states_rewards_values(R, executed_action, current_state):
    return [R[executed_action][current_state][reward] for reward in R[executed_action][current_state]]

def get_foll_states_prob_values(P, current_state, executed_action):
    return [P[current_state][executed_action][prob] for prob in P[current_state][executed_action]]


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

def createMDPupdated():
    S = ['s0', 's1', 's2'] #state space
    A = ['a0', 'a1'] #action space
    # S = mdp_sets.generate_states()
    # A = mdp_sets.generate_actions()

    R = mdp_sets.generate_rewards_update(S, A)
    P = mdp_sets.generate_prob(S, A)

    # print(R)
    # print(P)

    return MDP(S, A, R, P) 

createMDPupdated()


    # Doesn't work properly
    # with open("generated_R.txt", "w") as file:
    #     pickle.dump(R, file)

