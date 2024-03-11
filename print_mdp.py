def print_mdp_details(prob_dict):
    for state, action_prob_dict in prob_dict.items():
        print(state)
        for action, prob in action_prob_dict.items():
            print(action, ":", prob)
        print('\n')