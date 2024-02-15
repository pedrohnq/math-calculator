import settings

import tkinter as tk


class Controller(tk.Tk):
    def __init__(self, frames, *args, **kwargs):
        if not frames:
            raise ValueError("You must provide at least one frame to the controller")

        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.config(bg=settings.COLORS["background"])
        container.grid(column=0, row=0, sticky = "nsew")
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.title("Utilities Calculator")
        self.geometry("800x600")

        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in frames:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky = "nsew")            

        self.render(frames[0].__name__)

    def render(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()