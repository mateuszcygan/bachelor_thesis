import mdp
import print_mdp
    
test_R, test_P = mdp.createMDP()
# print_rewards_details(test_R)

print_mdp.print_rewards_details(test_R)
print_mdp.print_prob_details(test_P)
