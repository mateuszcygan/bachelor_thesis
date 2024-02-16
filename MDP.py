import random

# Data structure representing transitions
# {
#   's1': {
#         'a': {'foll_state': 's1', 'reward': 4, 'probability': 0.75},
#         'b': {'foll_state': 's3', 'reward': 2, 'probability': 0.2},
#         'c': {'foll_state': 's7', 'reward': 9, 'probability': 0.05}
#     }
# }

def create_transitions(state, actions, keys):
    return {state : {action : { key : None for key in keys} for action in actions}}

def print_transition_details(transition_dict):
    for state, actions_dict in transition_dict.items():
        print(state)
        for action, properties in actions_dict.items():
            print(action, ":", properties)

def createMDP():

    # Define MDP 
    states = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']

    actions = ['a', 'b', 'c']

    transition_keys = ['foll_state', 'reward', 'probability']

    # Generate random transitions
    transitions = {}

    for state in states:
        transition = create_transitions(state, actions, transition_keys)
        total_prob = 0
        # Generate a random following state and a random reward
        for action in actions:
            transition[state][action]['foll_state'] = random.choice(states)
            transition[state][action]['reward'] = random.randint(-10, 10)
        for action in actions[:-1]:  # Exclude the last action, as it will be adjusted later
            # Generate a random probability with two decimal places
            prob = round(random.uniform(0, 1 - total_prob), 2)
            total_prob += prob
            transition[state][action]['probability'] = prob
        # Adjust the probability of the last action to ensure the sum is exactly 1.0
        prob_c = round(1 - total_prob, 2)
        transition[state]['c']['probability'] = prob_c
        transitions.update(transition)
    return transitions

