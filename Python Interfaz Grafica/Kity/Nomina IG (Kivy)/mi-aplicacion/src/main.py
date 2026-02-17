"""

Kivy
Descripción: Un framework de código abierto para desarrollar 
            aplicaciones multitáctiles y multiplataforma.

Ventajas: Soporta aplicaciones en dispositivos móviles y de escritorio,
          y es ideal para aplicaciones que requieren gestos táctiles.

Uso: Aplicaciones móviles y de escritorio, especialmente aquellas 
     que requieren interfaces modernas y atractivas.

"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

from models import Empleado

class MainApp(App):
    def build(self):
        self.empleados = []
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.nombre_input = TextInput(hint_text='Nombre', multiline=False)
        self.cedula_input = TextInput(hint_text='Cédula', multiline=False)
        self.id_input = TextInput(hint_text='ID', multiline=False)
        self.cargo_input = TextInput(hint_text='Cargo', multiline=False)
        self.sueldo_input = TextInput(hint_text='Sueldo', multiline=False)

        layout.add_widget(self.nombre_input)
        layout.add_widget(self.cedula_input)
        layout.add_widget(self.id_input)
        layout.add_widget(self.cargo_input)
        layout.add_widget(self.sueldo_input)

        registrar_btn = Button(text='Registrar Empleado', size_hint=(None, None), size=(200, 50))
        registrar_btn.bind(on_press=self.registrar_empleado)
        layout.add_widget(registrar_btn)

        ver_empleados_btn = Button(text='Ver Empleados', size_hint=(None, None), size=(200, 50))
        ver_empleados_btn.bind(on_press=self.mostrar_empleados)
        layout.add_widget(ver_empleados_btn)

        return layout

    def registrar_empleado(self, instance):
        nombre = self.nombre_input.text.strip()
        cedula = self.cedula_input.text.strip()
        emp_id = self.id_input.text.strip()
        cargo = self.cargo_input.text.strip()
        sueldo = self.sueldo_input.text.strip()

        if nombre and cedula and emp_id and cargo and sueldo:
            try:
                sueldo_float = float(sueldo)
                empleado = Empleado(nombre, cedula, emp_id, cargo, sueldo_float)
                self.empleados.append(empleado)

                content = Label(text=f'Empleado {nombre} registrado con éxito.')
                popup = Popup(title='Registro Exitoso', content=content, size_hint=(0.5, 0.5))
                popup.open()
                
                self.limpiar_campos()
            except ValueError:
                self.mostrar_error('Por favor, ingrese un sueldo válido.')
        else:
            self.mostrar_error('Por favor, complete todos los campos.')

    def mostrar_empleados(self, instance):
        if not self.empleados:
            self.mostrar_error('No hay empleados registrados.')
            return

        layout = GridLayout(cols=5, row_force_default=True, row_default_height=40)
        layout.add_widget(Label(text='Nombre'))
        layout.add_widget(Label(text='Cédula'))
        layout.add_widget(Label(text='ID'))
        layout.add_widget(Label(text='Cargo'))
        layout.add_widget(Label(text='Sueldo'))

        for emp in self.empleados:
            layout.add_widget(Label(text=emp.nombre))
            layout.add_widget(Label(text=emp.cedula))
            layout.add_widget(Label(text=emp.id))
            layout.add_widget(Label(text=emp.cargo))
            layout.add_widget(Label(text=f'${emp.sueldo:.2f}'))

        popup = Popup(title='Lista de Empleados', content=layout, size_hint=(0.8, 0.8))
        popup.open()

    def mostrar_error(self, message):
        content = Label(text=message)
        popup = Popup(title='Error', content=content, size_hint=(0.7, 0.4))
        popup.open()

    def limpiar_campos(self):
        self.nombre_input.text = ''
        self.cedula_input.text = ''
        self.id_input.text = ''
        self.cargo_input.text = ''
        self.sueldo_input.text = ''

if __name__ == '__main__':
    MainApp().run()