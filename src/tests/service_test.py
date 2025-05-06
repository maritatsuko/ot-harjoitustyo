import unittest
import bcrypt
from services.closet_service import closet_service
from repositories.closet_repository import closet_repository
from entities.piece import Piece
from repositories.user_repository import user_repository
from entities.user import User


class TestClosetService(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all()
        closet_repository.delete_all()
        self.test_username = "mari"
        self.test_password = "1234"
        self.test_user = closet_service.create_user(self.test_username, self.test_password)
        self.piece_blaser = Piece(
            "Blaser", "src/data/test_data/blaser.png", "brown", "jacket")

    def test_login(self):
        logged_user = closet_service.login(self.test_user.username, self.test_password)
        self.assertEqual(logged_user.username, "mari")
        self.assertTrue(
            bcrypt.checkpw(self.test_password.encode('utf-8'), logged_user.password.encode('utf-8')))

    def test_logout(self):
        closet_service.login(self.test_user.username, self.test_password)
        closet_service.logout()
        self.assertIsNone(closet_service.get_current_user())

    def test_create_user(self):
        user_repository.delete_all()
        closet_service.create_user(self.test_username, self.test_password)
        new_user = user_repository.find_by_username(self.test_username)
        self.assertEqual(new_user.username, self.test_username)
        self.assertTrue(
            bcrypt.checkpw(self.test_password.encode('utf-8'), new_user.password.encode('utf-8')))
