import random

# Function that outputs the number of states with a probability of 0.0 (indicating unreachable states)
def unreachable_states(mdp_object):

    states = mdp_object.states
    actions = mdp_object.actions
    P = mdp_object.probabilities

    poss_states_transitions = len(states)*len(states)*len(actions)

    unreachable_overall = 0

    for s in states:
        for a in actions:
            prob_values = list(P[s][a].values())
            unreachable = 0
            for prob_value in prob_values:
                if prob_value == 0.0:
                    unreachable += 1
            # print("Unreachable states:", unreachable)
            unreachable_overall += unreachable

    print("tran_to_other_states(incl prob=0):", poss_states_transitions)
    print("unreach_states(prob=0):", unreachable_overall)
    
    unreachable_percentage = unreachable_overall/poss_states_transitions
    print("percent_of_unreach_states:", unreachable_percentage)

# For states without following actions (all probabilities are set to zero) randomly choose one following state
def random_following_state(mdp):

    S = mdp.states
    A = mdp.actions
    P = mdp.probabilities

    for current_state in S:
        for action in A:
            transition_prob = list(P[current_state][action].values())

            # If all probabilities are zero (no following state), choose randomly one action and assign probability 1.0 to it
            if sum(transition_prob) == 0:
                random_state = random.choice(S)
                P[current_state][action][random_state] = 1.0

# Normalizing probabilities for following states of a certain MDP
def normalize_mdp_probabilities(mdp):

    S = mdp.states
    A = mdp.actions
    P = mdp.probabilities

    for current_state in S:
        for action in A:

            # Calculate the total value of probabilities for certain action
            action_prob = list(P[current_state][action].values())
            total = sum(action_prob)

            for foll_state in S:

                # Normalize the probability of following states
                try:
                    P[current_state][action][foll_state] = P[current_state][action][foll_state]/total
                except ZeroDivisionError:
                    P[current_state][action][foll_state] = 0

# Thinning the reachable states in the MDP by using state_sparsity_rate - percentage of states that should be unreached
def sparse_mdp_states(mdp, state_sparsity_rate):

    S = mdp.states
    A = mdp.actions
    P = mdp.probabilities
    
    old_probability_weight = 1 - state_sparsity_rate
    sparsity_weights = [state_sparsity_rate, old_probability_weight] # Sparse weights for 0.0 probability and probability of going over to following state

    for current_state in S:
        for action in A:
            for following_state in S:

                possible_prob_values = [0.0]  # Array containing 0.0 probability and probability of transitioning to following state (used for decision-making)
                prob_value = P[current_state][action][following_state]

                # If any of the following states is already unreachable, don't change it
                if prob_value == 0:
                    continue

                possible_prob_values.append(prob_value)

                # Choose between 0.0 and old probability of transitioning to following state
                new_prob_value = random.choices(possible_prob_values, weights = sparsity_weights)[0]
                P[current_state][action][following_state] = new_prob_value

    normalize_mdp_probabilities(mdp)
    random_following_state(mdp)

def sparse_mdp_rewards(mdp, reward_sparsity_rate):

    S = mdp.states
    A = mdp.actions
    R = mdp.rewards

    old_probability_weight = 1 - reward_sparsity_rate
    sparsity_weights = [reward_sparsity_rate, old_probability_weight] # Sparse weights for 0.0 reward and assigned reward

    for current_state in S:
        for action in A:
            for following_state in S:

                # possible_reward_values = [0]
                possible_reward_values = [0.0]  # Array containing 0.0 reward and assigned reward (used for decision-making) 
                reward_value = R[current_state][action][following_state]

                # If any of the following states is already unreachable, don't change it
                if reward_value == 0:
                    continue

                possible_reward_values.append(reward_value)

                # Choose between reward 0.0 and assigned reward
                new_reward_value = random.choices(possible_reward_values, weights = sparsity_weights)[0]
                R[current_state][action][following_state] = new_reward_value

def reduce_actions_number(mdp, min_num=1, max_num=None):

    """
    Reduce the number of possible actions for each state

    Args:
    - mdp: An object representing the MDP.
    - min_num: The minimum number of possible actions from a state. Defaults to 1.
    - max_num: The maximum number of possible actions from a state. If not specified, defaults to the total number of actions available in the MDP.

    Returns:

    Test: executable actions in rewards and probabilities for the same states are the same
    """

    # If max_num not defined, assign the value of possible states
    if max_num is None:
        max_num = len(mdp.actions)
    
    A = mdp.actions
    S = mdp.states
    R = mdp.rewards
    P = mdp.probabilities
    
    for state in S:

        actions_num = random.randint(min_num, max_num) # Randomly choose a number from a given interval (number of executable actions from certain state)
        random_actions = random.choices(A, k=actions_num) # Randomly choose actions that should be executable
        print("Randomly chosen executable actions:", random_actions)

        actions_to_delete = set(A) - set(random_actions) # Determine actions that should be deleted for certain state
        print("Actions to delete:", actions_to_delete)

        for action_to_delete in actions_to_delete:
            del R[state][action_to_delete]
            del P[state][action_to_delete]











    



