import unittest
from services.closet_service import closet_service
from repositories.closet_repository import closet_repository
from entities.piece import Piece
from repositories.user_repository import user_repository
from entities.user import User

class TestClosetService(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all()
        closet_repository.delete_all()
        self.user_mari = User("mari", "1234")
        self.piece_blaser = Piece("Blaser", "src/data/test_data/blaser.png", "brown", "jacket")
    
    def test_login(self):
        closet_service.create_user(self.user_mari.username, self.user_mari.password)
        logged_user = closet_service.login(self.user_mari.username, self.user_mari.password)
        self.assertEqual(logged_user.username, "mari")
        self.assertEqual(logged_user.password, "1234")
    
    def test_logout(self):
        closet_service.create_user(self.user_mari.username, self.user_mari.password)
        closet_service.login(self.user_mari.username, self.user_mari.password)
        closet_service.logout()
        self.assertIsNone(closet_service.get_current_user())
