from ui.start_view import StartView
from ui.create_acc_view import CreateAccView
from tkinter import ttk

class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._show_create_acc_view
        )

        self._current_view.pack()
    
    def _show_create_acc_view(self):
        self._hide_current_view()

        self._current_view = CreateAccView(
            self._root,
            self._show_start_view
        )

        self._current_view.pack()