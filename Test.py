import unittest
from action import Action
from world import World
from agent import Agent

class Test(unittest.TestCase):

    # Action Tests
    def test_action_attr(self):
        A = Action("0:1 0 0.5 1 0.5")
        print(A)
        self.assertEqual(A.id, 1)
        self.assertEqual(A.probs, {0: 0.5, 1: 0.5})

    def test_action_eq(self):
        A1 = Action("0:1 0 0.5 1 0.5")
        A2 = Action("0:1 1 0.5 0 0.5")
        A3 = Action("0:1 1 0.5 2 0.5")
        self.assertEqual(A1, A2)
        self.assertNotEqual(A1, A3)

    # Agent Tests
    def test_agent_arrays(self):
        w = World("test_input.txt")
        a = Agent(w)
        self.assertEqual(len(a.count), 2)
        self.assertEqual(len(a.count[0]), 2)
        self.assertEqual(len(a.count[1]), 2)

if __name__ == "__main__":
    unittest.main()
