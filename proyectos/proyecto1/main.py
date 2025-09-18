import tkinter as tk

from mvc.view.app_view import AppView
from mvc.controller.app_controller import AppController


def main():
    root = tk.Tk()
    view = AppView(root)
    AppController(view)
    root.mainloop()


if __name__ == "__main__":
    main()


