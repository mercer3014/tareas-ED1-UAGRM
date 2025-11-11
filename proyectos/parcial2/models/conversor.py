from .pila import Pila

class Conversor:
    def infija_a_postfija(self, exp):
        valores = Pila()
        operadores = Pila()
        num = ""
        for char in exp:
            if char.isdigit():
                num += char
            else:
                if num:
                    valores.push(num)
                    num = ""
                if char in "+-*/^":
                    operadores.push(char)
        if num:
            valores.push(num)
        salida = list(valores.items) + list(operadores.items)
        return salida

    def postfija_a_prefija(self, postfija):
        valores = Pila()
        operadores = Pila()
        for token in postfija:
            if token in "+-*/^":
                operadores.push(token)
            else:
                valores.push(token)
        salida = list(operadores.items) + list(valores.items)
        return " ".join(salida)