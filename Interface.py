import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from martypy import Marty, MartyConnectException
from Movement import *

class ControlPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.setWindowTitle("Interface de pilotage du robot Marty")
        self.setFixedSize(800, 800)
        self.interface()

    def interface(self):
        layout = QVBoxLayout()

        self.btn_forward = QPushButton("Move forward")
        self.btn_backward = QPushButton("Move backward")
        self.btn_right = QPushButton("Move to right")
        self.btn_left = QPushButton("Move to left")
        self.btn_dance = QPushButton("Dance")
        
        layout.addWidget(self.btn_forward)
        layout.addWidget(self.btn_backward)
        layout.addWidget(self.btn_right)
        layout.addWidget(self.btn_left)
        layout.addWidget(self.btn_dance)


        self.btn_forward.clicked.connect(lambda: move_forward(self.marty))
        self.btn_left.clicked.connect(lambda: move_left(self.marty))
        self.btn_right.clicked.connect(lambda: move_right(self.marty))
        self.btn_dance.clicked.connect(lambda: move_dance(self.marty))

        self.setLayout(layout)