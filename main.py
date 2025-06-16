import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from mainWindow import MainWindow  # Ton fichier principal avec MainWindow
from gamepad_interface import GamepadInterface
from martypy import Marty
from kb_interface import KeyboardInterface
from KeyboardT import keyboard_loop

def launch_interface():
    app = QApplication(sys.argv)
    marty = None  # ou initialise à None ici, sera mis à jour via l'interface
    window = MainWindow(marty)
    window.show()
    sys.exit(app.exec())

def launch_controller():
    app = QApplication(sys.argv)
    marty = None
    window = GamepadInterface(marty)
    window.show()
    sys.exit(app.exec())

def launch_keyboard():
    app = QApplication(sys.argv)
    marty = None
    window = KeyboardInterface(marty)
    window.show()
    sys.exit(app.exec())

def menu():
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Choix du mode")
    msg_box.setText("Quel mode voulez-vous utiliser ?")
    interface_btn = msg_box.addButton("Interface Graphique", QMessageBox.ButtonRole.AcceptRole)
    manette_btn = msg_box.addButton("Manette (Gamepad)", QMessageBox.ButtonRole.AcceptRole)
    keyboard_btn = msg_box.addButton("Clavier", QMessageBox.ButtonRole.AcceptRole)
    msg_box.exec()

    if msg_box.clickedButton() == interface_btn:
        launch_interface()
    elif msg_box.clickedButton() == manette_btn:
        launch_controller()
    elif msg_box.clickedButton() == keyboard_btn:
        launch_keyboard()

if __name__ == "__main__":
    menu()