import unittest
import mdp_sets

class TestMdpSets(unittest.TestCase):

    def setUp(self):
        self.states = mdp_sets.generate_states()
        self.actions = mdp_sets.generate_actions()

    def test_generate_states_non_empty(self):
        self.assertTrue(self.states)  # Assert that states is not empty

    def test_generate_states_type(self):
        self.assertIsInstance(self.states, list)  # Assert that states is a list

    def test_generate_actions_non_empty(self):
        self.assertTrue(self.actions)  # Assert that actions is not empty

    def test_generate_actions_type(self):
        self.assertIsInstance(self.actions, list)  # Assert that actions is a list

if __name__ == '__main__':
    unittest.main()