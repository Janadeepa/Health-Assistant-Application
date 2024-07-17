import unittest
from app.routes.mental_health import get_mental_health_resources

class TestMentalHealth(unittest.TestCase):
    def test_get_mental_health_resources(self):
        # Test that get_mental_health_resources returns a list of mental health resources
        resources = get_mental_health_resources()
        self.assertIsInstance(resources, list)

if __name__ == '__main__':
    unittest.main()
