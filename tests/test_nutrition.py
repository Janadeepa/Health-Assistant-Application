import unittest
from app.routes.nutrition import get_nutrition_plan

class TestNutrition(unittest.TestCase):
    def test_get_nutrition_plan(self):
        # Test that get_nutrition_plan returns a nutrition plan
        user_id = 1
        plan = get_nutrition_plan(user_id)
        self.assertIsInstance(plan, dict)

if __name__ == '__main__':
    unittest.main()
