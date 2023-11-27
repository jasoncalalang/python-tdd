import unittest
from unittest.mock import MagicMock
from AuthService import AuthService

class TestAuthService(unittest.TestCase):
    def setUp(self):
        self.mock_user_db = MagicMock()
        self.auth_service = AuthService(self.mock_user_db)

    def test_authenticate_valid_user(self):
        # Setup
        self.mock_user_db.validate_user.return_value = True

        # Action
        result = self.auth_service.authenticate("valid_user", "correct_password")

        # Assert
        self.assertTrue(result)
        self.mock_user_db.validate_user.assert_called_once_with("valid_user", "correct_password")

    def test_authenticate_invalid_user(self):
        # Setup
        self.mock_user_db.validate_user.return_value = False

        # Action
        result = self.auth_service.authenticate("invalid_user", "wrong_password")

        # Assert
        self.assertFalse(result)
        self.mock_user_db.validate_user.assert_called_once_with("invalid_user", "wrong_password")

if __name__ == "__main__":
    unittest.main()

