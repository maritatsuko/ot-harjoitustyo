class Piece:
    """Represents a piece of clothing with its attributes.
    """

    def __init__(self, title: str, image_path: str, color: str, category: str, uploaded_by: str):
        """Class constructor for a new piece of clothing.

        Args:
            title (str): Name of the piece of clothing.
            image_path (str): Path to the image of the piece.
            color (str): Color of the piece.
            category (str): Category of the piece (e.g., top, skirt, etc.).
            uploaded_by (str): Username of the person who uploaded the piece.
        """
        self.title = title
        self.image_path = image_path
        self.color = color
        self.category = category
        self.uploaded_by = uploaded_by
