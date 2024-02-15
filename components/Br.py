import tkinter as tk


class Br(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        tk.Label.__init__(
            self,
            parent,
            text="",
            *args,
            **kwargs
        )
        self.pack({"pady": 10})