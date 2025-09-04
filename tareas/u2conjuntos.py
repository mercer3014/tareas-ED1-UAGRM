# ===============================
# ADT CONJUNTO - Estructura Dinámica
# ===============================
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ConjuntoDinamico:
    def __init__(self):
        self.cabeza = None

    # Getter
    def get_elementos(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    # Setter
    def set_elementos(self, lista):
        for elem in lista:
            self.agregar(elem)

    def agregar(self, elemento):
        if not self.contiene(elemento):
            nuevo = Nodo(elemento)
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

    def quitar(self, elemento):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato == elemento:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def contiene(self, elemento):
        actual = self.cabeza
        while actual:
            if actual.dato == elemento:
                return True
            actual = actual.siguiente
        return False

    def __str__(self):
        return "{" + ", ".join(map(str, self.get_elementos())) + "}"


# ===============================
# ADT CONJUNTO - Estructura Estática
# ===============================
class ConjuntoEstatico:
    def __init__(self, elementos=None):
        self.elementos = elementos if elementos else []

    # Getters y setters
    def get_elementos(self):
        return self.elementos

    def set_elementos(self, elementos):
        self.elementos = list(elementos)

    def agregar(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def quitar(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def __str__(self):
        return "{" + ", ".join(map(str, self.elementos)) + "}"


# ===============================
# ADT POLINOMIO - Estructura Dinámica
# ===============================
class NodoPolinomio:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class PolinomioDinamico:
    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        nuevo = NodoPolinomio(coeficiente, exponente)
        if not self.cabeza or self.cabeza.exponente < exponente:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.exponente >= exponente:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def __str__(self):
        resultado = ""
        actual = self.cabeza
        while actual:
            if actual.coeficiente != 0:
                if resultado and actual.coeficiente > 0:
                    resultado += "+"
                resultado += f"{actual.coeficiente}x^{actual.exponente}" if actual.exponente != 0 else f"{actual.coeficiente}"
            actual = actual.siguiente
        return resultado if resultado else "0"


# ===============================
# ADT POLINOMIO - Estructura Estática
# ===============================
class PolinomioEstatico:
    def __init__(self):
        self.terminos = []  # lista de tuplas (coeficiente, exponente)

    def agregar_termino(self, coeficiente, exponente):
        self.terminos.append((coeficiente, exponente))
        self.terminos.sort(key=lambda x: -x[1])  # orden descendente por exponente

    def __str__(self):
        resultado = ""
        for coef, exp in self.terminos:
            if coef != 0:
                if resultado and coef > 0:
                    resultado += "+"
                resultado += f"{coef}x^{exp}" if exp != 0 else f"{coef}"
        return resultado if resultado else "0"


# ===============================
# EJEMPLOS DE USO
# ===============================
if __name__ == "__main__":
    # Conjunto dinámico
    cd = ConjuntoDinamico()
    cd.set_elementos([1, 2, 3])
    cd.agregar(4)
    cd.quitar(2)
    print("Conjunto dinámico:", cd)

    # Conjunto estático
    ce = ConjuntoEstatico([5, 6, 7])
    ce.agregar(8)
    ce.quitar(6)
    print("Conjunto estático:", ce)

    # Polinomio dinámico
    pd = PolinomioDinamico()
    pd.agregar_termino(3, 2)
    pd.agregar_termino(5, 1)
    pd.agregar_termino(-2, 3)
    print("Polinomio dinámico:", pd)

    # Polinomio estático
    pe = PolinomioEstatico()
    pe.agregar_termino(4, 3)
    pe.agregar_termino(-1, 1)
    pe.agregar_termino(2, 0)
    print("Polinomio estático:", pe)
