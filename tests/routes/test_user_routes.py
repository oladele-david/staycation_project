"""
Tests for user routes.
"""

import unittest
from app import create_app, db


class TestUserRoutes(unittest.TestCase):
    """
    Test case for user routes.
    """

    def setUp(self):
        """
        Set up test variables and initialize the app.
        """
        self.app = create_app()
        self.app.config.from_mapping({
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'TESTING': True,
        })

        with self.app.app_context():
            db.create_all()
            self.client = self.app.test_client()

    def tearDown(self):
        """
        Clean up after each test.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_users(self):
        """
        Test the get users route.
        """
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"List of users", response.data)


if __name__ == '__main__':
    unittest.main()
    