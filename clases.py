from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import json
import sys
import subprocess

# Leer el archivo users.json
with open('json/users.json') as archivo_json:
    usuarios_validos = json.load(archivo_json)

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Clases')
        self.setGeometry(100, 100, 200, 150)

        layout = QVBoxLayout()

        imagen = QPixmap("usuario.png")
        label_imagen = QLabel(self)
        label_imagen.setPixmap(imagen)
        layout.addWidget(label_imagen, alignment=Qt.AlignCenter)

        # Entry de usuario
        self.usuario = QLineEdit(self)
        self.usuario.setMaxLength(10)  # Establecer máximo de 20 caracteres
        self.usuario.setStyleSheet("QLineEdit { max-width: 250px; }") # Establecer el ancho máximo del QLineEdit
        self.usuario.setPlaceholderText("Username: ")  # Establecer el texto predeterminado
        layout.addWidget(self.usuario, alignment=Qt.AlignCenter)

        # Entry de contraseña
        self.passwd = QLineEdit(self)
        self.passwd.setMaxLength(15)  # Establecer máximo de 20 caracteres
        #self.passwd.setStyleSheet("QLineEdit { max-width: 200px; }") # Establecer el ancho máximo del QLineEdit
        self.passwd.setPlaceholderText("Password: ")  # Establecer el texto predeterminado
        layout.addWidget(self.passwd, alignment=Qt.AlignCenter)

        # Botón login
        self.btn = QPushButton('Login', self)
        layout.addWidget(self.btn, alignment=Qt.AlignRight)
        self.btn.clicked.connect(self.btn_clicked)   

        self.setLayout(layout)

    def btn_clicked(self):
        username = self.usuario.text()
        password = self.passwd.text()

        usuarios_no_privilegiados = usuarios_validos.get("usuarios_no_privilegiados", {})

        if username in usuarios_no_privilegiados and usuarios_no_privilegiados[username] == password:
            print("Acceso concedido")
            try:
                # Ejecuta el archivo externo
                subprocess.run(["python3", "home.py"])
            except FileNotFoundError:
                print(f"No se pudo encontrar el archivo home.py.")
            except subprocess.CalledProcessError as e:
                print(f"Ocurrió un error al ejecutar el archivo: {e}")

        else:
            print("Acceso denegado")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
