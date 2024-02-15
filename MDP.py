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


# Define MDP
states = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']

actions = ['a', 'b', 'c']

transition_keys = ['foll_state', 'reward', 'probability']

# Generate random transitions
transitions = {}

for state in states:
    transition = create_transitions(state, actions, transition_keys)
    for action in actions:
        transition[state][action]['foll_state'] = random.choice(states)
    print_transition_details(transition)




#     possible_actions = random.sample(actions, k=random.randint(1, len(actions))) #randomly select actions
#     #randint(start, end)
#     #returns random integer in range [start, end], end points included
#     #random.sample(sequence, k)
#     #returns k length new list of elements chosen from the sequence

#     #print(possible_actions)
#     for poss_action in possible_actions:
#         transition = create_dictionary(state, transition_keys)
#         transition[state]['action'] = poss_action
#         transition[state]['foll_state'] = random.choice(states)
#         transition[state]['reward'] = random.randint(0, 10)
#         transitions.append(transition)

# print(*transitions, sep="\n")
    

