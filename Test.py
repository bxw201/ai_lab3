import unittest
from Action import Action

class Test(unittest.TestCase):

    def test_action_attr(self):
        A = Action("0:1 0 0.5 1 0.5")
        print(A)
        self.assertEqual(A.id, 1)
        self.assertEqual(A.probs, {0: 0.5, 1: 0.5})
    
    def test_action_eq(self):
        A1 = Action("0:1 0 0.5 1 0.5")
        A2 = Action("0:1 1 0.5 0 0.5")
        A3 = Action("0:1 1 0.5 2 0.5")
        print(f"A1 - {A1}")
        print(f"A2 - {A2}")
        print(f"A3 - {A3}")
        self.assertEqual(A1, A2)
        self.assertNotEqual(A1, A3)

if __name__ == "__main__":
    unittest.main()