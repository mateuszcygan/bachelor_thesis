import mdp
import print_mdp
import random

policy_mdp = mdp.createMDP() # For later: implement function that gives states and actions from these two dictionaries back


# Random policy
# Based on selecting randomly action that should be executed
# 1. Select randomly action
# 2. Based on probabilities, transition to another state will be executed

def random_policy(mdp_object, tran_num):

    # Sets of which MDP is composed
    A = mdp_object.get_actions()

    
    current_state = 's0' # Start from s0
    for number in range(0, tran_num):
        next_action = random.choice(A)
        print(next_action)




# Define random_policy

# helpful function - random.choices
# mylist = ["apple", "banana", "cherry"]
# print(random.choices(mylist, weights = [10, 1, 1], k = 14))
# weights - weigh the possibility of each result with the weights parameter

# def random_policy(state):
#     actions = list(mdp1[state].keys())  # Get available actions for the given state
#     print(actions)
#     probabilities = [action_info['probability'] for action_info in mdp1[state].values()]  # Get probabilities
#     print(probabilities)
#     selected_action_index = random.choices(range(len(actions)), weights=probabilities)[0]  # Select action based on probabilities
#     return actions[selected_action_index]  # Return selected action

# Example usage
# current_state = 's1'
# selected_action = random_policy(current_state)
# print("Selected Action:", selected_action)
