import tkinter as tk
from tkinter import ttk, messagebox
from controllers.controller import ExpresionController

class VistaExpresion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Evaluador con Pilas")
        self.geometry("900x300")

        self.controller = ExpresionController()
        self._crear_ui()

    def _crear_ui(self):
        frame = ttk.Frame(self, padding=15)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Ingrese expresión infija:").grid(row=0, column=0, sticky="w")
        self.entry = ttk.Entry(frame, width=40)
        self.entry.grid(row=0, column=1)

        ttk.Button(frame, text="Evaluar", command=self.evaluar).grid(row=1, column=0, columnspan=2, pady=10)

        self.txt = tk.Text(frame, width=70, height=10)
        self.txt.grid(row=2, column=0, columnspan=2)

    def evaluar(self):
        try:
            exp = self.entry.get()
            post, pre, res = self.controller.procesar(exp)

            self.txt.delete("1.0", tk.END)
            self.txt.insert(tk.END, f"Postfija : {' '.join(post)}\n")
            self.txt.insert(tk.END, f"Prefija  : {pre}\n")
            self.txt.insert(tk.END, f"Resultado: {res}\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))
