import re

def is_valid_password_simplified(password):
    # Check if the password is at least 8 characters
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        return False

    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        return False

    # Check for at least one number
    if not re.search("[0-9]", password):
        return False

    # Check for at least one special character
    if not re.search("[!@#$%^&*(),.<>/?;:'\"[\\]{}|`~=_+-]", password):
        return False

    return True

def test_password_validator():
    # Test minimum length
    assert not is_valid_password_simplified('Pass12'), "Fail: Password should be at least 8 characters long."

    # Test uppercase letter requirement
    assert not is_valid_password_simplified('password123!'), "Fail: Password should contain at least one uppercase letter."

    # Test lowercase letter requirement
    assert not is_valid_password_simplified('PASSWORD123!'), "Fail: Password should contain at least one lowercase letter."

    # Test number requirement
    assert not is_valid_password_simplified('Password!'), "Fail: Password should contain at least one number."

    # Test special character requirement
    assert not is_valid_password_simplified('Password123'), "Fail: Password should contain at least one special character."

    # Test valid password
    assert is_valid_password_simplified('ValidPass123!'), "Fail: This is a valid password and should pass all checks."

    print("All tests passed!")

# Run the tests
if __name__ == "__main__":
    test_password_validator()

