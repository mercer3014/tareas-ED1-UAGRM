from nodo import *

class ListaEnlazada :
    def __init__(self):
        self.head = None
        self.cant = 0

    def getCant(self):
        return self.cant

    def insert(self,coeficiente,exponente):
        nw = Nodo(coeficiente, exponente, self.head)
        
        aux = self.head
        while aux:
            if aux.exponente == exponente:
                aux.coeficiente += coeficiente
                return
            aux = aux.nex

        self.head = nw
        self.cant += 1
        self.ordenarDesc()

    def ordenarDesc(self):
        if self.head is None or self.head.nex is None:
            return  # no hay nada que ordenar

        actual = self.head
        while actual is not None:
            siguiente = actual.nex
            while siguiente is not None:
                if siguiente.exponente > actual.exponente:
                    # Intercambiamos coeficientes y exponentes
                    actual.coeficiente, siguiente.coeficiente = siguiente.coeficiente, actual.coeficiente
                    actual.exponente, siguiente.exponente = siguiente.exponente, actual.exponente
                siguiente = siguiente.nex
            actual = actual.nex

    def obtenerDato(self, i):
        if i < 0 or i >= self.cant:
            print('Indice fuera de rango')
            return
        
        act = self.head
        for x in range (i):
            act = act.nex

        return (act.coeficiente, act.exponente)
    
    def evaluarPolinomio(self, x):
        r = 0
        for i in range(self.cant):
            coef, exp = self.obtenerDato(i)
            r += coef * (x ** exp)
        return r

    def __str__(self):
        aux = self.head
        s = ''
        if aux is None:
            return s

        s = s + str(aux.coeficiente) + 'x^' + str(aux.exponente)
        aux = aux.nex
        while aux:
            if aux.coeficiente > 0:
                s = s + ' + ' + str(aux.coeficiente) + 'x^' + str(aux.exponente)
            else:
                s = s + str(aux.coeficiente) + 'x^' + str(aux.exponente)
            aux = aux.nex

        return s

def sumarPolinomios(P:ListaEnlazada, Q:ListaEnlazada):
    R = ListaEnlazada()

    for i in range(P.getCant()):
        coef, exp = P.obtenerDato(i)
        R.insert(coef, exp)

    for i in range(Q.getCant()):
        coef, exp = Q.obtenerDato(i)
        R.insert(coef, exp)

    return R

def multiplicarPolinomio(P:ListaEnlazada, Q:ListaEnlazada):
    R = ListaEnlazada()
    for i in range(Q.getCant()):
        coef, exp = Q.obtenerDato(i)
        for j in range(P.getCant()):
            coef2, exp2 = P.obtenerDato(j)
            R.insert(coef * coef2, exp + exp2)

    return R


if __name__ == '__main__':
    L = ListaEnlazada()
    L.insert(2, 3)
    #L.insert(7, 5)
    L.insert(5, 4)

    M = ListaEnlazada()
    M.insert(3, 3)
    M.insert(5, 5)
    #M.insert(5, 8)

    print(f"Px: {L}")
    #print(L.evaluarPolinomio(3))
    print(f"Qx: {M}")

    #print(f"Rx: {sumarPolinomios(L, M)}")
    print(f'Rx: {multiplicarPolinomio(L, M)}')
