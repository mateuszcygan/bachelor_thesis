import mdp
import print_mdp as p
import mdp_files_generator as mdp_file
import dense_sparse as ds

mdp_object = mdp.createMDPupdated()

S = mdp_object.get_states()
A = mdp_object.get_actions()
R = mdp_object.get_rewards()
P = mdp_object.get_probabilities()

print('\n')
print("States: ", S)
print('\n')
print("Actions: ", A)
print('\n')
print("Rewards: ")
p.print_prob_details(R)
print("Probabilities set: ")
p.print_prob_details(P)

ds.unreachable_states(mdp_object)

ds.sparse_mdp_states(mdp_object, 0.5)

p.print_prob_details(mdp_object.probabilities)
ds.unreachable_states(mdp_object)
