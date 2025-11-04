import sys
import os
import tkinter as tk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.listacircular import ListaCircular
from view.interfazcircular import Vista
from controllers.controllercircular import Controlador

def main():
    root = tk.Tk()
    root.geometry("600x600")
    modelo = ListaCircular()
    vista = Vista(root)
    controlador = Controlador(vista, modelo)
    vista.set_controlador(controlador)

    root.mainloop()

if __name__ == "__main__":
    main()