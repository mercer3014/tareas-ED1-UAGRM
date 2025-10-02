# ==============================
# ADT Inventario de Productos - Estático y Dinámico
# Autor: Alex
# ==============================

class Producto:
    """Clase que representa un producto."""

    def __init__(self, nombre: str, cantidad: int, precio: float):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_nombre(self) -> str:
        return self.nombre

    def get_cantidad(self) -> int:
        return self.cantidad

    def get_precio(self) -> float:
        return self.precio

    # Setters
    def set_nombre(self, nombre: str) -> None:
        self.nombre = nombre

    def set_cantidad(self, cantidad: int) -> None:
        self.cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        self.precio = precio

    def __str__(self) -> str:
        return f"{self.nombre} (Cant: {self.cantidad}, Precio: {self.precio})"


class InventarioEstatico:
    """Inventario estático con capacidad fija."""

    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.productos = [None] * capacidad
        self.tamano = 0

    def agregar(self, producto: Producto) -> None:
        if self.tamano < self.capacidad:
            self.productos[self.tamano] = producto
            self.tamano += 1

    def get_producto(self, indice: int) -> Producto:
        if 0 <= indice < self.tamano:
            return self.productos[indice]
        return None

    def set_producto(self, indice: int, producto: Producto) -> None:
        if 0 <= indice < self.tamano:
            self.productos[indice] = producto

    def __str__(self) -> str:
        return "InventarioEstatico: [" + ", ".join(
            str(p) for p in self.productos if p is not None
        ) + "]"


class InventarioDinamico:
    """Inventario dinámico usando lista de Python."""

    def __init__(self):
        self.productos = []

    def agregar(self, producto: Producto) -> None:
        self.productos.append(producto)

    def get_producto(self, indice: int) -> Producto:
        if 0 <= indice < len(self.productos):
            return self.productos[indice]
        return None

    def set_producto(self, indice: int, producto: Producto) -> None:
        if 0 <= indice < len(self.productos):
            self.productos[indice] = producto

    def __str__(self) -> str:
        return "InventarioDinamico: [" + ", ".join(
            str(p) for p in self.productos
        ) + "]"


# ==============================
# Ejemplo de uso
# ==============================
if __name__ == "__main__":
    # Inventario Estático
    ie = InventarioEstatico(3)
    ie.agregar(Producto("Pan", 10, 1.5))
    ie.agregar(Producto("Leche", 5, 2.0))
    print(ie)

    prod = ie.get_producto(0)
    prod.set_cantidad(20)  # Modifico cantidad con setter
    print("Inventario Estático Modificado:", ie)

    # Inventario Dinámico
    idn = InventarioDinamico()
    idn.agregar(Producto("Arroz", 8, 3.0))
    idn.agregar(Producto("Fideos", 12, 2.5))
    print(idn)

    idn.set_producto(1, Producto("Fideos Integrales", 15, 3.5))
    print("Inventario Dinámico Modificado:", idn)
