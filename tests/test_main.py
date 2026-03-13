import pytest
from unittest.mock import patch
from temp_module import EmailAddress

def test_email_address_creation_with_valid_email():
    # Arrange: a valid email
    valid_email = "user@example.com"
    
    # Act: create EmailAddress
    email_address = EmailAddress(valid_email)
    
    # Assert: value is correctly stored and normalized
    assert email_address.value == "user@example.com"

def test_email_address_creation_with_invalid_email_format():
    # Arrange: an invalid email format
    invalid_email = "not-an-email"
    
    # Act & Assert: creating EmailAddress raises ValueError
    with pytest.raises(ValueError, match="Invalid email format"):
        EmailAddress(invalid_email)

def test_email_address_normalization():
    # Arrange: an email with uppercase and whitespace
    unnormalized_email = "  User@Example.COM  "
    
    # Act: create EmailAddress
    email_address = EmailAddress(unnormalized_email)
    
    # Assert: email is normalized (lowercase, no whitespace)
    assert email_address.value == "user@example.com"