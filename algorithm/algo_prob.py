import random
import copy
from mdp_obj import mdp
from mdp_obj import print_mdp


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
    states_hits = {s : { a : {s : 0 for s in S} for a in A } for s in S}

    prob_denominator = len(S) # Denominator for calculating probabilities

    # Initially all probabilities for transitioning to other state are equal
    initial_prob = 1/prob_denominator
    approximated_prob = copy.deepcopy(P)

    # Set all transition probabilities to initial probability
    for state in approximated_prob:
        for action in approximated_prob[state]:
            for next_state in approximated_prob[state][action]:
                approximated_prob[state][action][next_state] = initial_prob

    current_state = 's0' # Start at state 's0'

    for _ in range(100000):
        # Retreive which action should be executed as a next one
        action_to_execute_index = state_actions[current_state]["iteration_num"] % state_actions[current_state]["actions_num"]
        executed_action = state_actions[current_state]["actions"][action_to_execute_index]

        state_actions[current_state]["iteration_num"]+=1 # Increase the iteration number of the current state

        # Get probabilities of transitioning to other states (needed for transition execution)
        states_prob = mdp.get_foll_states_prob_values(P, current_state, executed_action)
        next_state = random.choices(S, weights = states_prob)[0]

        # Mark state to which transition took place
        states_hits[current_state][executed_action][next_state]+=1
    
        # Calculate new approximation of probabilities
        hits_list = list(states_hits[current_state][executed_action].values())  
        hits_num = sum(hits_list) # Sum how many states changes took place for a certain state after executing a certain action
        
        for state in S:
            approximated_prob[current_state][executed_action][state] = (1 + states_hits[current_state][executed_action][state]) / (prob_denominator + hits_num)
    
        current_state = next_state

    print_mdp.print_mdp_details(approximated_prob)
    return approximated_prob


    
    

