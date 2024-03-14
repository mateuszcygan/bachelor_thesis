import mdp_obj.mdp as mdp
import mdp_obj.print_mdp as print_mdp
import mdp_obj.mdp_files_generator as mfg

import policies.random_policy as rp

import policies.iteration_value as it
import policies.iteration_value_finite_horizon as finite_horizon

import mdp_obj.dense_sparse as ds

mdp_obj = mdp.createMDP()
V_obj, policy_obj, iterations_obj = it.value_iteration(mdp_obj)
V_finite_obj, policy_finite_obj = finite_horizon.value_iteration(mdp_obj, 80)

print("Number of iterations:", iterations_obj)
print_mdp.print_value_function(policy_obj)
print("Value function:")
print_mdp.print_value_function(V_obj)
print("\n")
print("Policy with finite horizon:")
print_mdp.print_value_function(policy_finite_obj)
print("Value function with finite horizon:")
print_mdp.print_value_function(V_finite_obj)
print("\n")

print("Before")
ds.unreachable_states(mdp_obj)
print("\n")

print("After")
ds.sparse_mdp_states(mdp_obj, 0.6)
ds.unreachable_states(mdp_obj)
print("\n")


print("Probabilities:")
print_mdp.print_mdp_details(mdp_obj.probabilities)
ds.sparse_mdp_rewards(mdp_obj, 0.25)
print("Rewards:")
print_mdp.print_mdp_details(mdp_obj.rewards)










