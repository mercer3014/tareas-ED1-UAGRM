import tkinter as tk
from tkinter import ttk


class AppView(ttk.Frame):
    """
    Vista principal con dos pestañas: Conjuntos y Relaciones.
    No contiene lógica de negocio; expone callbacks para el controlador.
    """

    def __init__(self, master: tk.Misc):
        super().__init__(master)
        self.master.title("Simulador de Conjuntos y Relaciones")
        self.master.geometry("820x600")

        self._build_widgets()

        # Callbacks que el controlador asignará
        self.on_compute_sets = None
        self.on_check_relations = None

    def _build_widgets(self) -> None:
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Tab de Conjuntos
        tab_sets = ttk.Frame(notebook)
        notebook.add(tab_sets, text="Conjuntos")
        self._build_sets_tab(tab_sets)

        # Tab de Relaciones
        tab_rel = ttk.Frame(notebook)
        notebook.add(tab_rel, text="Relaciones (Opcional)")
        self._build_relations_tab(tab_rel)

        self.pack(fill=tk.BOTH, expand=True)

    # ---------------- Conjuntos -----------------
    def _build_sets_tab(self, parent: ttk.Frame) -> None:
        container = ttk.Frame(parent, padding=12)
        container.pack(fill=tk.BOTH, expand=True)

        # Entradas para conjuntos A y B
        row1 = ttk.Frame(container)
        row1.pack(fill=tk.X, pady=4)
        ttk.Label(row1, text="Conjunto A (ej: {a,b,c} o a,b,c):").pack(side=tk.LEFT)
        self.entry_set_a = ttk.Entry(row1)
        self.entry_set_a.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)

        row2 = ttk.Frame(container)
        row2.pack(fill=tk.X, pady=4)
        ttk.Label(row2, text="Conjunto B (ej: {b,c,d} o b,c,d):").pack(side=tk.LEFT)
        self.entry_set_b = ttk.Entry(row2)
        self.entry_set_b.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)

        # Botones de operaciones
        buttons = ttk.Frame(container)
        buttons.pack(fill=tk.X, pady=8)

        self.btn_union = ttk.Button(buttons, text="Unión", command=self._handle_compute_sets)
        self.btn_intersection = ttk.Button(buttons, text="Intersección", command=self._handle_compute_sets)
        self.btn_difference = ttk.Button(buttons, text="Diferencia A−B", command=self._handle_compute_sets)
        self.btn_difference_ba = ttk.Button(buttons, text="Diferencia B−A", command=self._handle_compute_sets)
        self.btn_symdiff = ttk.Button(buttons, text="Dif. Simétrica", command=self._handle_compute_sets)
        self.btn_subset = ttk.Button(buttons, text="A ⊆ B?", command=self._handle_compute_sets)
        self.btn_superset = ttk.Button(buttons, text="A ⊇ B?", command=self._handle_compute_sets)

        for w in [
            self.btn_union,
            self.btn_intersection,
            self.btn_difference,
            self.btn_difference_ba,
            self.btn_symdiff,
            self.btn_subset,
            self.btn_superset,
        ]:
            w.pack(side=tk.LEFT, padx=4)

        # Área de resultados y errores
        out_frame = ttk.LabelFrame(container, text="Resultado", padding=8)
        out_frame.pack(fill=tk.BOTH, expand=True, pady=8)
        self.txt_sets_output = tk.Text(out_frame, height=8, wrap=tk.WORD)
        self.txt_sets_output.pack(fill=tk.BOTH, expand=True)

        err_frame = ttk.LabelFrame(container, text="Errores", padding=8)
        err_frame.pack(fill=tk.BOTH, expand=False)
        self.var_sets_error = tk.StringVar(value="")
        lbl_err = ttk.Label(err_frame, textvariable=self.var_sets_error, foreground="red")
        lbl_err.pack(fill=tk.X)

    def _handle_compute_sets(self):
        if self.on_compute_sets is None:
            return
        # Determinar operación desde el botón
        widget = self.master.focus_get()
        op = None
        if widget is self.btn_union:
            op = "union"
        elif widget is self.btn_intersection:
            op = "intersection"
        elif widget is self.btn_difference:
            op = "difference_ab"
        elif widget is self.btn_difference_ba:
            op = "difference_ba"
        elif widget is self.btn_symdiff:
            op = "symdiff"
        elif widget is self.btn_subset:
            op = "subset"
        elif widget is self.btn_superset:
            op = "superset"
        if op is None:
            return
        self.on_compute_sets(
            op,
            self.entry_set_a.get(),
            self.entry_set_b.get(),
        )

    def show_sets_result(self, text: str) -> None:
        self.txt_sets_output.configure(state=tk.NORMAL)
        self.txt_sets_output.delete("1.0", tk.END)
        self.txt_sets_output.insert(tk.END, text)
        self.txt_sets_output.configure(state=tk.DISABLED)

    def show_sets_error(self, message: str) -> None:
        self.var_sets_error.set(message or "")

    # ---------------- Relaciones -----------------
    def _build_relations_tab(self, parent: ttk.Frame) -> None:
        container = ttk.Frame(parent, padding=12)
        container.pack(fill=tk.BOTH, expand=True)

        row_u = ttk.Frame(container)
        row_u.pack(fill=tk.X, pady=4)
        ttk.Label(row_u, text="Universo U (ej: {a,b,c}):").pack(side=tk.LEFT)
        self.entry_universe = ttk.Entry(row_u)
        self.entry_universe.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)

        row_r = ttk.Frame(container)
        row_r.pack(fill=tk.X, pady=4)
        ttk.Label(row_r, text="Relación R (ej: {(a,a),(a,b)}):").pack(side=tk.LEFT)
        self.entry_relation = ttk.Entry(row_r)
        self.entry_relation.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)

        # Botón verificar
        btns = ttk.Frame(container)
        btns.pack(fill=tk.X, pady=8)
        self.btn_check_rel = ttk.Button(btns, text="Verificar propiedades", command=self._handle_check_relations)
        self.btn_check_rel.pack(side=tk.LEFT)

        # Salida
        out_frame = ttk.LabelFrame(container, text="Propiedades", padding=8)
        out_frame.pack(fill=tk.BOTH, expand=True, pady=8)
        self.txt_rel_output = tk.Text(out_frame, height=10, wrap=tk.WORD)
        self.txt_rel_output.pack(fill=tk.BOTH, expand=True)

        err_frame = ttk.LabelFrame(container, text="Errores", padding=8)
        err_frame.pack(fill=tk.BOTH, expand=False)
        self.var_rel_error = tk.StringVar(value="")
        lbl_err = ttk.Label(err_frame, textvariable=self.var_rel_error, foreground="red")
        lbl_err.pack(fill=tk.X)

    def _handle_check_relations(self):
        if self.on_check_relations is None:
            return
        self.on_check_relations(
            self.entry_universe.get(),
            self.entry_relation.get(),
        )

    def show_relations_result(self, text: str) -> None:
        self.txt_rel_output.configure(state=tk.NORMAL)
        self.txt_rel_output.delete("1.0", tk.END)
        self.txt_rel_output.insert(tk.END, text)
        self.txt_rel_output.configure(state=tk.DISABLED)

    def show_relations_error(self, message: str) -> None:
        self.var_rel_error.set(message or "")


