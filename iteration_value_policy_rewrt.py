import mdp
import print_mdp as p
import mdp_files_generator as mfg
import iteration_value_policy as ivp

def print_value_function(V):
    for state, value in V.items():
        print(state, ":", value)


def value_iteration(mdp_object):

    # Extract MDP properties
    S, A, R, P = mdp_object.get_properties() # Extract all properties of MDP
    print("States: ", S)
    print("Actions: ", A)
    print("Rewards: ")
    p.print_prob_details(R)
    print("Probabilities: ")
    p.print_prob_details(P)

    dicount_factor = 0.9

    # Initialize the value for each state to 0
    V = {s : 0 for s in S}
    V_new = {s : 0 for s in S}

    i = 0
    while True:
        for current_state in S:

            values = []
            for a in A:
                # Get probabilities and rewards for current state
                probabilities = list(P[current_state][a].values())
                rewards = list(R[a][current_state].values())

                # Calculate sum(Pa(s,s')(Ra(s,s') + dicount_factor*V_i(s')))
                value = sum([prob * (reward + dicount_factor * V[current_state]) for prob, reward in zip(probabilities, rewards)])
                values.append(value)
            
            print("Calculated values for state", current_state, ":", values)
            V_new[current_state] = max(values) # Set maximum of calculated values as a new value for current_state
            i += 1
            print("Iteration number", i, "\n")

            # Termination condition
            print("Old value function:")
            print_value_function(V)
            print('\n')
            print("New value function:")
            print_value_function(V_new)
            print("\n")
            if (all( abs(V[s] - V_new[s]) < 0.0001 for s in S)):
                print("Number of iterations: ", i)
                return V_new
            V = V_new.copy()

# mdp_object = mdp.createMDPupdated()
# value_iteration(mdp_object)

mdp_updated = mfg.read_saved_mdp("mdp_object.pkl")

y = value_iteration(mdp_updated)
x = ivp.value_iteration(mdp_updated)
print(x)
print(y)
