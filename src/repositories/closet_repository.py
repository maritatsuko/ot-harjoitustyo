from entities.piece import Piece
from database_connection import get_database_connection


def get_piece_by_row(row):
    """Converts a database row into a Piece object.

    Args:
        row[_type_]: A dictionary representing a row from the database.

    Returns:
        Piece: A Piece object created from the database row if the row is not None, otherwise None.
    """
    if not row:
        return None
    return Piece(row["title"], row["image_path"], row["color"], row["category"])


class ClosetRepository:
    """Repository class for managing pieces of clothing in the closet.
    """

    def __init__(self, connection):
        """Class constructor for the ClosetRepository.

        Args:
            connection: Database connection object.
        """

        self._connection = connection

    def find_all(self):
        """Fetches all pieces from the database.

        Returns:
            list: A list of Piece objects representing all pieces in the closet.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from pieces")
        rows = cursor.fetchall()

        return list(map(get_piece_by_row, rows))

    def find_by_title(self, title):
        """Fetches a piece by its title from the database.

        Args:
            title: The title (name) of the piece to search for.

        Returns:
            Piece: A Piece object representing the piece with the given title, or None if not found.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            "select * from pieces where title = ?",
            (title,)
        )
        row = cursor.fetchone()

        return get_piece_by_row(row)

    def upload_piece(self, piece):
        """Uploads a new piece to the database.

        Args:
            piece(title, image_path, color, category): 
            A Piece object representing the piece to be uploaded.

        Returns:
            Piece: The Piece object that was uploaded to the database.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into pieces (title, image_path, color, category) values (?, ?, ?, ?)",
            (piece.title, piece.image_path, piece.color, piece.category)
        )

        self._connection.commit()

        return piece

    def edit_piece(self, piece, old_title):
        """Edits an existing piece in the database.

        Args:
            piece: The Piece object representing the piece to be edited.
            old_title: The old title of the piece to be edited.
        
        Returns:
            Piece: The edited Piece object.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "update pieces set title = ?, image_path = ?, color = ?, category = ? where title = ?",
            (piece.title, piece.image_path, piece.color, piece.category, old_title)
        )

        self._connection.commit()
        return piece

    def delete_all(self):
        """Deletes all pieces from the database.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from pieces")

        self._connection.commit()

    def delete_piece(self, piece):
        """Deletes a specific piece from the database.

        Args:
            piece: The Piece object representing the piece to be deleted.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "delete from pieces where title = ?",
            (piece.title,)
        )

        self._connection.commit()

    def find_all_colors(self):
        """Fetches all colors from the database.

        Returns:
            list: A list of colors.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from colors")
        rows = cursor.fetchall()

        return [row["name"] for row in rows]

    def find_all_categories(self):
        """Fetches all categories from the database.

        Returns:
            list: A list of categories.
        """

        cursor = self._connection.cursor()
        cursor.execute("select * from categories")
        rows = cursor.fetchall()

        return [row["name"] for row in rows]


closet_repository = ClosetRepository(get_database_connection())
