import mdp
import print_mdp

#Rewards
R = {'s0': {'a0': 3, 'a1': -3}, 's1': {'a0': 5, 'a1': 4}, 's2': {'a0': 2, 'a1': 2}} 

print(R['s0']['a0'])

mdp_obj = mdp.createMDP()
print(mdp_obj.get_rewards(), '\n')
print(mdp_obj.get_probabilities(), '\n')
