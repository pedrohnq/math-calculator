from components import Title, PrimaryButton
from pages.base import BasePage


class WelcomePage(BasePage):
    def _set_widgets(self):
        Title(self, text="Math calculator", name='welcome_title', style={"pady": 20})
        PrimaryButton(
            self, text="Limit", name='calculate_limit_button', style={"pady": 20, "ipadx": 38}, 
            command = lambda: self.controller.render("CalculateLimitPage")
        )
        PrimaryButton(
            self, text="Derivative", name='calculate_derivative_button', 
            style={"pady": 20, "ipadx": 20}, command = lambda: self.controller.render("CalculateDerivativePage")
        )
        PrimaryButton(
            self, text="Integral", name='calculate_integral_button', style={"pady": 20, "ipadx": 30},
            command = lambda: self.controller.render("CalculateIntegralPage")
        )
