import mdp_obj.mdp_sets as mdp_sets

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
    return list(P[current_state][executed_action].values())

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

    return MDP(S, A, R, P)





