import tkinter as tk


class BasePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self._set_widgets()

    def _set_widgets(self):
        pass