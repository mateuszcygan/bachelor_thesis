import mdp
import print_mdp
import random

# random_policy(policy_mdp, 5)

# Expected value policy
# Multiply rewards with probabilities
# Choose the action with bigger expected value
# should be executed with rewards set generated from "generate_rewards_update"
#
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
#

def expected_value_policy(mdp_object, tran_num):

    rewards_sum = 0
    current_state = 's0' # Start from s0

    A = mdp_object.get_actions()
    S = mdp_object.get_states()
    R = mdp_object.get_rewards()
    P = mdp_object.get_probabilities()

    # print("Actions: ", A)
    # print("States: ", S)
    # print("Rewards: ")
    # print_mdp.print_prob_details(R)
    # print("Probabilities: ")
    # print_mdp.print_prob_details(P)

    expected_value = 0
    # expected_values_actions = [] # Array that stores expected values of each actions executed from current state

    # From each action possible to go to each state with different reward and probability
    # States are inside rewards after each action (therefore state in second loop)
    # We need probabilities only for current state (to go over to other states) - state is the outer value in two dictionaries
    next_action = A[0] # Initially assign first action from set with actions

    for _ in range(0, tran_num):
        max_exp_val = float('-inf')

        for action in A: # Calculate expected value for each action
            print("\nGoing over into another action")
            for state in S: # From each action it is possible to go over to all of the states
                print("Iteration through: ", action, state)
                print(R[action][current_state][state])
                print(P[current_state][action][state])
                expected_value += R[action][current_state][state] * P[current_state][action][state]
            # Compare the expected value of the current action from loop with the present biggest expected value
            print("Expected value: ", expected_value, "from action", action)
            if max_exp_val < expected_value:
                max_exp_val = expected_value
                next_action = A[A.index(action)]
                print("next action: ", next_action)
        print("Max expected value: ", max_exp_val, "from action", next_action)

        # After calculating the expected value, execute the chosen action
        # Set with probabilities is needed
        
            
    return

# Compare random with expected value policy
mdp_updated = mdp.createMDPupdated();
# print(mdp_updated.get_actions())
# print(mdp_updated.get_states())
# print(mdp_updated.get_rewards())
# print(mdp_updated.get_probabilities())

# expected_value_policy(mdp_updated, 2)

def value_iteration(mdp_object, tran_num=float('inf')):

    S, A, R, P = mdp_object.get_properties() # Extract all properties of MDP
    dicount_factor = 0.9 # Define dicount factor [0,1]

    current_state = 's0' # Start from state 's0'
    rewards_sum = 0



value_iteration(mdp_updated)