# models/evaluador.py
from .pila import Pila

class Evaluador:
    def evaluar_postfija(self, postfija):
        pila_valores = Pila()
        pila_operadores = Pila()

        for token in postfija:
            if token in "+-*/^":
                pila_operadores.push(token)
            else:
                pila_valores.push(float(token))

        resultado = pila_valores.pop()
        while not pila_operadores.esta_vacia():
            op = pila_operadores.pop()
            val = pila_valores.pop()
            if op == '+':
                resultado = val + resultado
            elif op == '-':
                resultado = val - resultado
            elif op == '*':
                resultado = val * resultado
            elif op == '/':
                resultado = val / resultado
            elif op == '^':
                resultado = val ** resultado

        return resultado