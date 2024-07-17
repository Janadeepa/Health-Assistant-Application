import unittest
from app.routes.records import get_medical_records

class TestRecords(unittest.TestCase):
    def test_get_medical_records(self):
        # Test that get_medical_records returns a list of medical records
        user_id = 1
        records = get_medical_records(user_id)
        self.assertIsInstance(records, list)

if __name__ == '__main__':
    unittest.main()
