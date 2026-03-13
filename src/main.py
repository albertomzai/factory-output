import re


class EmailAddress:
    """Represents an email address with validation and normalization."""
    
    def __init__(self, email: str):
        """
        Initialize an EmailAddress with validation and normalization.
        
        Args:
            email: The email address string to validate and normalize
            
        Raises:
            ValueError: If the email format is invalid
        """
        if not email or not re.match(r'^[^@]+@[^@]+\.[^@]+$', email.strip()):
            raise ValueError("Invalid email format")
            
        self.value = email.strip().lower()