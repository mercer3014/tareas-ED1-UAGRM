# ==============================
# ADT Conjunto - Estático y Dinámico
# Autor: Alex
# ==============================

class ConjuntoEstatico:
    """Implementación estática del conjunto usando lista fija."""

    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.elementos = [None] * capacidad
        self.tamano = 0

    def agregar(self, valor: int) -> None:
        """Agrega un valor si no existe y hay espacio."""
        if valor not in self.elementos and self.tamano < self.capacidad:
            self.elementos[self.tamano] = valor
            self.tamano += 1

    def get_elemento(self, indice: int):
        """Getter de elemento por índice."""
        if 0 <= indice < self.tamano:
            return self.elementos[indice]
        return None

    def set_elemento(self, indice: int, valor: int) -> None:
        """Setter: modifica un valor en una posición existente."""
        if 0 <= indice < self.tamano:
            self.elementos[indice] = valor

    def __str__(self) -> str:
        return "{" + ", ".join(str(e) for e in self.elementos if e is not None) + "}"


class ConjuntoDinamico:
    """Implementación dinámica del conjunto usando lista de Python."""

    def __init__(self):
        self.elementos = []

    def agregar(self, valor: int) -> None:
        """Agrega un valor si no existe."""
        if valor not in self.elementos:
            self.elementos.append(valor)

    def get_elemento(self, indice: int):
        """Getter de elemento por índice."""
        if 0 <= indice < len(self.elementos):
            return self.elementos[indice]
        return None

    def set_elemento(self, indice: int, valor: int) -> None:
        """Setter: modifica un valor en una posición existente."""
        if 0 <= indice < len(self.elementos):
            self.elementos[indice] = valor

    def __str__(self) -> str:
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"


# ==============================
# Ejemplo de uso
# ==============================
if __name__ == "__main__":
    # Conjunto Estático
    ce = ConjuntoEstatico(5)
    ce.agregar(1)
    ce.agregar(2)
    ce.agregar(3)
    print("Conjunto Estático:", ce)
    print("Getter índice 1:", ce.get_elemento(1))
    ce.set_elemento(1, 99)
    print("Conjunto Estático Modificado:", ce)

    # Conjunto Dinámico
    cd = ConjuntoDinamico()
    cd.agregar(10)
    cd.agregar(20)
    cd.agregar(30)
    print("Conjunto Dinámico:", cd)
    print("Getter índice 0:", cd.get_elemento(0))
    cd.set_elemento(0, 100)
    print("Conjunto Dinámico Modificado:", cd)

