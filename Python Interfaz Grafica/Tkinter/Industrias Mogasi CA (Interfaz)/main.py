import tkinter as tk
from tkinter import ttk, messagebox
from productos import productos, carrito, facturas, sucursales
from datetime import datetime

class BakerySystem:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sistema de Registro de Panadería")
        self.window.geometry("1000x700")
        
        # Configurar estilo
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#2196f3")
        self.style.configure("TLabel", padding=5)
        self.style.configure("Header.TLabel", font=("Calibri", 30, "bold"))
        
        self.setup_main_menu()

    def setup_main_menu(self):
        # Limpiar ventana
        for widget in self.window.winfo_children():
            widget.destroy()

        # Título
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(expand=True, fill="both")

        title = ttk.Label(main_frame, text="Sistema de Registro de Panadería", 
                         style="Header.TLabel")
        title.pack(pady=20)

        # Botones del menú principal
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

        # Número de factura
        ttk.Label(frame, text="Número de Factura:").pack(pady=5)
        factura_entry = ttk.Entry(frame)
        factura_entry.pack(pady=5)

        # Selección de sucursal
        ttk.Label(frame, text="Sucursal:").pack(pady=5)
        sucursal_var = tk.StringVar()
        sucursal_combo = ttk.Combobox(frame, values=sucursales, 
                                    textvariable=sucursal_var, state="readonly")
        sucursal_combo.pack(pady=5)
        sucursal_combo.set(sucursales[0])

        def continuar_registro():
            numero_factura = factura_entry.get().strip()
            if not numero_factura:
                messagebox.showerror("Error", "Por favor ingrese un número de factura")
                return
            
            if any(f['numero'] == numero_factura for f in facturas):
                messagebox.showerror("Error", "Este número de factura ya existe")
                return

            self.registrar_productos(numero_factura, sucursal_var.get())

        button_frame = ttk.Frame(frame)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Continuar", 
                  command=continuar_registro).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Cancelar", 
                  command=self.setup_main_menu).pack(side="left", padx=5)

    def registrar_productos(self, numero_factura, sucursal):
        for widget in self.window.winfo_children():
            widget.destroy()

        # Marco principal con scroll
        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(expand=True, fill="both")

        # Canvas y scrollbar para productos
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Entradas para productos
        entries = {}
        for codigo, producto in productos.items():
            frame = ttk.Frame(scrollable_frame)
            frame.pack(pady=5, padx=10, fill="x")

            ttk.Label(frame, text=producto['nombre']).pack(side="left", padx=5)

            ttk.Label(frame, text="|       Monto $").pack(pady=5, side="left")
            precio_var = tk.StringVar()
            precio_entry = ttk.Entry(frame, textvariable=precio_var, width=15)
            precio_entry.pack(side="left", padx=5)
            precio_entry.insert(0, "0")

            ttk.Label(frame, text="Unidades").pack(pady=5, side="left")
            unidades_var = tk.StringVar()
            unidades_entry = ttk.Entry(frame, textvariable=unidades_var, width=10)
            unidades_entry.pack(side="left", padx=5)
            unidades_entry.insert(0, "0")

            entries[codigo] = {
                'precio': precio_var,
                'unidades': unidades_var
            } 
            
        def guardar_registro():
            try:
                carrito.clear()
                for codigo, entry_vars in entries.items():
                    precio = float(entry_vars['precio'].get() or 0)
                    unidades = int(entry_vars['unidades'].get() or 0)

                    if precio < 0 or unidades < 0:
                        raise ValueError("Los valores no pueden ser negativos")

                    carrito[codigo] = {
                        'nombre': productos[codigo]['nombre'],
                        'precio': precio,
                        'unidades': unidades
                    }

                fecha_actual = datetime.now()
                facturas.append({
                    'numero': numero_factura,
                    'fecha': fecha_actual,
                    'sucursal': sucursal,
                    'productos': carrito.copy()
                })

                messagebox.showinfo("Éxito", "Venta registrada correctamente")
                self.mostrar_factura_gui(carrito, numero_factura, fecha_actual, sucursal)

            except ValueError as e:
                messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(pady=20)

        ttk.Button(button_frame, text="Guardar", 
                  command=guardar_registro).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Cancelar", 
                  command=self.setup_main_menu).pack(side="left", padx=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def mostrar_factura_gui(self, carrito, numero_factura, fecha, sucursal):
        for widget in self.window.winfo_children():
            widget.destroy()

        frame = ttk.Frame(self.window, padding="20")
        frame.pack(expand=True, fill="both")

        # Encabezado
        ttk.Label(frame, text="FACTURA DE VENTA", 
                 style="Header.TLabel").pack(pady=10)
        ttk.Label(frame, text=f"Número de Factura: {numero_factura}").pack()
        ttk.Label(frame, text=f"Fecha: {fecha.strftime('%d/%m/%Y %H:%M:%S')}").pack()
        ttk.Label(frame, text=f"Sucursal: {sucursal}").pack()

        # Tabla de productos
        table_frame = ttk.Frame(frame)
        table_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Encabezados
        headers = ["Producto", "Precio Unit.", "Unidades", "Subtotal"]
        for i, header in enumerate(headers):
            ttk.Label(table_frame, text=header, 
                     style="Header.TLabel").grid(row=0, column=i, padx=5, pady=5)

        # Productos
        total = 0
        row = 1
        for codigo, detalles in carrito.items():
            if detalles['unidades'] > 0:
                nombre = detalles['nombre']
                precio = detalles['precio']
                unidades = detalles['unidades']
                subtotal = precio * unidades

                ttk.Label(table_frame, text=nombre).grid(row=row, column=0, padx=5, pady=2)
                ttk.Label(table_frame, text=f"${precio:.2f}").grid(row=row, column=1, padx=5, pady=2)
                ttk.Label(table_frame, text=str(unidades)).grid(row=row, column=2, padx=5, pady=2)
                ttk.Label(table_frame, text=f"${subtotal:.2f}").grid(row=row, column=3, padx=5, pady=2)

                total += subtotal
                row += 1

        # Total
        ttk.Label(table_frame, text="TOTAL:", 
                 style="Header.TLabel").grid(row=row, column=2, padx=5, pady=10)
        ttk.Label(table_frame, text=f"${total:.2f}", 
                 style="Header.TLabel").grid(row=row, column=3, padx=5, pady=10)

        ttk.Button(frame, text="Volver al Menú Principal", 
                  command=self.setup_main_menu).pack(pady=20)

    def ver_factura_actual(self):
        if not carrito:
            messagebox.showwarning("Aviso", "No hay una venta activa")
            return
        self.mostrar_factura_gui(carrito, "ACTUAL", datetime.now(), "")

    def ver_facturas_anteriores(self):
        if not facturas:
            messagebox.showinfo("Información", "No hay facturas registradas")
            return

        for widget in self.window.winfo_children():
            widget.destroy()

        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(expand=True, fill="both")

        ttk.Label(main_frame, text="Facturas Registradas", 
                 style="Header.TLabel").pack(pady=10)

        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for factura in facturas:
            frame = ttk.Frame(scrollable_frame)
            frame.pack(pady=10, padx=10, fill="x")

            ttk.Label(frame, text=f"Factura #{factura['numero']}", 
                     style="Header.TLabel").pack()
            ttk.Label(frame, text=f"Fecha: {factura['fecha'].strftime('%d/%m/%Y %H:%M:%S')}").pack()
            ttk.Label(frame, text=f"Sucursal: {factura['sucursal']}").pack()

            def ver_detalle(f=factura):
                self.mostrar_factura_gui(
                    f['productos'],
                    f['numero'],
                    f['fecha'],
                    f['sucursal']
                )

            ttk.Button(frame, text="Ver Detalle", 
                      command=ver_detalle).pack(pady=5)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        ttk.Button(main_frame, text="Volver al Menú Principal", 
                  command=self.setup_main_menu).pack(pady=20)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BakerySystem()
    app.run()