 
import mdp
import pickle 
import print_mdp

# Solution from: https://stackoverflow.com/questions/4529815/saving-an-object-data-persistence

def save_object(obj, filename):
    with open(filename, 'wb') as outp:  # Overwrites any existing file.
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

def saved_mdp_prop(filename):
    with open(filename, 'rb') as inp:
          mdp = pickle.load(inp)
          S = mdp.states
          A = mdp.actions
          R = mdp.rewards
          P = mdp.probabilities
          return S, A, R, P








