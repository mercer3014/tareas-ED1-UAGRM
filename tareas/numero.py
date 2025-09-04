class Numero:
    """
    Clase que representa un número y su longitud.

    Atributos
    ----------
    valor : int
        El valor del número.
    longitud : int
        La cantidad de dígitos del número.

    Métodos
    -------
    getNumero():
        Retorna el valor del número.
    setNumero(valor):
        Establece el valor del número.
    getLongitud():
        Retorna la longitud del número.
    setLongitud(longitud):
        Establece la longitud del número.
    """

    def __init__(self, valor, longitud):
        """
        Constructor de la clase Numero.

        Parámetros
        ----------
        valor : int
            El valor inicial del número.
        longitud : int
            La longitud inicial del número.
        """
        self.valor = valor
        self.longitud = longitud

    def getNumero(self):
        """
        Obtiene el valor del número.

        Returns
        -------
        int
            El valor del número.
        """
        return self.valor
    
    def setNumero(self, valor):
        """
        Establece el valor del número.

        Parámetros
        ----------
        valor : int
            Nuevo valor del número.
        """
        self.valor = valor

    def getLongitud(self):
        """
        Obtiene la longitud del número.

        Returns
        -------
        int
            La longitud del número.
        """
        return self.longitud

    def setLongitud(self, longitud):
        """
        Establece la longitud del número.

        Parámetros
        ----------
        longitud : int
            Nueva longitud del número.
        """
        self.longitud = longitud


if __name__ == "__main__":
    # Ejemplos de uso
    n = Numero(12345, 5)
    print("Número inicial:", n.getNumero())         # → 12345
    print("Longitud inicial:", n.getLongitud())     # → 5

    n.setNumero(6789)
    n.setLongitud(4)

    print("Número modificado:", n.getNumero())      # → 6789
    print("Longitud modificada:", n.getLongitud())  # → 4
