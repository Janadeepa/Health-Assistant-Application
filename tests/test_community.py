import unittest
from app.routes.community import get_community_posts

class TestCommunity(unittest.TestCase):
    def test_get_community_posts(self):
        # Test that get_community_posts returns a list of community posts
        posts = get_community_posts()
        self.assertIsInstance(posts, list)

if __name__ == '__main__':
    unittest.main()
