class GestorAutomovil:
    """Gestor estático de automóviles con métodos de clase."""

    # Atributo estático
    _autos = []

    # --- Getter y Setter ---
    @classmethod
    def get_autos(cls):
        return cls._autos

    @classmethod
    def set_autos(cls, autos):
        if isinstance(autos, list):
            cls._autos = autos
        else:
            print("Error: Debes pasar una lista de automóviles.")

    # --- Métodos del gestor ---
    @classmethod
    def agregar(cls, auto):
        cls._autos.append(auto)

    @classmethod
    def mostrar(cls):
        if not cls._autos:
            print("No hay automóviles registrados.")
        else:
            for i, auto in enumerate(cls._autos, 1):
                print(f"{i}. {auto}")

    @classmethod
    def eliminar(cls, indice):
        if 1 <= indice <= len(cls._autos):
            cls._autos.pop(indice - 1)
        else:
            print("Índice inválido.")

    @classmethod
    def modificar(cls, indice, nuevo_auto):
        if 1 <= indice <= len(cls._autos):
            cls._autos[indice - 1] = nuevo_auto
        else:
            print("Índice inválido.")


# --- DEMO ---
if __name__ == "__main__":
    # Usando setter para definir lista inicial
    GestorAutomovil.set_autos(["Toyota", "Ford"])
    print("Automóviles iniciales (con setter):")
    GestorAutomovil.mostrar()

    print("\nAgregar un auto con método agregar:")
    GestorAutomovil.agregar("Honda")
    GestorAutomovil.mostrar()

    print("\nModificar el auto 2:")
    GestorAutomovil.modificar(2, "Chevrolet")
    GestorAutomovil.mostrar()

    print("\nEliminar el auto 1:")
    GestorAutomovil.eliminar(1)
    GestorAutomovil.mostrar()

    print("\nUsando getter para obtener lista cruda:")
    print(GestorAutomovil.get_autos())
