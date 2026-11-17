"""User model with secure password handling.

This module defines the `User` class used by the application. Passwords are
stored as Werkzeug-generated hashes; use `verify_password` to authenticate.
"""

from werkzeug.security import generate_password_hash, check_password_hash


class User:
    """Simple user model.

    Attributes:
        login (str): the username or login identifier.
        password_hash (str): hashed password stored for authentication.
        id (int): optional unique identifier set elsewhere (e.g., DB).
    """

    def __init__(self, login, password_hash):
        # Store the login identifier.
        self.login = login
        self.password_hash = password_hash
        self.id = None  # to be set externally, e.g., by the database
        # Optional: add other user-related fields here (e.g., email, profile info).

    def hash_and_set_password(self, password):
        """Set a new password for the user, hashing it securely."""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Return True if `password` matches the stored password hash."""
        return check_password_hash(self.password_hash, password)

    def to_session(self):
        """Export user data for session storage.

        Return a small JSON-serializable mapping with only non-sensitive fields.
        """
        return {
            "id": self.id,
            "login": self.login,
            # ...
        }

    def __repr__(self):
        """Return a developer-friendly string representation."""
        return f"<User login={self.login}>"
