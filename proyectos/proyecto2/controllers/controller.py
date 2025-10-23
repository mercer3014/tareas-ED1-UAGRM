import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tkinter import messagebox
from models.listaEnlazada import ListaEnlazada, sumarPolinomios, multiplicarPolinomio


class PolinomioController:
    def __init__(self):
        self.P = ListaEnlazada()
        self.Q = ListaEnlazada()

    def agregar_termino(self, nombre_polinomio, coeficiente, exponente):
        if nombre_polinomio.upper() == "P":
            self.P.insert(coeficiente, exponente)
        elif nombre_polinomio.upper() == "Q":
            self.Q.insert(coeficiente, exponente)
        else:
            raise ValueError("Debe especificar 'P' o 'Q' como nombre del polinomio.")

    def obtener_polinomio(self, nombre_polinomio):
        if nombre_polinomio.upper() == "P":
            return str(self.P)
        elif nombre_polinomio.upper() == "Q":
            return str(self.Q)
        else:
            raise ValueError("Polinomio inválido")

    def evaluar(self, nombre_polinomio, x):
        if nombre_polinomio.upper() == "P":
            return self.P.evaluarPolinomio(x)
        elif nombre_polinomio.upper() == "Q":
            return self.Q.evaluarPolinomio(x)
        else:
            raise ValueError("Polinomio inválido")

    def sumar(self):
        resultado = sumarPolinomios(self.P, self.Q)
        return str(resultado)

    def multiplicar(self):
        resultado = multiplicarPolinomio(self.P, self.Q)
        return str(resultado)

    def limpiar(self, nombre_polinomio):
        if nombre_polinomio.upper() == "P":
            self.P = ListaEnlazada()
        elif nombre_polinomio.upper() == "Q":
            self.Q = ListaEnlazada()
        else:
            raise ValueError("Polinomio inválido")
