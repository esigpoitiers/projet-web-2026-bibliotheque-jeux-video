"""User controller: retrieval and persistence helpers.

This module provides a thin controller layer around the `SQL` abstraction used
by the app. It focuses on fetching users from the database and returning
`User` objects. Note: the mapping from a DB row to the `User` constructor is
application-specific — see the comments in `get_by_id`.
"""

from models.user import User
from sql import SQL
from typing import Optional


class UserController:
    """Controller handling user-related database operations.

    The controller is initialized with an `SQL` instance (a small database
    wrapper provided by `sql.py`). Methods should translate DB rows into
    domain objects (`User`).
    """

    def __init__(self, db: SQL):
        # Store the provided database abstraction for reuse in methods.
        self.db = db

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Return a `User` for `user_id`, or `None` when not found.
        Args:
            user_id (int): the unique identifier of the user to fetch.
        Returns:
            Optional[User]: the corresponding `User` object, or `None` if not found
        """
        rows = self.db.execute("SELECT * FROM users WHERE id = ?", user_id)
        if not rows:
            return None

        # Select the first row from the results
        row = rows[0]

        user = User(row['username'], row['password_hash'])
        user.id = row['id']
        return user

    def get_by_username(self, username: str) -> Optional[User]:
        """Return a `User` for `username`, or `None` when not found.
        Args:
            username (str): the username of the user to fetch.
        Returns:
            Optional[User]: the corresponding `User` object, or `None` if not found
        """
        # TODO: implement this method
        raise NotImplementedError("get_by_username is not implemented yet")

    def create_user(self, user: User) -> int:
        """Insert a new user into the database.
        Args:
            user (User): the `User` object to insert.
        Returns:
            int: the newly created user's ID.
        """

        # TODO: implement this method
        raise NotImplementedError("create_user is not implemented yet")
