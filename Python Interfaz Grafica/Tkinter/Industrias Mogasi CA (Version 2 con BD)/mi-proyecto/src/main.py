import tkinter as tk
from tkinter import ttk
from database import Database

class App:
    def __init__(self, root):
        self.window = root
        self.window.title("Sistema de Ventas")
        self.database = Database()
        self.setup_ui()

    def setup_ui(self):
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(expand=True, fill="both")

        title = ttk.Label(main_frame, text="Bienvenido al Sistema de Ventas", style="Header.TLabel")
        title.pack(pady=20)

        button_frame = ttk.Frame(main_frame)
        button_frame.pack(expand=True)

        ttk.Button(button_frame, text="Registrar Nueva Venta", 
                  command=self.iniciar_registro).pack(pady=10, padx=20)
        ttk.Button(button_frame, text="Ver Factura Actual", 
                  command=self.ver_factura_actual).pack(pady=10, padx=20)
        ttk.Button(button_frame, text="Ver Facturas Anteriores", 
                  command=self.ver_facturas_anteriores).pack(pady=10, padx=20)
        ttk.Button(button_frame, text="Salir", 
                  command=self.window.quit).pack(pady=10, padx=20)

    def iniciar_registro(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        frame = ttk.Frame(self.window, padding="20")
        frame.pack(expand=True, fill="x")

        ttk.Label(frame, text="Número de Factura:").pack(pady=5)
        factura_entry = ttk.Entry(frame)
        factura_entry.pack(pady=5)

        ttk.Label(frame, text="Sucursal:").pack(pady=5)
        sucursal_var = tk.StringVar()
        sucursal_combo = ttk.Combobox(frame, values=["Sucursal 1", "Sucursal 2"], 
                                    textvariable=sucursal_var, state="readonly")
        sucursal_combo.pack(pady=5)
        sucursal_combo.set("Sucursal 1")

        def continuar_registro():
            numero_factura = factura_entry.get().strip()
            sucursal = sucursal_var.get()
            self.database.registrar_venta(numero_factura, sucursal)

        ttk.Button(frame, text="Continuar", command=continuar_registro).pack(pady=10)

    def ver_factura_actual(self):
        pass  # Implementar lógica para ver factura actual

    def ver_facturas_anteriores(self):
        pass  # Implementar lógica para ver facturas anteriores

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()