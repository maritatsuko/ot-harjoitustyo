import unittest
from repositories.closet_repository import closet_repository
from entities.piece import Piece


class TestClosetRepository(unittest.TestCase):
    def setUp(self):
        closet_repository.delete_all()
        self.test_piece_1 = Piece(
            "Blaser", "src/data/test_data/blaser.png", "brown", "jacket")
        self.test_piece_2 = Piece(
            "Jacket", "src/data/test_data/jacket.png", "pink", "jacket")
        self.test_piece_3 = Piece(
            "T-shirt", "src/data/test_data/tshirt.png", "blue", "shirt")

    def test_upload_piece(self):
        piece = closet_repository.upload_piece(self.test_piece_1)
        self.assertEqual(piece.title, self.test_piece_1.title)
        self.assertEqual(piece.image_path, self.test_piece_1.image_path)
        self.assertEqual(piece.color, self.test_piece_1.color)
        self.assertEqual(piece.category, self.test_piece_1.category)

    def test_edit_piece(self):
        closet_repository.upload_piece(self.test_piece_1)
        piece = closet_repository.edit_piece(
            self.test_piece_2, self.test_piece_1.title)
        self.assertEqual(piece.title, self.test_piece_2.title)
        self.assertEqual(piece.image_path, self.test_piece_2.image_path)
        self.assertEqual(piece.color, self.test_piece_2.color)
        self.assertEqual(piece.category, self.test_piece_2.category)

    def test_delete_piece(self):
        closet_repository.upload_piece(self.test_piece_1)
        closet_repository.delete_piece(self.test_piece_1)
        piece = closet_repository.find_by_title(self.test_piece_1.title)
        self.assertIsNone(piece)

    def test_find_all(self):
        closet_repository.upload_piece(self.test_piece_1)
        closet_repository.upload_piece(self.test_piece_2)
        closet_repository.upload_piece(self.test_piece_3)
        pieces = closet_repository.find_all()
        self.assertEqual(len(pieces), 3)
        self.assertEqual(pieces[0].title, self.test_piece_1.title)
        self.assertEqual(pieces[1].title, self.test_piece_2.title)
        self.assertEqual(pieces[2].title, self.test_piece_3.title)

    def test_find_by_title(self):
        closet_repository.upload_piece(self.test_piece_1)
        piece = closet_repository.find_by_title(self.test_piece_1.title)
        self.assertEqual(piece.title, self.test_piece_1.title)
        self.assertEqual(piece.image_path, self.test_piece_1.image_path)
        self.assertEqual(piece.color, self.test_piece_1.color)
        self.assertEqual(piece.category, self.test_piece_1.category)
