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

    def __init__(
            self,
            user_repository=default_user_repository,
            closet_repository=default_closet_repository):

        self._user = None
        self._user_repository = user_repository
        self._piece = None
        self._closet_repository = closet_repository

    def login(self, username: str, password: str):
        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise ValueError("Invalid username or password")

        self._user = user
        return user

    def get_current_user(self):
        return self._user

    def get_all_users(self):
        return self._user_repository.find_all()

    def logout(self):
        self._user = None

    def create_user(self, username: str, password: str, login=True):

        if self._user_repository.find_by_username(username):
            raise ValueError("Username already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

    def upload_piece(self, title: str, image, upload=True):
        if self._closet_repository.find_by_title(title):
            raise ValueError("A piece with this name already exists")

        piece = self._closet_repository.upload_piece(Piece(title, image))

        if upload:
            self._piece = piece

        return piece

    def show_image(self):
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

    def get_all_pieces(self):
        return self._closet_repository.find_all()


closet_service = ClosetService()
