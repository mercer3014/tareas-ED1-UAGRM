class GestorAutomovil:
    """Gestor estático de automóviles con métodos de clase."""
    def __init__(self):
        self.__automoviles = []  # lista privada de autos

    # --- Getter ---
    def get_automoviles(self):
        return self.__automoviles

    # --- Setter ---
    def set_automoviles(self, automoviles):
        if isinstance(automoviles, list):
            self.__automoviles = automoviles
        else:
            print("Error: Debes pasar una lista de automóviles.")

    # --- Métodos de gestión ---
    def agregar(self, marca, modelo, anio):
        auto = {"marca": marca, "modelo": modelo, "año": anio}
        self.__automoviles.append(auto)

    def mostrar(self):
        if not self.__automoviles:
            print("No hay automóviles registrados.")
        else:
            for i, auto in enumerate(self.__automoviles, 1):
                print(f"{i}. {auto['marca']} {auto['modelo']} ({auto['año']})")

    def eliminar(self, indice):
        if 1 <= indice <= len(self.__automoviles):
            self.__automoviles.pop(indice - 1)
        else:
            print("Índice inválido.")

    def modificar(self, indice, marca, modelo, anio):
        if 1 <= indice <= len(self.__automoviles):
            self.__automoviles[indice - 1] = {"marca": marca, "modelo": modelo, "año": anio}
        else:
            print("Índice inválido.")


# --- DEMO ---
if __name__ == "__main__":
    gestor = GestorAutomovil()

    # Usando setter para establecer lista inicial
    gestor.set_automoviles([
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
        {"marca": "Ford", "modelo": "Fiesta", "año": 2018}
    ])

    print("Automóviles iniciales (con setter):")
    gestor.mostrar()

    print("\nAgregar un automóvil:")
    gestor.agregar("Honda", "Civic", 2022)
    gestor.mostrar()

    print("\nModificar el automóvil 2:")
    gestor.modificar(2, "Ford", "Focus", 2019)
    gestor.mostrar()

    print("\nEliminar el automóvil 1:")
    gestor.eliminar(1)
    gestor.mostrar()

    print("\nUsando getter para obtener lista cruda:")
    print(gestor.get_automoviles())
