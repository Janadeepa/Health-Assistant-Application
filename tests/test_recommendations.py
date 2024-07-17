import unittest
from app.routes.recommendations import get_recommendations

class TestRecommendations(unittest.TestCase):
    def test_get_recommendations(self):
        # Test that get_recommendations returns a list of recommendations
        recommendations = get_recommendations()
        self.assertIsInstance(recommendations, list)

    def test_get_recommendations_with_user_id(self):
        # Test that get_recommendations returns a list of recommendations for a specific user
        user_id = 1
        recommendations = get_recommendations(user_id)
        self.assertIsInstance(recommendations, list)

if __name__ == '__main__':
    unittest.main()
