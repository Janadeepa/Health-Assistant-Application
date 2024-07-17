import unittest
from app.routes.health import health_monitoring, get_health_data

class TestHealth(unittest.TestCase):
    def test_health_monitoring(self):
        # Test that health monitoring returns a success response
        response = health_monitoring()
        self.assertEqual(response.status_code, 200)

    def test_get_health_data(self):
        # Test that get_health_data returns a list of health data
        health_data = get_health_data()
        self.assertIsInstance(health_data, list)

if __name__ == '__main__':
    unittest.main()
