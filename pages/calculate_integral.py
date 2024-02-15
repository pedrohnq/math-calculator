import tkinter as tk
import sympy as sp

from components import Entry, PrimaryButton, Label, Br
from pages.base import BasePage


def calculate_integral(page, expression):
    x = sp.symbols('x')
    result = sp.integrate(expression, x)
    page.nametowidget('result_label').config(text=f"Result: {result}")


class CalculateIntegralPage(BasePage):
    def _set_widgets(self):
        Br(self)
        Label(self, text="Expression", name='expression_label', style={"pady": 5})
        Entry(self, name='expression_input', style={"pady": 5})
        PrimaryButton(
            self, text="Calculate", name='calculate_button', style={"pady": 10, "ipadx": 20},
            command=lambda: calculate_integral(
                self, 
                self.nametowidget('expression_input').get(),
            )
        )
        Label(self, text="", name='result_label', style={"pady": 10})