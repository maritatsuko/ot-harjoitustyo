from tkinter import filedialog
import os
from entities.user import User
from entities.piece import Piece

from repositories.user_repository import (
    user_repository as default_user_repository
)
from repositories.closet_repository import (
    closet_repository as default_closet_repository
)


class ClosetService:
    """Service class for managing user authentication and closet operations.
    """

    def __init__(
            self,
            user_repository=default_user_repository,
            closet_repository=default_closet_repository):
        """Class constructor for the ClosetService.

        Args:
            user_repository: The user repository. Defaults to default_user_repository.
            closet_repository: The closet repository. Defaults to default_closet_repository.
            _user: The current user. Defaults to None.
            _piece: The current piece. Defaults to None.
        """

        self._user = None
        self._user_repository = user_repository
        self._piece = None
        self._closet_repository = closet_repository

    def login(self, username: str, password: str):
        """Logs in a user by validating their credentials.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Raises:
            ValueError: If the username or password is invalid.

        Returns:
            User: The authenticated user object.
        """
        user = self._user_repository.find_by_username(username)
        if not user or self._user_repository.verify_password(user, password) is False:
            raise ValueError("Invalid username or password")

        self._user = user
        return user

    def get_current_user(self):
        """Returns the currently logged-in user.

        Returns:
            User: The currently logged-in user object.
        """
        return self._user

    def get_all_users(self):
        """Returns all users in the system.

        Returns:
            list: A list of all user objects.
        """
        return self._user_repository.find_all()

    def logout(self):
        """Logs out the current user by setting the _user attribute to None.
        """
        self._user = None

    def create_user(self, username: str, password: str, login=True):
        """Creates a new user in the system.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
            login (bool, optional): Defaults to True.

        Raises:
            ValueError: If the username already exists.

        Returns:
            User: The newly created user object.
        """

        if self._user_repository.find_by_username(username):

            raise ValueError("Username already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def upload_piece(self, title: str, image_path: str, color: str, category: str, upload=True):
        """Uploads a new piece of clothing.

        Args:
            title (str): Title (name) of the piece.
            image_path (str): Image path for the piece.
            color (str): Color of the piece.
            category (str): Category of the piece (eg. top, skirt).
            upload (bool, optional): Defaults to True.

        Raises:
            ValueError: If a piece with the same name already exists.

        Returns:
            Piece: The uploaded piece.
        """
        if self._closet_repository.find_by_title(title):
            raise ValueError("A piece with this name already exists")

        piece = self._closet_repository.upload_piece(
            Piece(title, image_path, color, category))

        if upload:
            self._piece = piece

        return piece

    def edit_piece(self, title: str, old_title: str, image_path: str, color: str, category: str):
        """Edits an existing piece of clothing.

        Args:
            title (str): Title (name) of the piece.
            image_path (str): Image path for the piece.
            color (str): Color of the piece.
            category (str): Category of the piece (eg. top, skirt).

        Returns:
            Piece: The edited piece.
        """

        piece = self._closet_repository.edit_piece(
            Piece(title, image_path, color, category), old_title)

        self._piece = piece

        return piece

    def get_all_pieces(self):
        """Fetches all uploaded pieces.

        Returns:
            list: List of all pieces.
        """
        return self._closet_repository.find_all()

    def delete_piece(self, piece: Piece):
        """Deletes a specific piece.

        Args:
            piece (Piece): The piece that should be deleted.

        Returns:
            True
        """
        self._closet_repository.delete_piece(piece)
        return True

    def show_image(self):
        """Shows the uploaded image on the main view.

        Raises:
            ValueError: If the image format is incorrect.

        Returns:
            file_path: The image path.
        """
        file_path = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select image file",
            filetypes=[("PNG file", "*.png")])
        if not file_path:
            return None

        filename, ext = os.path.splitext(file_path)
        if ext.lower() not in [".png"]:
            raise ValueError("Invalid image format")

        return file_path

    def get_all_colors(self):
        """Fetches all colors.

        Returns:
            list: List of all colors.
        """
        return self._closet_repository.find_all_colors()

    def get_all_categories(self):
        """Fetches all categories.

        Returns:
            list: List of all categories.
        """
        return self._closet_repository.find_all_categories()


closet_service = ClosetService()
