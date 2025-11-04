from tkinter import messagebox

class Controlador:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo

    def ingresar_figura(self):
        figura = self.vista.combo_figura.get()
        color = self.vista.combo_color.get()
        
        if not figura or not color:
            messagebox.showwarning("Advertencia", 
                "Por favor seleccione una figura y un color")
            return
            
        self.modelo.insertar(figura, color)
        self.actualizar_vista()

    def avanzar(self):
        if not self.modelo.actual:
            messagebox.showinfo("Información", 
                "No hay figuras en la lista")
            return
        self.modelo.avanzar()
        self.actualizar_vista()

    def retroceder(self):
        if not self.modelo.actual:
            messagebox.showinfo("Información", 
                "No hay figuras en la lista")
            return
        self.modelo.retroceder()
        self.actualizar_vista()

    def actualizar_vista(self):
        figura, color_siguiente = self.modelo.obtener_actual()
        if figura:
            self.vista.dibujar_figura(figura, color_siguiente)