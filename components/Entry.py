import settings

import tkinter as tk


class Entry(tk.Entry):
    def __init__(self, parent, name = '', style = {}, *args, **kwargs):
        tk.Entry.__init__(
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
            bg=settings.COLORS["white"],
            relief=tk.FLAT,
            highlightbackground=settings.COLORS["primary"],
            highlightthickness=1
        )

        if style:
            self.pack(**style)
        else:
            self.pack()