import tkinter as tk
from tkinter import ttk

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista Circular de Figuras")
        self.controlador = None  

        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(main_frame, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)

        controls_frame = ttk.Frame(main_frame)
        controls_frame.pack(fill=tk.X, pady=5)

        ttk.Label(controls_frame, text="Seleccione figura:").pack()
        self.combo_figura = ttk.Combobox(controls_frame,
                                        values=["Círculo", "Rectángulo", "Triángulo"],
                                        state="readonly")
        self.combo_figura.pack(pady=5)

        ttk.Label(controls_frame, text="Seleccione color:").pack()
        self.combo_color = ttk.Combobox(controls_frame,
                                        values=["Rojo", "Azul", "Verde"],
                                        state="readonly")
        self.combo_color.pack(pady=5)

        # Botones sin comandos aún
        self.btn_ingresar = ttk.Button(controls_frame, text="Ingresar Figura")
        self.btn_ingresar.pack(pady=10)

        nav_frame = ttk.Frame(main_frame)
        nav_frame.pack(fill=tk.X, pady=5)

        self.btn_retroceder = ttk.Button(nav_frame, text="← Retroceder")
        self.btn_retroceder.pack(side=tk.LEFT, padx=5)

        self.btn_avanzar = ttk.Button(nav_frame, text="Avanzar →")
        self.btn_avanzar.pack(side=tk.RIGHT, padx=5)

    def set_controlador(self, controlador):
        self.controlador = controlador
        self.btn_ingresar.config(command=self.controlador.ingresar_figura)
        self.btn_avanzar.config(command=self.controlador.avanzar)
        self.btn_retroceder.config(command=self.controlador.retroceder)

    def dibujar_figura(self, figura, color):
        self.canvas.delete("all")
        color_map = {"Rojo": "red", "Azul": "blue", "Verde": "green"}
        c = color_map.get(color, "black")

        if figura == "Círculo":
            self.canvas.create_oval(100, 100, 200, 200, fill=c)
        elif figura == "Rectángulo":
            self.canvas.create_rectangle(100, 100, 200, 200, fill=c)
        elif figura == "Triángulo":
            self.canvas.create_polygon(150, 100, 100, 200, 200, 200, fill=c)