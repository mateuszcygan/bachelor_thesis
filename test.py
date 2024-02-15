import random

# Data structure 
# 's1': {
#         'a': {'foll_state': 's1', 'reward': 4, 'probability': 0.75},
#         'b': {'foll_state': 's3', 'reward': 2, 'probability': 0.2},
#         'c': {'foll_state': 's7', 'reward': 9, 'probability': 0.05}
#     }

#         'a': {'foll_state': 's1', 'reward': 4, 'probability': 0.75},
#         'b': {'foll_state': 's3', 'reward': 2, 'probability': 0.2},
#         'c': {'foll_state': 's7', 'reward': 9, 'probability': 0.05}

keys = ['foll_state', 'reward', 'probability']
actions = ['a', 'b', 'c']
def create_transition(state, actions, keys):
    return {state : {action : { key : None for key in keys} for action in actions}}

tran = create_transition('s1', actions, keys)

for state, actions_dict in tran.items():
    print(state)
    for action, properties in actions_dict.items():
        print(action, ":", properties)

# def create_dictionary(state, actions)
        
ex_dict = {'brand' : 'Ford',
           'year' : '1999',
           'model' : 'Mustang'}
print(tran.items())