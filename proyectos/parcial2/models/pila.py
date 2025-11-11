class Pila:
    def __init__(self):
        self.items = []
    def push(self, dato):
        self.items.append(dato)
    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None
    def esta_vacia(self):
        return len(self.items) == 0
    def __iter__(self):
        return iter(self.items)