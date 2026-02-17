import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        # Creación de widgets
        self.account_label = QtWidgets.QLabel('Número de Cuenta')
        self.account_input = QtWidgets.QLineEdit()
        
        self.password_label = QtWidgets.QLabel('Contraseña')
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.terms_checkbox = QtWidgets.QCheckBox('Aceptar términos y condiciones')
        
        self.login_button = QtWidgets.QPushButton('Iniciar Sesión')
        self.forgot_password_button = QtWidgets.QPushButton('Recuperar Contraseña')
        
        # Diseño del formulario
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(self.account_label, self.account_input)
        form_layout.addRow(self.password_label, self.password_input)
        
        # Diseño de botones y casilla de verificación
        vbox = QtWidgets.QVBoxLayout()
        vbox.addLayout(form_layout)
        vbox.addWidget(self.terms_checkbox)
        vbox.addWidget(self.login_button)
        vbox.addWidget(self.forgot_password_button)
        
        self.setLayout(vbox)
        
        # Conexiones
        self.login_button.clicked.connect(self.login)
        self.forgot_password_button.clicked.connect(self.recover_password)
        
        self.setWindowTitle('Login de Banco')
        self.setGeometry(100, 100, 300, 200)
        self.show()
        
    def login(self):
        account = self.account_input.text()
        password = self.password_input.text()
        terms_accepted = self.terms_checkbox.isChecked()
        
        if terms_accepted:
            QtWidgets.QMessageBox.information(self, 'Login Info', f'Cuenta: {account}\nContraseña: {password}\nTérminos aceptados: {terms_accepted}')
        else:
            QtWidgets.QMessageBox.warning(self, 'Advertencia', 'Debes aceptar los términos y condiciones')
    
    def recover_password(self):
        email, ok = QtWidgets.QInputDialog.getText(self, 'Recuperación de Contraseña', 
                                                   'Introduce tu correo electrónico:')
        
        if ok:
            QtWidgets.QMessageBox.information(self, 'Recuperación de Contraseña', f'Se ha enviado un correo de recuperación a: {email}')
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
