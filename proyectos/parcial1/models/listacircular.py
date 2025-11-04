class Nodo:
    def __init__(self, figura, color):
        self.figura = figura
        self.color = color
        self.siguiente = None
        self.anterior = None

class ListaCircular:
    def __init__(self):
        self.actual = None
        self.inicio = None       

    def insertar(self, figura, color):
        nuevo = Nodo(figura, color)
        if not self.actual:
            nuevo.siguiente = nuevo.anterior = nuevo
            self.actual = nuevo
            self.inicio = nuevo 
        else:
            ultimo = self.actual.anterior
            nuevo.siguiente = self.actual
            nuevo.anterior = ultimo
            ultimo.siguiente = nuevo
            self.actual.anterior = nuevo

    def avanzar(self):
        if self.actual:
            self.actual = self.actual.siguiente
            # Si volvimos al inicio, rotamos colores
            if self.actual == self.inicio:
                self.rotar_colores()


    def retroceder(self):
        if self.actual:
            self.actual = self.actual.anterior

    def obtener_actual(self):
        if self.actual:
            siguiente_color = self.actual.siguiente.color
            return self.actual.figura, siguiente_color
        return None, None
    
    def rotar_colores(self):
        if not self.actual:
            return
        colores = []
        nodo = self.actual
        while True:
            colores.append(nodo.color)
            nodo = nodo.siguiente
            if nodo == self.actual:
                break

        colores = colores[1:] + colores[:1]

        nodo = self.actual
        for color in colores:
            nodo.color = color
            nodo = nodo.siguiente