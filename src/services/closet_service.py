from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class ClosetService:

    def __init__(self, user_repository=default_user_repository):
        self._user = None
        self._user_repository = user_repository

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


closet_service = ClosetService()
