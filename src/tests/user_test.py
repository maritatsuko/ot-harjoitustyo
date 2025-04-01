import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all()
        self.user_mari = User("mari", "1234")
    
    def test_create_user(self):
        user_repository.create(self.user_mari)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, "mari")

