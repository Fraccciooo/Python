# FILE: /mi-aplicacion/mi-aplicacion/src/ui/__init__.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class EmpleadoUI(BoxLayout):
    def __init__(self, **kwargs):
        super(EmpleadoUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.center_buttons()

        self.nombre_input = TextInput(hint_text='Nombre del Empleado')
        self.cedula_input = TextInput(hint_text='Cédula')
        self.id_input = TextInput(hint_text='ID')
        self.cargo_input = TextInput(hint_text='Cargo')
        self.sueldo_input = TextInput(hint_text='Sueldo')

        self.registrar_btn = Button(text='Registrar Empleado', size_hint=(None, None), size=(200, 50))
        self.registrar_btn.bind(on_press=self.registrar_empleado)

        self.add_widget(self.nombre_input)
        self.add_widget(self.cedula_input)
        self.add_widget(self.id_input)
        self.add_widget(self.cargo_input)
        self.add_widget(self.sueldo_input)
        self.add_widget(self.registrar_btn)

    def center_buttons(self):
        self.registrar_btn.size_hint = (None, None)
        self.registrar_btn.size = (200, 50)
        self.registrar_btn.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

    def registrar_empleado(self, instance):
        nombre = self.nombre_input.text.strip()
        cedula = self.cedula_input.text.strip()
        id_empleado = self.id_input.text.strip()
        cargo = self.cargo_input.text.strip()
        sueldo = self.sueldo_input.text.strip()

        if nombre and cedula and id_empleado and cargo and sueldo:
            try:
                sueldo_float = float(sueldo)
                content = Label(text=f'Empleado: {nombre}\nCédula: {cedula}\nID: {id_empleado}\nCargo: {cargo}\nSueldo: ${sueldo_float:.2f}')
                popup = Popup(title='Registro Exitoso', content=content, size_hint=(0.5, 0.5))
                popup.open()

                self.limpiar_campos()
            except ValueError:
                self.show_error_popup('Por favor, ingrese un sueldo válido.')
        else:
            self.show_error_popup('Por favor, complete todos los campos.')

    def limpiar_campos(self):
        self.nombre_input.text = ''
        self.cedula_input.text = ''
        self.id_input.text = ''
        self.cargo_input.text = ''
        self.sueldo_input.text = ''

    def show_error_popup(self, message):
        content = Label(text=message)
        popup = Popup(title='Error', content=content, size_hint=(0.7, 0.4))
        popup.open()