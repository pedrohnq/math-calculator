import settings

import tkinter as tk


class Title(tk.Label):
    def __init__(self, parent, text, name = '', style = {}, *args, **kwargs):
        tk.Label.__init__(
            self, 
            parent, 
            text=text,
            cnf={
                "name": name
            },
            *args, 
            **kwargs
        )

        self.config(
            font=(settings.FONT, 24, "bold"),
            fg=settings.COLORS["text"],
            bg=settings.COLORS["background"]
        )

        if style:
            self.pack(**style)
        else:
            self.pack()