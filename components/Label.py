import settings

import tkinter as tk


class Label(tk.Label):
    def __init__(self, parent, name = '', style = {}, *args, **kwargs):
        tk.Label.__init__(
            self, 
            parent,
            cnf={
                "name": name
            },
            *args, 
            **kwargs
        )

        self.config(
            font=(settings.FONT, 12),
            fg=settings.COLORS["text"],
            bg=settings.COLORS["background"],
            relief=tk.FLAT,
            bd=0,
        )

        if style:
            self.pack(**style)
        else:
            self.pack()