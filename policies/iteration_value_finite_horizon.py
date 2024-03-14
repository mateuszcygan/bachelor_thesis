import mdp_obj.print_mdp as print_mdp 

def value_iteration(mdp_object, finite_horizon):

    # Extract MDP properties
    S, A, R, P = mdp_object.get_properties()

    dicount_factor = 0.9 # For comparisson
    # discount_factor = 1

    # Initialize the value for each state to 0
    V = {s : 0 for s in S}
    V_new = {s : 0 for s in S}
    policy = {s : None for s in S} # Dictionary that represents calculated policy

    iterations = range(finite_horizon) # Number of iterations
    i = 0


    for x in iterations:
        print("Value of x:", x)
        i += 1

        for current_state in S:

            actions_values = {action : 0 for action in A} # Dictionary with value for each action is a specific state

            for a in A:

                # Get probabilities and rewards for current state
                probabilities = list(P[current_state][a].values())
                rewards = list(R[current_state][a].values())

                # Calculate sum(Pa(s,s')(Ra(s,s') + dicount_factor*V_i(s')))
                value = sum([prob * (reward + dicount_factor * V[current_state]) for prob, reward in zip(probabilities, rewards)])
                actions_values[a] = value
            
            print("Calculated values for state", current_state, ":", actions_values)

            # Find the biggest value and its action
            max_value = max(list(actions_values.values()))
            biggest_value_action = list(actions_values.keys())[list(actions_values.values()).index(max_value)]

            policy[current_state] = biggest_value_action # Set the action with the biggest value as the policy action from current state

            V_new[current_state] = max_value # Set maximum of calculated values as a new value for current_state

            print("Old value function:")
            print_mdp.print_value_function(V)
            print('\n')
            print("New value function:")
            print_mdp.print_value_function(V_new)
            print("\n")

            V = V_new.copy()
        
    return V_new, policy