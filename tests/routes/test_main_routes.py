"""
Tests for main routes.
"""

import unittest
from app import create_app, db


class TestMainRoutes(unittest.TestCase):
    """
    Test case for main routes.
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

    def test_index_route(self):
        """
        Test the index route.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, this is the main route", response.data)


if __name__ == '__main__':
    unittest.main()