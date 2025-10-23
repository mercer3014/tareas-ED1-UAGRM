import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from controllers.controller import PolinomioController


class VistaPolinomio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Polinomio Matemático")
        self.geometry("800x500")
        self.resizable(False, False)

        self.controller = PolinomioController()
        self._crear_componentes()

    def _crear_componentes(self):
        # Marco principal
        frame = ttk.Frame(self, padding=15)
        frame.pack(fill="both", expand=True)

        # Entradas
        ttk.Label(frame, text="Coeficiente:").grid(row=0, column=0, sticky="w", pady=5)
        self.coef_entry = ttk.Entry(frame, width=10)
        self.coef_entry.grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="Exponente:").grid(row=0, column=2, sticky="w", pady=5)
        self.exp_entry = ttk.Entry(frame, width=10)
        self.exp_entry.grid(row=0, column=3, padx=5)

        ttk.Label(frame, text="Polinomio:").grid(row=0, column=4, sticky="w")
        self.var_poli = tk.StringVar(value="P")
        ttk.Radiobutton(frame, text="P(x)", variable=self.var_poli, value="P").grid(row=0, column=5)
        ttk.Radiobutton(frame, text="Q(x)", variable=self.var_poli, value="Q").grid(row=0, column=6)

        ttk.Button(frame, text="Agregar término", command=self.agregar_termino).grid(row=1, column=0, columnspan=7, pady=8)

        # Mostrar polinomios
        ttk.Label(frame, text="Polinomio P(x):").grid(row=2, column=0, sticky="w")
        self.lbl_p = ttk.Label(frame, text="(vacío)", background="white", width=60)
        self.lbl_p.grid(row=2, column=1, columnspan=6, sticky="w")

        ttk.Label(frame, text="Polinomio Q(x):").grid(row=3, column=0, sticky="w", pady=5)
        self.lbl_q = ttk.Label(frame, text="(vacío)", background="white", width=60)
        self.lbl_q.grid(row=3, column=1, columnspan=6, sticky="w")

        # Evaluar
        ttk.Label(frame, text="Evaluar en x = ").grid(row=4, column=0, sticky="w", pady=5)
        self.x_entry = ttk.Entry(frame, width=10)
        self.x_entry.grid(row=4, column=1, padx=5)
        self.var_eval = tk.StringVar(value="P")
        ttk.Radiobutton(frame, text="P(x)", variable=self.var_eval, value="P").grid(row=4, column=2)
        ttk.Radiobutton(frame, text="Q(x)", variable=self.var_eval, value="Q").grid(row=4, column=3)
        ttk.Button(frame, text="Evaluar", command=self.evaluar).grid(row=4, column=4, padx=5)

        # Operaciones
        ttk.Button(frame, text="Sumar P + Q", command=self.sumar).grid(row=5, column=0, columnspan=2, pady=10)
        ttk.Button(frame, text="Multiplicar P * Q", command=self.multiplicar).grid(row=5, column=2, columnspan=2)
        ttk.Button(frame, text="Limpiar", command=self.limpiar).grid(row=5, column=5, columnspan=2)

        # Resultado
        ttk.Label(frame, text="Resultado:").grid(row=6, column=0, sticky="nw")
        self.txt_resultado = tk.Text(frame, width=70, height=10, wrap="word")
        self.txt_resultado.grid(row=7, column=0, columnspan=7, pady=10)

    # ----- FUNCIONES -----
    def agregar_termino(self):
        try:
            coef = float(self.coef_entry.get())
            exp = int(self.exp_entry.get())
            poli = self.var_poli.get()
            self.controller.agregar_termino(poli, coef, exp)
            self.actualizar_pantalla()
            self.coef_entry.delete(0, tk.END)
            self.exp_entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar_pantalla(self):
        self.lbl_p.config(text=self.controller.obtener_polinomio("P"))
        self.lbl_q.config(text=self.controller.obtener_polinomio("Q"))

    def evaluar(self):
        try:
            x = float(self.x_entry.get())
            poli = self.var_eval.get()
            resultado = self.controller.evaluar(poli, x)
            self.txt_resultado.insert(tk.END, f"{poli}({x}) = {resultado}\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def sumar(self):
        resultado = self.controller.sumar()
        self.txt_resultado.insert(tk.END, f"P(x) + Q(x) = {resultado}\n")

    def multiplicar(self):
        resultado = self.controller.multiplicar()
        self.txt_resultado.insert(tk.END, f"P(x) * Q(x) = {resultado}\n")

    def limpiar(self):
        poli = self.var_poli.get()
        self.controller.limpiar(poli)
        self.actualizar_pantalla()
        self.txt_resultado.delete(1.0, tk.END)


if __name__ == "__main__":
    app = VistaPolinomio()
    app.mainloop()
