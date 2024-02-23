from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import subprocess
import json

class Window(QWidget):
    def __init__(self):
        super().__init__()
        # Parámetros de la ventana
        self.setWindowTitle("Home")
        self.setGeometry(900, 900, 800, 750)

        main_layout = QVBoxLayout(self)

        clases = QPushButton('Clases', self)
        main_layout.addWidget(clases)
        clases.clicked.connect(self.btn_clicked)

        # Agregamos un separador
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)  
        separator.setFrameShadow(QFrame.Sunken)  
        main_layout.addWidget(separator)

        # Creamos un área de desplazamiento para las imágenes de usuario
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Creamos un widget para contener las imágenes de usuario
        scroll_content = QWidget(scroll_area)
        scroll_area.setWidget(scroll_content)

        # Creamos un layout para las imágenes de usuario
        image_layout = QVBoxLayout(scroll_content)

        # Leer usuarios del json
        with open('json/students.json') as archivo_json:
            alumnos = json.load(archivo_json)

        # Usuarios
        for i in range(7):
            # Creamos un layout horizontal para cada imagen y texto
            hbox_layout = QHBoxLayout()

            # Creamos la imagen de usuario
            imagen = QPixmap("usuario.png")
            label_imagen = QLabel()
            label_imagen.setPixmap(imagen)
            hbox_layout.addWidget(label_imagen)

            # Informacion
            textname = QLabel("Nombre del alumno")
            hbox_layout.addWidget(textname)

            coursestudent = QLabel("Curso")
            hbox_layout.addWidget(coursestudent)

            # Agregamos el layout horizontal al layout de imágenes
            image_layout.addLayout(hbox_layout)

            # Boton de visualizar usuario
            def viewstudent():
                try:
                    subprocess.run(["python3", "students.py"])
                except FileNotFoundError:
                    print("File not found")
                except subprocess.CalledProcessError as e:
                    print("Error archive")


            # Warning true/false
            def show_warning():
                try:
                    subprocess.run(["python3", "alert.py"])
                except FileNotFoundError:
                    print("File not found")
                except subprocess.CalledProcessError as e:
                    print("Error archive")

            # Crea el botón de advertencia
            warning = QPushButton('Warning', self)
            warning.setMaximumWidth(50)
            image_layout.addWidget(warning)

            # Conecta el clic del botón a la función show_warning
            warning.clicked.connect(show_warning)


            visualizar = QPushButton('Student', self)
            visualizar.setMaximumWidth(100)
            image_layout.addWidget(visualizar)
            visualizar.clicked.connect(viewstudent)

            # Agregamos el layout horizontal al layout de imágenes
            image_layout.addLayout(hbox_layout)

        # Agregamos el área de desplazamiento al diseño principal
        main_layout.addWidget(scroll_area)

    def btn_clicked(self):
        try:
            # Ejecuta el archivo externo
            subprocess.run(["python3", "classes.py"])
        except FileNotFoundError:
            print(f"No se pudo encontrar el archivo classes.py.")
        except subprocess.CalledProcessError as e:
            print(f"Ocurrió un error al ejecutar el archivo: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    _window = Window()
    _window.show()
    sys.exit(app.exec())
