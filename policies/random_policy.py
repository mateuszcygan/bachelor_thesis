import mdp_obj.mdp as mdp
import random

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
    S, A, R, P = mdp_object.get_properties()

    current_state = 's0' # Start from s0
    rewards_sum = 0

    for _ in range(0, tran_num): # Use _ as a placeholder for the loop variable

        print("curr_state:", current_state)

        executed_action = random.choice(A) # Randomly choose action from A
        print("random_action:", executed_action)

        states_weights = mdp.get_foll_states_prob_values(P, current_state, executed_action) # Extract probabilities for following states
        print("tran_prob", current_state, ":", states_weights)

        # Go over to another state based on transition probabilities
        next_state = random.choices(S, weights = states_weights)[0]
        print("next_state (prob based):", next_state, '\n')

        reward = R[current_state][executed_action][next_state]
        rewards_sum += reward

        print("reward:", reward)
        print("collected_rewards:", rewards_sum)

        current_state = next_state

    return rewards_sum