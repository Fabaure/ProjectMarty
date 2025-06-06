import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from martypy import Marty
from controlPanel import ControlPanel
from creationPanel import CreationPanel

class MainWindow(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.control_panel = ControlPanel(marty)
        self.creation_panel = CreationPanel(marty)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.control_panel)
        self.stack.addWidget(self.creation_panel)

        self.btn_control = QPushButton("Control Panel")
        self.btn_creation = QPushButton("Creation Panel")

        self.btn_control.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_creation.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_control)
        btn_layout.addWidget(self.btn_creation)

        main_layout = QVBoxLayout()
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)
        self.setWindowTitle("Switch Panels")

