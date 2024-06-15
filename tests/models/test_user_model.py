"""
Tests for the User model.
"""

import unittest
from app import create_app, db
from app.models.user import User


class TestUserModel(unittest.TestCase):
    """
    Test case for the User model.
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
            self.user = User(username='testuser', email='testuser@example.com')
            self.user.set_password('password')
            db.session.add(self.user)
            db.session.commit()

    def tearDown(self):
        """
        Clean up after each test.
        """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_password(self):
        """
        Test the password hashing and checking functionality.
        """
        with self.app.app_context():
            user = User.query.filter_by(username='testuser').first()
            self.assertTrue(user.check_password('password'))
            self.assertFalse(user.check_password('wrongpassword'))


if __name__ == '__main__':
    unittest.main()