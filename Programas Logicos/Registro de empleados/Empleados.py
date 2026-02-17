import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json
import os

class AppRegistroEmpleados:
    def _init_(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Empleados")
        self.root.geometry("1000x700")
        
        # Datos de empleados
        self.empleados = []
        self.cargar_datos()
        
        # Variables de control
        self.var_nombre = tk.StringVar()
        self.var_apellido = tk.StringVar()
        self.var_cedula = tk.StringVar()
        self.var_fecha_nac = tk.StringVar()
        self.var_direccion = tk.StringVar()
        self.var_telefono = tk.StringVar()
        self.var_email = tk.StringVar()
        self.var_cargo = tk.StringVar()
        self.var_salario_hora = tk.DoubleVar(value=0.0)
        self.var_horas_trabajadas = tk.DoubleVar(value=8.0)
        self.var_fecha_ingreso = tk.StringVar()
        self.var_estado_civil = tk.StringVar()
        self.var_educacion = tk.StringVar()
        self.var_emergencia_nombre = tk.StringVar()
        self.var_emergencia_telefono = tk.StringVar()
        self.var_buscar = tk.StringVar()
        
        # Crear interfaz
        self.crear_interfaz()
    
    def cargar_datos(self):
        if os.path.exists("empleados.json"):
            with open("empleados.json", "r") as f:
                self.empleados = json.load(f)
    
    def guardar_datos(self):
        with open("empleados.json", "w") as f:
            json.dump(self.empleados, f, indent=4)
    
    def crear_interfaz(self):
        # Notebook (pestañas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de Registro
        frame_registro = ttk.Frame(notebook)
        notebook.add(frame_registro, text="Registro")
        
        # Pestaña de Consulta
        frame_consulta = ttk.Frame(notebook)
        notebook.add(frame_consulta, text="Consulta")
        
        # Pestaña de Asistencia
        frame_asistencia = ttk.Frame(notebook)
        notebook.add(frame_asistencia, text="Asistencia")
        
        # Widgets de Registro
        self.crear_formulario_registro(frame_registro)
        
        # Widgets de Consulta
        self.crear_interfaz_consulta(frame_consulta)
        
        # Widgets de Asistencia
        self.crear_interfaz_asistencia(frame_asistencia)
    
    def crear_formulario_registro(self, parent):
        # Frame principal con scroll
        main_frame = tk.Frame(parent)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Información Personal
        lbl_personal = ttk.Label(scrollable_frame, text="Información Personal", font=('Helvetica', 12, 'bold'))
        lbl_personal.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
        
        ttk.Label(scrollable_frame, text="Nombre:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_nombre, width=30).grid(row=1, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Apellido:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_apellido, width=30).grid(row=2, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Cédula:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_cedula, width=30).grid(row=3, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Fecha Nacimiento (dd/mm/aaaa):").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_fecha_nac, width=30).grid(row=4, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Dirección:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_direccion, width=30).grid(row=5, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Teléfono:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_telefono, width=30).grid(row=6, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Email:").grid(row=7, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_email, width=30).grid(row=7, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Estado Civil:").grid(row=8, column=0, sticky="e", padx=5, pady=5)
        ttk.Combobox(scrollable_frame, textvariable=self.var_estado_civil, 
                     values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"], width=27).grid(row=8, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Nivel de Educación:").grid(row=9, column=0, sticky="e", padx=5, pady=5)
        ttk.Combobox(scrollable_frame, textvariable=self.var_educacion, 
                     values=["Primaria", "Secundaria", "Técnico", "Universitario", "Postgrado"], width=27).grid(row=9, column=1, sticky="w", pady=5)
        
        # Información Laboral
        lbl_laboral = ttk.Label(scrollable_frame, text="Información Laboral", font=('Helvetica', 12, 'bold'))
        lbl_laboral.grid(row=10, column=0, columnspan=2, pady=10, sticky="w")
        
        ttk.Label(scrollable_frame, text="Cargo:").grid(row=11, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_cargo, width=30).grid(row=11, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Salario por Hora ($):").grid(row=12, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_salario_hora, width=30).grid(row=12, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Horas Trabajadas por Día:").grid(row=13, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_horas_trabajadas, width=30).grid(row=13, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Fecha de Ingreso (dd/mm/aaaa):").grid(row=14, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_fecha_ingreso, width=30).grid(row=14, column=1, sticky="w", pady=5)
        
        # Contacto de Emergencia
        lbl_emergencia = ttk.Label(scrollable_frame, text="Contacto de Emergencia", font=('Helvetica', 12, 'bold'))
        lbl_emergencia.grid(row=15, column=0, columnspan=2, pady=10, sticky="w")
        
        ttk.Label(scrollable_frame, text="Nombre:").grid(row=16, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_emergencia_nombre, width=30).grid(row=16, column=1, sticky="w", pady=5)
        
        ttk.Label(scrollable_frame, text="Teléfono:").grid(row=17, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(scrollable_frame, textvariable=self.var_emergencia_telefono, width=30).grid(row=17, column=1, sticky="w", pady=5)
        
        # Botones
        btn_frame = ttk.Frame(scrollable_frame)
        btn_frame.grid(row=18, column=0, columnspan=2, pady=20)
        
        ttk.Button(btn_frame, text="Guardar", command=self.guardar_empleado).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Limpiar", command=self.limpiar_formulario).pack(side=tk.LEFT, padx=5)
    
    def crear_interfaz_consulta(self, parent):
        # Frame de búsqueda
        frame_busqueda = ttk.Frame(parent)
        frame_busqueda.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame_busqueda, text="Buscar (nombre, cédula o cargo):").pack(side=tk.LEFT, padx=5)
        ttk.Entry(frame_busqueda, textvariable=self.var_buscar, width=30).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_busqueda, text="Buscar", command=self.buscar_empleado).pack(side=tk.LEFT, padx=5)
        ttk.Button(frame_busqueda, text="Mostrar Todos", command=self.mostrar_todos).pack(side=tk.LEFT, padx=5)
        
        # Treeview para mostrar empleados
        frame_tree = ttk.Frame(parent)
        frame_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        columns = ("cedula", "nombre", "apellido", "cargo", "salario_hora", "horas_dia", "sueldo_dia")
        self.tree = ttk.Treeview(frame_tree, columns=columns, show="headings", selectmode="browse")
        
        # Configurar columnas
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("apellido", text="Apellido")
        self.tree.heading("cargo", text="Cargo")
        self.tree.heading("salario_hora", text="Salario/Hora")
        self.tree.heading("horas_dia", text="Horas/Día")
        self.tree.heading("sueldo_dia", text="Sueldo/Día")
        
        self.tree.column("cedula", width=100)
        self.tree.column("nombre", width=120)
        self.tree.column("apellido", width=120)
        self.tree.column("cargo", width=120)
        self.tree.column("salario_hora", width=80, anchor="e")
        self.tree.column("horas_dia", width=80, anchor="e")
        self.tree.column("sueldo_dia", width=100, anchor="e")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        # Botón para ver detalles
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(btn_frame, text="Ver Detalles", command=self.mostrar_detalles).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Eliminar", command=self.eliminar_empleado).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Exportar a CSV", command=self.exportar_csv).pack(side=tk.RIGHT, padx=5)
        
        # Mostrar todos los empleados al inicio
        self.mostrar_todos()
    
    def crear_interfaz_asistencia(self, parent):
        # Frame para registrar asistencia
        frame_registro = ttk.Frame(parent)
        frame_registro.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(frame_registro, text="Cédula Empleado:").pack(side=tk.LEFT, padx=5)
        self.var_cedula_asistencia = tk.StringVar()
        ttk.Entry(frame_registro, textvariable=self.var_cedula_asistencia, width=15).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame_registro, text="Fecha (dd/mm/aaaa):").pack(side=tk.LEFT, padx=5)
        self.var_fecha_asistencia = tk.StringVar()
        ttk.Entry(frame_registro, textvariable=self.var_fecha_asistencia, width=12).pack(side=tk.LEFT, padx=5)
        
        ttk.Label(frame_registro, text="Horas Trabajadas:").pack(side=tk.LEFT, padx=5)
        self.var_horas_asistencia = tk.DoubleVar(value=8.0)
        ttk.Entry(frame_registro, textvariable=self.var_horas_asistencia, width=5).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(frame_registro, text="Registrar Asistencia", command=self.registrar_asistencia).pack(side=tk.LEFT, padx=10)
        
        # Treeview para mostrar asistencias
        frame_tree = ttk.Frame(parent)
        frame_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        columns = ("fecha", "cedula", "nombre", "horas", "salario_dia")
        self.tree_asistencia = ttk.Treeview(frame_tree, columns=columns, show="headings", selectmode="browse")
        
        # Configurar columnas
        self.tree_asistencia.heading("fecha", text="Fecha")
        self.tree_asistencia.heading("cedula", text="Cédula")
        self.tree_asistencia.heading("nombre", text="Nombre")
        self.tree_asistencia.heading("horas", text="Horas")
        self.tree_asistencia.heading("salario_dia", text="Salario Día")
        
        self.tree_asistencia.column("fecha", width=100)
        self.tree_asistencia.column("cedula", width=100)
        self.tree_asistencia.column("nombre", width=150)
        self.tree_asistencia.column("horas", width=80, anchor="e")
        self.tree_asistencia.column("salario_dia", width=100, anchor="e")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree_asistencia.yview)
        self.tree_asistencia.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree_asistencia.pack(fill=tk.BOTH, expand=True)
        
        # Cargar asistencias
        self.cargar_asistencias()
    
    def guardar_empleado(self):
        # Validar campos obligatorios
        if not self.var_nombre.get() or not self.var_apellido.get() or not self.var_cedula.get():
            messagebox.showerror("Error", "Nombre, apellido y cédula son campos obligatorios")
            return
        
        try:
            salario_hora = float(self.var_salario_hora.get())
            horas_trabajadas = float(self.var_horas_trabajadas.get())
        except ValueError:
            messagebox.showerror("Error", "Salario por hora y horas trabajadas deben ser números válidos")
            return
        
        # Crear diccionario con datos del empleado
        empleado = {
            "nombre": self.var_nombre.get(),
            "apellido": self.var_apellido.get(),
            "cedula": self.var_cedula.get(),
            "fecha_nacimiento": self.var_fecha_nac.get(),
            "direccion": self.var_direccion.get(),
            "telefono": self.var_telefono.get(),
            "email": self.var_email.get(),
            "estado_civil": self.var_estado_civil.get(),
            "educacion": self.var_educacion.get(),
            "cargo": self.var_cargo.get(),
            "salario_hora": salario_hora,
            "horas_trabajadas": horas_trabajadas,
            "fecha_ingreso": self.var_fecha_ingreso.get(),
            "emergencia_nombre": self.var_emergencia_nombre.get(),
            "emergencia_telefono": self.var_emergencia_telefono.get(),
            "asistencias": []
        }
        
        # Verificar si el empleado ya existe
        for i, emp in enumerate(self.empleados):
            if emp["cedula"] == empleado["cedula"]:
                self.empleados[i] = empleado  # Actualizar
                messagebox.showinfo("Éxito", "Empleado actualizado correctamente")
                self.limpiar_formulario()
                self.mostrar_todos()
                self.guardar_datos()
                return
        
        # Si no existe, agregar nuevo
        self.empleados.append(empleado)
        messagebox.showinfo("Éxito", "Empleado registrado correctamente")
        self.limpiar_formulario()
        self.mostrar_todos()
        self.guardar_datos()
    
    def limpiar_formulario(self):
        self.var_nombre.set("")
        self.var_apellido.set("")
        self.var_cedula.set("")
        self.var_fecha_nac.set("")
        self.var_direccion.set("")
        self.var_telefono.set("")
        self.var_email.set("")
        self.var_estado_civil.set("")
        self.var_educacion.set("")
        self.var_cargo.set("")
        self.var_salario_hora.set(0.0)
        self.var_horas_trabajadas.set(8.0)
        self.var_fecha_ingreso.set("")
        self.var_emergencia_nombre.set("")
        self.var_emergencia_telefono.set("")
    
    def mostrar_todos(self):
        self.tree.delete(*self.tree.get_children())
        for emp in self.empleados:
            sueldo_dia = emp["salario_hora"] * emp["horas_trabajadas"]
            self.tree.insert("", "end", values=(
                emp["cedula"],
                emp["nombre"],
                emp["apellido"],
                emp["cargo"],
                f"${emp['salario_hora']:.2f}",
                f"{emp['horas_trabajadas']:.1f}",
                f"${sueldo_dia:.2f}"
            ))
    
    def buscar_empleado(self):
        termino = self.var_buscar.get().lower()
        if not termino:
            self.mostrar_todos()
            return
        
        self.tree.delete(*self.tree.get_children())
        for emp in self.empleados:
            if (termino in emp["nombre"].lower() or 
                termino in emp["apellido"].lower() or 
                termino in emp["cedula"].lower() or 
                termino in emp["cargo"].lower()):
                
                sueldo_dia = emp["salario_hora"] * emp["horas_trabajadas"]
                self.tree.insert("", "end", values=(
                    emp["cedula"],
                    emp["nombre"],
                    emp["apellido"],
                    emp["cargo"],
                    f"${emp['salario_hora']:.2f}",
                    f"{emp['horas_trabajadas']:.1f}",
                    f"${sueldo_dia:.2f}"
                ))
    
    def mostrar_detalles(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un empleado")
            return
        
        item = self.tree.item(seleccion[0])
        cedula = item["values"][0]
        
        for emp in self.empleados:
            if emp["cedula"] == cedula:
                detalles = f"""Nombre: {emp['nombre']} {emp['apellido']}
Cédula: {emp['cedula']}
Fecha Nacimiento: {emp['fecha_nacimiento']}
Dirección: {emp['direccion']}
Teléfono: {emp['telefono']}
Email: {emp['email']}
Estado Civil: {emp['estado_civil']}
Educación: {emp['educacion']}
Cargo: {emp['cargo']}
Salario por Hora: ${emp['salario_hora']:.2f}
Horas Trabajadas por Día: {emp['horas_trabajadas']:.1f}
Sueldo Diario: ${emp['salario_hora'] * emp['horas_trabajadas']:.2f}
Fecha de Ingreso: {emp['fecha_ingreso']}
Contacto Emergencia: {emp['emergencia_nombre']} - {emp['emergencia_telefono']}"""
                
                messagebox.showinfo("Detalles del Empleado", detalles)
                return
    
    def eliminar_empleado(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un empleado")
            return
        
        item = self.tree.item(seleccion[0])
        cedula = item["values"][0]
        
        confirmacion = messagebox.askyesno("Confirmar", f"¿Eliminar al empleado con cédula {cedula}?")
        if confirmacion:
            self.empleados = [emp for emp in self.empleados if emp["cedula"] != cedula]
            self.guardar_datos()
            self.mostrar_todos()
            messagebox.showinfo("Éxito", "Empleado eliminado correctamente")
    
    def exportar_csv(self):
        try:
            with open("empleados.csv", "w", encoding="utf-8") as f:
                f.write("Cédula,Nombre,Apellido,Cargo,Salario/Hora,Horas/Día,Sueldo/Día\n")
                for emp in self.empleados:
                    sueldo_dia = emp["salario_hora"] * emp["horas_trabajadas"]
                    f.write(f"{emp['cedula']},{emp['nombre']},{emp['apellido']},{emp['cargo']},"
                            f"{emp['salario_hora']:.2f},{emp['horas_trabajadas']:.1f},{sueldo_dia:.2f}\n")
            
            messagebox.showinfo("Éxito", "Datos exportados a empleados.csv")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {str(e)}")
    
    def registrar_asistencia(self):
        cedula = self.var_cedula_asistencia.get()
        fecha = self.var_fecha_asistencia.get()
        
        if not cedula or not fecha:
            messagebox.showerror("Error", "Cédula y fecha son campos obligatorios")
            return
        
        try:
            horas = float(self.var_horas_asistencia.get())
            if horas <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Horas trabajadas debe ser un número positivo")
            return
        
        # Buscar empleado
        empleado = None
        for emp in self.empleados:
            if emp["cedula"] == cedula:
                empleado = emp
                break
        
        if not empleado:
            messagebox.showerror("Error", "No se encontró el empleado con esa cédula")
            return
        
        # Registrar asistencia
        salario_dia = empleado["salario_hora"] * horas
        asistencia = {
            "fecha": fecha,
            "horas": horas,
            "salario_dia": salario_dia
        }
        
        empleado["asistencias"].append(asistencia)
        self.guardar_datos()
        
        # Mostrar en el treeview
        self.tree_asistencia.insert("", "end", values=(
            fecha,
            cedula,
            f"{empleado['nombre']} {empleado['apellido']}",
            f"{horas:.1f}",
            f"${salario_dia:.2f}"
        ))
        
        messagebox.showinfo("Éxito", "Asistencia registrada correctamente")
        self.var_horas_asistencia.set(8.0)
    
    def cargar_asistencias(self):
        self.tree_asistencia.delete(*self.tree_asistencia.get_children())
        for emp in self.empleados:
            for asist in emp["asistencias"]:
                self.tree_asistencia.insert("", "end", values=(
                    asist["fecha"],
                    emp["cedula"],
                    f"{emp['nombre']} {emp['apellido']}",
                    f"{asist['horas']:.1f}",
                    f"${asist['salario_dia']:.2f}"
                ))

if __name__ == "__main__":
    root = tk.Tk()
    app = AppRegistroEmpleados(root)
    root.mainloop()