import unittest
from app.routes.fitness import get_fitness_plan

class TestFitness(unittest.TestCase):
    def test_get_fitness_plan(self):
        # Test that get_fitness_plan returns a fitness plan
        user_id = 1
        plan = get_fitness_plan(user_id)
        self.assertIsInstance(plan, dict)

if __name__ == '__main__':
    unittest.main()
