from entities.piece import Piece
# from entities.user import User
from database_connection import get_database_connection


def get_piece_by_row(row):
    return Piece(row["title"], row["image_path"]) if row else None


class ClosetRepository:

    def __init__(self, connection):

        self._connection = connection

    def find_all(self):

        cursor = self._connection.cursor()
        cursor.execute("select * from pieces")
        rows = cursor.fetchall()

        return list(map(get_piece_by_row, rows))

    def find_by_title(self, title):

        cursor = self._connection.cursor()
        cursor.execute(
            "select * from pieces where title = ?",
            (title,)
        )
        row = cursor.fetchone()

        return get_piece_by_row(row)

    def upload_piece(self, piece):

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into pieces (title, image_path) values (?, ?)",
            (piece.title, piece.image_path)
        )

        self._connection.commit()

        return piece

    def delete_all(self):

        cursor = self._connection.cursor()

        cursor.execute("delete from pieces")

        self._connection.commit()

    def delete_piece(self, piece):
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from pieces where title = ?",
            (piece.title,)
        )

        self._connection.commit()


closet_repository = ClosetRepository(get_database_connection())
