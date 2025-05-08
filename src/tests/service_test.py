import unittest
import bcrypt
from services.closet_service import closet_service
from repositories.closet_repository import closet_repository
from entities.piece import Piece
from repositories.user_repository import user_repository


class TestClosetService(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all()
        closet_repository.delete_all()
        self.test_username = "mari"
        self.test_password = "1234"
        self.test_user = closet_service.create_user(
            self.test_username, self.test_password)
        self.piece_blaser = Piece(
            "Blaser", "src/data/test_data/blaser.png", "brown", "jacket", self.test_username)

    # User related tests

    def test_login(self):
        logged_user = closet_service.login(
            self.test_user.username, self.test_password)
        self.assertEqual(logged_user.username, "mari")
        self.assertTrue(
            bcrypt.checkpw(self.test_password.encode('utf-8'), logged_user.password.encode('utf-8')))

    def test_login_invalid_username(self):
        with self.assertRaises(ValueError):
            closet_service.login("invalid_username", self.test_password)

    def test_login_invalid_password(self):
        with self.assertRaises(ValueError):
            closet_service.login(self.test_user.username, "invalid_password")
    
    def test_login_with_empty_username(self):
        with self.assertRaises(ValueError):
            closet_service.login("", self.test_password)
    
    def test_login_with_empty_password(self):
        with self.assertRaises(ValueError):
            closet_service.login(self.test_user.username, "")

    def test_logout(self):
        closet_service.login(self.test_user.username, self.test_password)
        closet_service.logout()
        self.assertIsNone(closet_service.get_current_user())

    def test_create_user(self):
        user_repository.delete_all()
        new_user = closet_service.create_user(
            self.test_username, self.test_password)
        self.assertEqual(new_user.username, self.test_username)
        self.assertTrue(
            bcrypt.checkpw(self.test_password.encode('utf-8'), new_user.password.encode('utf-8')))

    def test_create_user_with_existing_username(self):
        with self.assertRaises(ValueError):
            closet_service.create_user(self.test_username, self.test_password)

    # Piece related tests

    def test_upload_piece(self):
        piece = closet_service.upload_piece(self.piece_blaser.title, self.piece_blaser.image_path,
                                            self.piece_blaser.color, self.piece_blaser.category)
        self.assertEqual(piece.title, self.piece_blaser.title)
        self.assertEqual(piece.image_path, self.piece_blaser.image_path)
        self.assertEqual(piece.color, self.piece_blaser.color)
        self.assertEqual(piece.category, self.piece_blaser.category)

    def test_upload_piece_with_existing_title(self):
        closet_service.upload_piece(self.piece_blaser.title, self.piece_blaser.image_path,
                                    self.piece_blaser.color, self.piece_blaser.category)
        with self.assertRaises(ValueError):
            closet_service.upload_piece(self.piece_blaser.title, self.piece_blaser.image_path,
                                        self.piece_blaser.color, self.piece_blaser.category)

    def test_edit_piece_title(self):
        closet_service.upload_piece(self.piece_blaser.title, self.piece_blaser.image_path,
                                    self.piece_blaser.color, self.piece_blaser.category)
        piece = closet_service.edit_piece("New Blaser", self.piece_blaser.title,
                                          self.piece_blaser.image_path, self.piece_blaser.color, self.piece_blaser.category)
        self.assertEqual(piece.title, "New Blaser")
        self.assertEqual(piece.image_path, self.piece_blaser.image_path)
        self.assertEqual(piece.color, self.piece_blaser.color)
        self.assertEqual(piece.category, self.piece_blaser.category)

    def test_edit_piece_image_path(self):
        closet_service.upload_piece(self.piece_blaser.title, self.piece_blaser.image_path,
                                    self.piece_blaser.color, self.piece_blaser.category)
        piece = closet_service.edit_piece(self.piece_blaser.title, self.piece_blaser.title,
                                          "src/data/test_data/jacket.png", self.piece_blaser.color, self.piece_blaser.category)
        self.assertEqual(piece.title, self.piece_blaser.title)
        self.assertEqual(piece.image_path, "src/data/test_data/jacket.png")
        self.assertEqual(piece.color, self.piece_blaser.color)
        self.assertEqual(piece.category, self.piece_blaser.category)

    def test_edit_piece_color(self):
        closet_service.upload_piece(self.piece_blaser.title, self.piece_blaser.image_path,
                                    self.piece_blaser.color, self.piece_blaser.category)
        piece = closet_service.edit_piece(self.piece_blaser.title, self.piece_blaser.title,
                                          self.piece_blaser.image_path, "green", self.piece_blaser.category)
        self.assertEqual(piece.title, self.piece_blaser.title)
        self.assertEqual(piece.image_path, self.piece_blaser.image_path)
        self.assertEqual(piece.color, "green")
        self.assertEqual(piece.category, self.piece_blaser.category)

    def test_edit_piece_category(self):
        closet_service.upload_piece(self.piece_blaser.title, self.piece_blaser.image_path,
                                    self.piece_blaser.color, self.piece_blaser.category)
        piece = closet_service.edit_piece(self.piece_blaser.title, self.piece_blaser.title,
                                          self.piece_blaser.image_path, self.piece_blaser.color, "jacket")
        self.assertEqual(piece.title, self.piece_blaser.title)
        self.assertEqual(piece.image_path, self.piece_blaser.image_path)
        self.assertEqual(piece.color, self.piece_blaser.color)
        self.assertEqual(piece.category, "jacket")

    def test_delete_piece(self):
        closet_service.upload_piece(self.piece_blaser.title, self.piece_blaser.image_path,
                                    self.piece_blaser.color, self.piece_blaser.category)
        closet_service.delete_piece(self.piece_blaser)
        piece = closet_repository.find_by_title(self.piece_blaser.title)
        self.assertIsNone(piece)
