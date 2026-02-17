
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.app import App

# En este ejemplo, hemos creado una aplicación de registro de nómina simple con Kivy. 
# La aplicación tiene un título, campos de entrada para el nombre, el sueldo y la cédula del empleado, y un botón de registro.
# Cuando se hace clic en el botón de registro, se valida la entrada del usuario y se muestra un mensaje emergente 
# con los detalles del empleado registrado. Si se produce un error, se muestra un mensaje emergente de error.

# Establecer el tamaño de la ventana
Window.size = (400, 300)
class NominaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Título
        self.layout.add_widget(Label(text='Registro de Nómina', font_size=24, bold=True, size_hint_y=50, height=20))

        # Crear un GridLayout para centrar los campos de entrada
        form_layout = GridLayout(cols=1, spacing=10, size_hint_y=50)
        form_layout.bind(minimum_height=form_layout.setter("height"))

        # Campo de entrada para el nombre
        self.nombre_input = TextInput(hint_text='Nombre del Empleado', multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.nombre_input)

        # Campo de entrada para el sueldo
        self.sueldo_input = TextInput(hint_text='Sueldo', multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.sueldo_input)

        # Campo de entrada para la cedula
        self.cedula_input = TextInput(hint_text='Cedula', multiline=False, size_hint_y=None, height=40)
        form_layout.add_widget(self.cedula_input)

        # Añadir el formulario al layout principal
        self.layout.add_widget(form_layout)

        # Botón de registro centrado
        self.registrar_btn = Button(text='Registrar', size_hint_y=None, height=40, background_color=(0.2, 0.6, 0.8, 1))
        self.registrar_btn.bind(on_press=self.registrar_empleado)
        self.layout.add_widget(self.registrar_btn)

        return self.layout

    def registrar_empleado(self, instance):
        nombre = self.nombre_input.text.strip()
        sueldo = self.sueldo_input.text.strip()
        cedula = self.cedula_input.text.strip()
        
        if nombre and sueldo:
            try:
                # Convertir sueldo a float
                sueldo_float = float(sueldo)  
                content = Label(text=f'Empleado: {nombre} \nRegistrado con sueldo: ${sueldo_float:.2f}\nCedula: {self.cedula_input.text}')
                popup = Popup(title='Registro Exitoso', content=content, size_hint=(1, 0.8))
                popup.open()

                # Limpiar campos de entrada
                self.nombre_input.text = ''
                self.sueldo_input.text = ''
                self.cedula_input.text = ''
            except ValueError:
                self.show_error_popup('Por favor, ingrese un sueldo válido.')
        else:
            self.show_error_popup('Por favor, complete todos los campos.')

    def show_error_popup(self, message):
        content = Label(text=message)
        popup = Popup(title='Error', content=content, size_hint=(0.7, 0.4))
        popup.open()

if __name__ == '__main__':
    NominaApp().run()