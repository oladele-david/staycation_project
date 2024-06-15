"""
Tests for configuration settings.
"""

import os
import unittest
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


class TestConfig(unittest.TestCase):
    """
    Test case for application configuration.
    """

    def test_environment_variables(self):
        """
        Test that required environment variables are set.
        """
        self.assertIsNotNone(os.getenv('DATABASE_URL'))
        self.assertIsNotNone(os.getenv('SECRET_KEY'))


if __name__ == '__main__':
    unittest.main()
