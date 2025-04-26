from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    """Converts a database row into a User object.

    Args:
        row [_type_]: A dictionary representing a row from the database.

    Returns:
        User: A User object created from the database row if the row is not None, otherwise None.
    """
    return User(row["username"], row["password"]) if row else None

class UserRepository:
    """Repository class for managing users in the system.
    """

    def __init__(self, connection):
        """Class constructor for the UserRepository.

        Args:
            connection: Database connection object.
        """

        self._connection = connection

    def find_all(self):
        """Fetches all users from the database.

        Returns:
            list: A list of User objects representing all users in the system.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """Fetches a user by their username from the database.

        Args:
            username: The username of the user to search for.

        Returns:
            User: A User object representing the user with the given username, or None if not found.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )
        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        """Creates a new user in the database.

        Args:
            user(username, password): The user object to be created.

        Returns:
            User: The created User object.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def delete_all(self):
        """Deletes all users from the database.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
