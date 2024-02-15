import tkinter as tk
import sympy as sp

from components import Entry, PrimaryButton, Label, Br
from pages.base import BasePage


def calculate_derivative(page, expression):
    x = sp.symbols('x')
    result = sp.diff(expression, x)
    page.nametowidget('result_label').config(text=f"Result: {result}")


class CalculateDerivativePage(BasePage):
    def _set_widgets(self):
        Br(self)
        Label(self, text="Expression", name='expression_label', style={"pady": 5})
        Entry(self, name='expression_input', style={"pady": 5})
        PrimaryButton(
            self, text="Calculate", name='calculate_button', style={"pady": 10, "ipadx": 20},
            command=lambda: calculate_derivative(
                self, 
                self.nametowidget('expression_input').get(),
            )
        )
        Label(self, text="", name='result_label', style={"pady": 10})