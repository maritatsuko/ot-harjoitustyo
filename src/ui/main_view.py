from tkinter import ttk, constants, PhotoImage, Canvas, Scrollbar
from services.closet_service import closet_service


class MainView:
    def __init__(self, root, handle_show_start_view, handle_show_upload_view):
        self._root = root.minsize(800, 1000)
        self._handle_show_start_view = handle_show_start_view
        self._handle_show_upload_view = handle_show_upload_view
        self._frame = None
        self._all_pieces = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _delete_piece(self, piece):
        if closet_service.delete_piece(piece):
            self._show_uploaded_pieces()

    def _show_uploaded_pieces(self):
        self._all_pieces = closet_service.get_all_pieces()

        # code generated with copilot starts here
        for widget in self._canvas.winfo_children():
            widget.destroy()
        content_frame = ttk.Frame(self._canvas, width=800)
        self._canvas.create_window((0, 0), window=content_frame, anchor="nw")
        # code generated with copilot ends here

        for i in range(len(self._all_pieces)):
            piece = self._all_pieces[i]
            color_label = ttk.Label(master=content_frame, text=piece.color)
            color_label.grid(row=4 + i, column=0, padx=5,
                             pady=5, sticky=constants.W)
            title_label = ttk.Label(master=content_frame, text=piece.title)
            title_label.grid(row=4 + i, column=1, padx=5,
                             pady=5, sticky=constants.W)
            image_path = piece.image_path
            filename = PhotoImage(file=image_path)
            canvas = Canvas(content_frame, width=filename.width(
            ), height=filename.height(), bg="white", bd=5, relief="groove")
            image = canvas.create_image(0, 0, image=filename, anchor="nw")
            canvas.grid(row=4 + i, column=2, padx=5,
                        pady=5, sticky=constants.N)
            canvas.image = filename
            delete_button = ttk.Button(
                master=content_frame, text="Delete piece", command=lambda piece=piece: self._delete_piece(piece))
            delete_button.grid(row=4 + i, column=3, padx=10,
                               pady=5, sticky=constants.E)

        # code generated with copilot starts here
        content_frame.update_idletasks()
        self._canvas.config(scrollregion=self._canvas.bbox("all"))
        # code generated with copilot ends here

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        title = ttk.Label(master=self._frame,
                          text="Your Closet <3", font=("Times", 24))
        welcome_text = ttk.Label(
            master=self._frame, text="Welcome to ClosetApp! Here you can manage your closet and outfits.", font=("Times", 16))

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_show_start_view)

        title2 = ttk.Label(
            master=self._frame, text="Uploaded pieces:", font=("Times", 20))
        new_upload_button = ttk.Button(
            master=self._frame, text="Upload a new piece", command=self._handle_show_upload_view)

        # code generated with copilot starts here
        # Create a canvas and a scrollbar
        self._canvas = Canvas(self._frame, width=800)
        scrollbar = Scrollbar(self._frame, orient="vertical",
                              command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=scrollbar.set)
        # code generated with copilot ends here

        self._frame.grid_columnconfigure(2, weight=1)
        self._frame.grid_rowconfigure(4, weight=1)
        logout_button.grid(row=0, column=2, padx=5, pady=5, sticky=constants.E)
        title.grid(row=1, column=0, padx=5, pady=5, sticky=constants.EW)
        welcome_text.grid(row=2, column=0, padx=5, pady=5, sticky=constants.EW)
        title2.grid(row=3, column=0, padx=5, pady=5, sticky=constants.EW)
        new_upload_button.grid(row=3, column=1, padx=5,
                               pady=5, sticky=constants.E)
        # code generated with copilot starts here
        # Place the canvas and scrollbar
        self._canvas.grid(row=4, column=0, sticky=constants.NSEW)
        scrollbar.grid(row=4, column=4, sticky=constants.NS)
        # code generated with copilot ends here
        self._show_uploaded_pieces()
