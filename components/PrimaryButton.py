import settings

import tkinter as tk


class PrimaryButton(tk.Button):
    def __init__(self, parent, name = '', style = {}, *args, **kwargs):
        tk.Button.__init__(
            self, 
            parent,
            cnf={
                "name": name
            },
            *args, 
            **kwargs
        )

        self.config(
            font=(settings.FONT, 12, "bold"),
            fg=settings.COLORS["white"],
            bg=settings.COLORS["primary"],
            activebackground=settings.COLORS["secondary"],
            activeforeground=settings.COLORS["white"],
            relief=tk.FLAT,
            bd=0,
        )

        if style:
            self.pack(**style)
        else:
            self.pack()