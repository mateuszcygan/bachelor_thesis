import mdp
import random

mdp1 = mdp.createMDP()
# print(mdp1)
mdp.print_transition_details(mdp1)

# Define random_policy

# helpful function - random.choices
# mylist = ["apple", "banana", "cherry"]
# print(random.choices(mylist, weights = [10, 1, 1], k = 14))
# weights - weigh the possibility of each result with the weights parameter

def random_policy(state):
    actions = list(mdp1[state].keys())  # Get available actions for the given state
    print(actions)
    probabilities = [action_info['probability'] for action_info in mdp1[state].values()]  # Get probabilities
    print(probabilities)
    selected_action_index = random.choices(range(len(actions)), weights=probabilities)[0]  # Select action based on probabilities
    return actions[selected_action_index]  # Return selected action

# Example usage
current_state = 's1'
selected_action = random_policy(current_state)
print("Selected Action:", selected_action)
