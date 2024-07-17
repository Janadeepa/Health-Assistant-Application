import unittest
from app.routes.alerts import create_alert, get_alerts

class TestAlerts(unittest.TestCase):
    def test_create_alert(self):
        # Test that create_alert creates a new alert
        alert_data = {'message': 'Test alert', 'user_id': 1}
        response = create_alert(alert_data)
        self.assertEqual(response.status_code, 201)

    def test_get_alerts(self):
        # Test that get_alerts returns a list of alerts
        alerts = get_alerts()
        self.assertIsInstance(alerts, list)

if __name__ == '__main__':
    unittest.main()
