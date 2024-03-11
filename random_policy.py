import mdp
import print_mdp as p
import random

policy_mdp = mdp.createMDP()


# Random policy
# Based on selecting randomly action that should be executed
# 1. Select randomly action
# 2. Based on probabilities, going over to another state will be executed

def random_policy(mdp_object, tran_num):
    """
    Implement a random policy for a Markov Decision Process (MDP).

    Args:
    - mdp_object: An object representing the MDP.
    - tran_num: The number of transitions to simulate.

    Returns:
    - rewards_sum: The sum of rewards collected during transitions.
    """

    # Sets of which MDP is composed (replace with new function that is already implemented)
    A = mdp_object.get_actions()
    S = mdp_object.get_states()
    R = mdp_object.get_rewards()
    P = mdp_object.get_probabilities()

    # Prints of MDP components (Delete)
    print(A, '\n')
    print(S, '\n')
    # print(R, '\n')
    # print(P, '\n')
    p.print_rewards_details(R)
    p.print_prob_details(P)

    
    current_state = 's0' # Start from s0
    rewards_sum = 0
    for _ in range(0, tran_num): # Use _ as a placeholder for the loop variable
        print("Current state:", current_state)

        current_action = random.choice(A) # Randomly choose action from A
        print("Randomly choosed action: ", current_action)

        print("Reward of taking current action:", R[current_state][current_action])
        rewards_sum += R[current_state][current_action] # Sum the collected rewards
        print("Collected rewards so far:", rewards_sum)

        prob_current_action = [P[current_state][current_action][state] for state in P]# Get probabilities for going over to another state from the current action
        print("Probabilities of going to another state after", current_action, ":", prob_current_action)

        # Go over to another state based on probability of certain action
        next_state = random.choices(S, weights = prob_current_action)[0] # [0] - return type is an array
        print("Based on probability chosen next state:", next_state, '\n')

        current_state = next_state

    return rewards_sum

random_policy(policy_mdp, 5)