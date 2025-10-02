# ==============================
# ADT Polinomio - Implementación Estática y Dinámica
# Autor: Alex
# ==============================

class Termino:
    """Clase para representar un término de un polinomio en lista enlazada."""

    def __init__(self, coeficiente: float, exponente: int):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

    # Getters y Setters
    def get_coeficiente(self) -> float:
        return self.coeficiente

    def set_coeficiente(self, valor: float) -> None:
        self.coeficiente = valor

    def get_exponente(self) -> int:
        return self.exponente

    def set_exponente(self, valor: int) -> None:
        self.exponente = valor


class PolinomioEstatico:
    """Representación estática de un polinomio usando lista de coeficientes."""

    def __init__(self, grado: int):
        self.coeficientes = [0] * (grado + 1)

    def set_coeficiente(self, exponente: int, valor: float) -> None:
        if 0 <= exponente < len(self.coeficientes):
            self.coeficientes[exponente] = valor

    def get_coeficiente(self, exponente: int) -> float:
        if 0 <= exponente < len(self.coeficientes):
            return self.coeficientes[exponente]
        return 0

    def __str__(self) -> str:
        return " + ".join(
            f"{c}x^{i}"
            for i, c in enumerate(self.coeficientes) if c != 0
        ) or "0"


class PolinomioDinamico:
    """Representación dinámica de un polinomio usando lista enlazada."""

    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente: float, exponente: int) -> None:
        nuevo = Termino(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def __str__(self) -> str:
        actual = self.cabeza
        resultado = []
        while actual:
            resultado.append(f"{actual.coeficiente}x^{actual.exponente}")
            actual = actual.siguiente
        return " + ".join(resultado) or "0"


# ==============================
# Ejemplo de uso
# ==============================
if __name__ == "__main__":
    # Polinomio estático: 2x^0 + 3x^2 + 5x^3
    pe = PolinomioEstatico(3)
    pe.set_coeficiente(0, 2)
    pe.set_coeficiente(2, 3)
    pe.set_coeficiente(3, 5)
    print("Polinomio Estático:", pe)

    # Polinomio dinámico: 4x^1 + 7x^2
    pd = PolinomioDinamico()
    pd.agregar_termino(4, 1)
    pd.agregar_termino(7, 2)
    print("Polinomio Dinámico:", pd)
