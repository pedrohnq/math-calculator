from controller import Controller
from pages import WelcomePage, CalculateLimitPage, CalculateDerivativePage


def main():
    controller = Controller(frames = [WelcomePage, CalculateLimitPage, CalculateDerivativePage])
    controller.mainloop()


if __name__ == "__main__":
    main()