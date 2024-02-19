def print_rewards_details(rewards_dict):
    for state, actions_dict in rewards_dict.items():
        print(state, ":", actions_dict)
    print('\n')

def print_prob_details(prob_dict):
    for state, action_prob_dict in prob_dict.items():
        print(state)
        for action, prob in action_prob_dict.items():
            print(action, ":", prob)
        print('\n')