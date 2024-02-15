from controller import Controller
from pages import WelcomePage, CalculateLimitPage, CalculateDerivativePage, CalculateIntegralPage


def main():
    controller = Controller(
        frames = [WelcomePage, CalculateLimitPage, CalculateDerivativePage, CalculateIntegralPage]
    )
    controller.mainloop()


if __name__ == "__main__":
    main()