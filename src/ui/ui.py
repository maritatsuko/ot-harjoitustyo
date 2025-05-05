from ui.start_view import StartView
from ui.create_acc_view import CreateAccView
from ui.main_view import MainView
from ui.upload_view import UploadView
from ui.edit_view import EditView

class UI:
    """
    This class represents the UI of the application.
    """

    def __init__(self, root):
        """Constructor for the UI class.

        Args:
            root: Root window of the application.
            _current_view: Current view being displayed.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Start the UI by showing the start view."""
        self._show_start_view()

    def _hide_current_view(self):
        """Hide the current view."""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_start_view(self):
        """Show the start view."""
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._show_main_view,
            self._show_create_acc_view
        )

        self._current_view.pack()
    
    def _show_create_acc_view(self):
        """Show the create account view."""
        self._hide_current_view()

        self._current_view = CreateAccView(
            self._root,
            self._show_main_view,
            self._show_start_view
        )

        self._current_view.pack()
    
    def _show_main_view(self):
        """Show the main view."""
        self._hide_current_view()
        self._current_view = MainView(
            self._root,
            self._show_start_view,
            self._show_upload_view,
            self._show_edit_view
        )

        self._current_view.pack()
    
    def _show_upload_view(self):
        """Show the upload view."""
        self._hide_current_view()
        self._current_view = UploadView(
            self._root,
            self._show_main_view,
            self._show_main_view
        )

        self._current_view.pack()
    
    def _show_edit_view(self, piece):
        """Show the edit view."""
        self._hide_current_view()
        self._current_view = EditView(
            self._root,
            piece,
            self._show_main_view,
            self._show_main_view
        )

        self._current_view.pack()