import sys
import threading
import msvcrt
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from martypy import Marty
from Keyboard import keyboard_loop

class KeyboardInterface(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.setWindowTitle("Contrôle clavier - Marty")
        self.setGeometry(100, 100, 300, 200)

        layout = QGridLayout()
        layout.addWidget(self.make_label("Z", "Avancer"), 0, 1)
        layout.addWidget(self.make_label("Q", "Gauche"), 1, 0)
        layout.addWidget(self.make_label("S", "Reculer"), 1, 1)
        layout.addWidget(self.make_label("D", "Droite"), 1, 2)
        layout.addWidget(self.make_label("E", "Capteurs"), 2, 1)
        self.setLayout(layout)

        threading.Thread(target=keyboard_loop, args=(self.marty,), daemon=True).start()

    def make_label(self, key, text):
        label = QLabel(f"{key} → {text}")
        label.setFont(QFont("Arial", 16))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label