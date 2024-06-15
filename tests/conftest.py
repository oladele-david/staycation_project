"""
Shared fixtures for testing.
"""

import unittest
from app import create_app, db


class BaseTestCase(unittest.TestCase):
    """
    A base test case for the application.
    """

    def setUp(self):
        """
        Set up the test client and database before each test.
        """
        self.app = create_app()
        self.app.config.from_mapping({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        })
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        """
        Drop the database after each test.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
