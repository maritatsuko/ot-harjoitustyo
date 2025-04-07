import unittest
from repositories.closet_repository import closet_repository
from entities.piece import Piece

class TestClosetRepository(unittest.TestCase):

    def setUp(self):
        closet_repository.delete_all()
        self.piece_blaser = Piece("Blaser", "src/data/test_data/blaser.png")
    
    def test_upload_piece(self):
        closet_repository.upload_piece(self.piece_blaser)
        pieces = closet_repository.find_all()
        self.assertEqual(len(pieces), 1)
        self.assertEqual(pieces[0].title, "Blaser")
