import time
import inputs
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt, QTimer
from Controller import handle_gamepad_event

class GamepadInterface(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.setWindowTitle("Contrôle Gamepad")
        self.setGeometry(300, 300, 400, 300)

        self.marty = marty
        self.arrows = {
            "UP": QLabel("↑", self),
            "DOWN": QLabel("↓", self),
            "LEFT": QLabel("←", self),
            "RIGHT": QLabel("→", self),
        }

        layout = QGridLayout()
        layout.addWidget(self.arrows["UP"], 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.arrows["LEFT"], 1, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.arrows["RIGHT"], 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.arrows["DOWN"], 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)

        for label in self.arrows.values():
            label.setFont(QFont("Arial", 48))
            self.set_arrow_color(label, "gray")

        self.setLayout(layout)

        # Timer pour vérifier la manette régulièrement
        self.timer = QTimer()
        self.timer.timeout.connect(self.listen_gamepad)
        self.timer.start(50)  # Vérifie toutes les 50ms

    def set_arrow_color(self, label: QLabel, color: str):
        palette = label.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor(color))
        label.setPalette(palette)

    def flash_arrow(self, direction: str):
        label = self.arrows.get(direction)
        if label:
            self.set_arrow_color(label, "green")
            QTimer.singleShot(200, lambda: self.set_arrow_color(label, "gray"))

    def listen_gamepad(self):
        try:
            events = inputs.get_gamepad()
        except Exception as e:
            print("Erreur manette :", e)
            return

        for event in events:
            direction = handle_gamepad_event(self.marty, event)
            if direction:
                self.flash_arrow(direction)