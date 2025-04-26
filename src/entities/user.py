class User:
    """Represents a user in the system.
    """

    def __init__(self, username: str, password: str):
        """Class constructor for a new user.

        Args:
            username (str): Username of the user.
            password (str): Password of the user.
        """
        self.username = username
        self.password = password
