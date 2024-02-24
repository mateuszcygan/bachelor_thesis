import random

def generate_states():
    S = []
    num_states = random.randint(3,9)
    for state_num in range(num_states):
        state = 's' + str(state_num)
        S.append(state)
    # print(S)
    return S




def generate_actions():
    A = []
    num_actions = random.randint(2,5)
    for action_num in range(num_actions):
        action = 'a' + str(action_num)
        A.append(action)
    # print(A)
    return A



# Rewards received after transitioning from state s to s' due to action a
# state : { action : reward }
# R = { 's0' : { 'a0' : 1, 'a1' : 3 },
#       's1' : { 'a0' : 4, 'a1' : 10},
#       's2' : { 'a0' : 5, 'a1' : 3}
#     }
def generate_rewards(states, actions):
        return {state : {action : random.randint(-5, 5) for action in actions} for state in states}

# Rewards updated
# After executing each action certain reward is assigned to each following state
# curr_state : { action : {foll_state1 : reward, foll_state2 : reward, ...}, action : {foll_state1 : reward, foll_state2 : reward, ...} }
# R = {
# {
#  'a0':
#   {'s0': {'s0': -2, 's1': 5, 's2': -2},
#    's1': {'s0': -4, 's1': -1, 's2': -5}, 
#    's2': {'s0': -3, 's1': 5, 's2': -5}
#   }, 
#  'a1':
#   {'s0': {'s0': 0, 's1': -3, 's2': -3},
#    's1': {'s0': -4, 's1': -5, 's2': 5}, 
#    's2': {'s0': -4, 's1': 5, 's2': -1}
#   }
#  }
# }
def generate_rewards_update(states, actions):
    return {action : {state : {state : random.randint(-5, 5) for state in states} for state in states} for action in actions}


# Probabilities that action a in state s at time t will lead to state s' at time t+1
# state : { action : {following state : probability}}
# P = {
#       's0' : {'a0' : { 's0' : 0.75, 's1' : 0.2, 's2' : 0.05},
#               'a1' : { 's0' : 0.3, 's1' : 0.2, 's2' : 0.5}
#               'a2' : { 's0' : 0.9, 's1' : 0.05, 's2' : 0.05}
#       }
#       's1' : {'a0' : { 's0' : 0.0, 's1' : 0.2, 's2' : 0.8},
#              { 'a1' : { ... }}
#       }
#     }
def gen_values_for_prob(states, actions):
    # number of needed prob values = states * actions * states
    # number of states => number of prob values for each action - 'a0' : { 's0' : 0.75, 's1' : 0.2, 's2' : 0.05}
    prob_values = []
    for state in states:
        for action in actions: # From each state we can activate each action
            total_prob = 0
            prob_val_action = [] 
            for state in states[:-1]: # Exclude the last state, as it will be adjusted later
                prob = round(random.uniform(0, 1 - total_prob), 2)
                total_prob += prob
                prob_val_action.append(prob)
            # Adjust the probability of the last state to ensure the sum is exactly 1.0
            last_prob = round(1 - total_prob, 2)
            prob_val_action.append(last_prob)
            
            prob_values.append(prob_val_action)
    # print(prob_values)
    num_of_val = len(states) * len(actions) * len(states)

    # print("Correct number of prob_values in array?:", num_of_val == len(prob_values))
    # print(prob_values)
    return prob_values
    

# Probabilities that action a in state s at time t will lead to state s' at time t+1
# state : { action : {following state : probability}}
# P = {
#       's0' : {'a0' : { 's0' : 0.75, 's1' : 0.2, 's2' : 0.05},
#               'a1' : { 's0' : 0.3, 's1' : 0.2, 's2' : 0.5}
#               'a2' : { 's0' : 0.9, 's1' : 0.05, 's2' : 0.05}
#       }
#       's1' : {'a0' : { 's0' : 0.0, 's1' : 0.2, 's2' : 0.8},
#              { 'a1' : { ... }}
#       }
#     }
def generate_prob(states, actions):
    prob_val = gen_values_for_prob(states, actions)
    prob_dict = {state : { action : {state : None for state in states} for action in actions } for state in states}
    action_number = 0
    for state in prob_dict:
        for action in prob_dict[state]:
            state_with_prob_number = 0
            for state_with_prob in prob_dict[state][action]:
                prob_dict[state][action][state_with_prob] = prob_val[action_number][state_with_prob_number]
                state_with_prob_number += 1
            action_number += 1
    # print(prob_dict)
    return prob_dict

# Go over to another state after selecting the action
def state_transition(P, current_state, chosen_action):
    prob_current_action = list(P[current_state][chosen_action].values())# Get probabilities for going over to another state from the current action
    following_states = list(P[current_state][chosen_action].keys())
    
    print("Probabilities of going to another state after", chosen_action, ":", prob_current_action)
    print("Possible following states:", following_states)

    # Go over to another state based on probability of certain action
    next_state = random.choices(following_states, weights = prob_current_action)[0]
    print("Next state:", next_state)

    # print("Based on probability chosen next state:", next_state, '\n')

    return next_state