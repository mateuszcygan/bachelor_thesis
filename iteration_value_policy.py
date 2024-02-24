import mdp
import print_mdp as p
import auxiliary_functions as aux
import mdp_sets
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

def value_iteration(mdp_object):

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
    V_old = [0 for _ in range(len(S))]  # Array with value function values
    V_new = [0 for _ in range(len(S))] # Array needed to check the convergence
    # print("Value function:", V, "for states", S)
    i = 0
    while True:
        print("Iteration number: ", i)
        Vi_next = [] # Array for all computable values from certain state (number of values dependent on possible actions)
        
        # Possible actions to execute from current state (needed in cases where not each action executable from a state)
        poss_actions = mdp.get_possible_actions(P, current_state)
        print("Possible action from current state", current_state, ":", poss_actions)

        for action in poss_actions:
            V_action = 0 # Value of value function for action

            foll_states = mdp.get_following_states(R, action, current_state)

            prob_foll_states = mdp.get_foll_states_prob_values(P, current_state, action) # Pa(s, s')
            print("Probabilities going over to following states through an current action: ", prob_foll_states)

            rewards_foll_states = mdp.get_foll_states_rewards_values(R, action, current_state) # Ra(s, s')
            print("Rewards going over to following states through an current action: ", rewards_foll_states)

            # Access all required components for (Ra(s,s') + discount_factor*Vi(s'))

            ## Access Vi(s') for following states
            foll_states_indexes = [int(s[1:]) for s in foll_states] # Extract indexes of following states
            print("Indexes of following states: ", foll_states_indexes)

            

            Vi_following_states = [] # Vi(s') - value function for following states
            for index in foll_states_indexes:
                Vi_following_states.append(V_old[index])
            
            discounted_rewards = [reward + dicount_factor*Vi_following_state for reward, Vi_following_state in zip(rewards_foll_states, Vi_following_states)] #discount_factor*Vi(s')
            print("Discounted rewards: ", discounted_rewards)

            # Vi_components - list with calculation Pa(s,s')(Ra(s,s') + discount_factor*Vi(s')) for each following state
            Vi_components = [prob_foll_state * discounted_reward for prob_foll_state, discounted_reward in zip(prob_foll_states, discounted_rewards)] # Pa(s,s')(Ra(s,s') + discount_factor*Vi(s'))
            possible_Vi = sum(Vi_components) # Calculate sum(Pa(s,s')(Ra(s,s') + discount_factor*Vi(s')))
            Vi_next.append(possible_Vi)
            print("Array of new possible value functions: ", Vi_next)
            print('\n')
        
        # Assign new value of value function for current state
        current_state_index = int(current_state[1:])
        print("Current state index:", current_state_index)
        V_new[current_state_index] = max(Vi_next)
        print("New value function:", V_new)

        # Termination condition
        print("Old value function:", V_old)
        if (all( abs(V_o - V_n) < 0.0001 for V_o, V_n in zip(V_old, V_new))):
            print("Number of iterations: ", i)
            return V_new
        
        V_old = V_new.copy()
        print("Old value function without convergance: ", V_old)

        # Choose next action
        next_action_index = aux.find_max_index(Vi_next)
        next_action = poss_actions[next_action_index]
        print(next_action)


        next_state = mdp_sets.state_transition(P, current_state, next_action) # Go over to another state through chosen action

        rewards_sum += R[next_action][current_state][next_state] # Update the reward's value
        print("Rewards: ", rewards_sum)
    
        current_state = next_state # Update the current state
        i+=1
        
x = value_iteration(mdp_updated)
print("Value iteration array: ", x)