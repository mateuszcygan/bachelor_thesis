import mdp
import print_mdp as p
# import numpy as np

# R = {
# {
#  'a0':
#   {'s0': {'s0': -2, 's1': 5, 's2': -2},
#    's1': {'s0': -4, 's1': -1, 's2': -5}, 
#    's2': {'s0': -3, 's1': 5, 's2': -5}
#   }, 
#  'a1':
#   {'s0': {'s0': 0, 's1': -3, 's2': -3},
#    's1': {'s0': -4, 's1': -5, 's2': 5}, 
#    's2': {'s0': -4, 's1': 5, 's2': -1}
#   }
#  }
# }
# 
# P = {
#       's0' : {'a0' : { 's0' : 0.75, 's1' : 0.2, 's2' : 0.05},
#               'a1' : { 's0' : 0.3, 's1' : 0.2, 's2' : 0.5}
#               'a2' : { 's0' : 0.9, 's1' : 0.05, 's2' : 0.05}
#       }
#       's1' : {'a0' : { 's0' : 0.0, 's1' : 0.2, 's2' : 0.8},
#              { 'a1' : { ... }}
#       }
#     }

mdp_updated = mdp.createMDPupdated()

def value_iteration(mdp_object, tran_num=float('inf')):

    S, A, R, P = mdp_object.get_properties() # Extract all properties of MDP
    print("States: ", S)
    print("Actions: ", A)
    print("Rewards: ")
    p.print_prob_details(R)
    print("Probabilities: ")
    p.print_prob_details(P)
    

    dicount_factor = 0.9 # Define dicount factor, range: [0,1]

    current_state = 's0' # Start from state 's0'
    rewards_sum = 0

    # Define initial value function value
    V = [0 for _ in range(len(S))]  # Array with value function values
    print("Value function:", V, "for states", S)

    for _ in range(0, 1):
        Vi_next = [] # Array for all computable values from certain state (number of values dependent on possible actions)
        
        # Possible actions to execute from current state (needed in cases where not each action executable from a state)
        actions_from_curr_state = [action_key for action_key in P[current_state].keys()]
        print("Actions possible from ", current_state, ":", actions_from_curr_state)

        for action in actions_from_curr_state:
            V_action = 0 # Value of value function for action
            # Possible following states from action (needed in cases where not from each action going over to each state possible)
            foll_states = [foll_state for foll_state in P[current_state][action].keys()]
            print("Following states from current action", action, ":", foll_states)

            prob_foll_states = [P[current_state][action][s] for s in P[current_state][action]] # Pa(s, s')
            print("Probabilities going over to following states through an current action: ", prob_foll_states)

            rewards_foll_states = [R[action][current_state][foll_state] for foll_state in R[action][current_state]]
            print("Rewards going over to follwing states through an current action: ", rewards_foll_states)





            
    return

        


value_iteration(mdp_updated)