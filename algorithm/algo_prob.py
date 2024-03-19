import random
from mdp_obj import mdp


def learn_probabilities(mdp_object):

    # The structure of MDP is known
    A = mdp_object.actions
    S = mdp_object.states
    P = mdp_object.probabilities # Probabilities needed for changing between transitions

    # Needed for choosing actions that should be executed
    state_actions = {s : 
                        {"iteration_num" : 0, 
                         "actions_num" : None, 
                         "actions" : None} for s in S}
 
    # Create dictionary that stores number of possible actions and possible actions in an array
    for state in S:
        state_actions[state]["actions_num"] = len(list(P[state].keys()))
        state_actions[state]["actions"] = list(P[state].keys())
    
    # for state in S:
    #     print(state)
    #     print("actions_num:", state_actions[state]["actions_num"])
    #     print("actions:", state_actions[state]["actions"])
    #     print("\n")
        
    # Store how many times a transition to a certain state took place
    states_hits = {s : {s : 0 for s in S} for s in S}

    prob_denominator = len(S) # Denominator for calculating probabilities

    # Initially all probabilities for transitioning to other state are equal
    initial_prob = 1/prob_denominator
    approximated_prob = {s : {s : initial_prob for s in S} for s in S}



    current_state = 's0' # Start at state 's0'

    for _ in range(200):
        # Retreive which action should be executed as a next one
        action_to_execute_index = state_actions[current_state]["iteration_num"] % state_actions[current_state]["actions_num"]
        executed_action = state_actions[current_state]["actions"][action_to_execute_index]

        state_actions[current_state]["iteration_num"]+=1 # Increase the iteration number of the current state

        # Get probabilities of transitioning to other states (needed for transition execution)
        states_prob = mdp.get_foll_states_prob_values(P, current_state, executed_action)
        next_state = random.choices(S, weights = states_prob)[0]

        # Mark state to which transition took place
        states_hits[current_state][next_state]+=1
    
        # Calculate new approximation of probabilities
        for state in S:
            approximated_prob[current_state][state] = (1 + states_hits[current_state][state]) / (prob_denominator + state_actions[current_state]["iteration_num"])
    
        current_state = next_state

    
    

