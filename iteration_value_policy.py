import mdp

mdp_updated = mdp.createMDPupdated()

def value_iteration(mdp_object, tran_num=float('inf')):

    S, A, R, P = mdp_object.get_properties() # Extract all properties of MDP
    dicount_factor = 0.9 # Define dicount factor [0,1]

    current_state = 's0' # Start from state 's0'
    rewards_sum = 0



value_iteration(mdp_updated)