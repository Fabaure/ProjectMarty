from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QGridLayout, QGroupBox, QSlider
)
from PyQt6.QtCore import Qt
from Movement import *
from Expression import *

class ControlPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.setWindowTitle("Interface de pilotage du robot Marty")

        self.setStyleSheet("""
            QPushButton { background-color: #fff; padding: 15px; font-size: 15px; border-radius:10px }
        """)

        self.interface()

    def interface(self):
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        middle_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        buttonM_layout = QGridLayout()
        self.btn_forward = QPushButton("Move forward")
        self.btn_backward = QPushButton("Move backward")
        self.btn_right = QPushButton("Move right")
        self.btn_left = QPushButton("Move left")

        buttonM_layout.addWidget(self.btn_forward, 0, 0)
        buttonM_layout.addWidget(self.btn_backward, 0, 1)
        buttonM_layout.addWidget(self.btn_right, 1, 0)
        buttonM_layout.addWidget(self.btn_left, 1, 1)

        for i in range(buttonM_layout.count()):
            widget = buttonM_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(300, 120)

        movement_box = QGroupBox("Controls")
        movement_box.setLayout(buttonM_layout)
        middle_layout.addWidget(movement_box)

        self.btn_forward.clicked.connect(lambda: move_forward(self.marty))
        self.btn_backward.clicked.connect(lambda: move_backward(self.marty))
        self.btn_left.clicked.connect(lambda: move_left(self.marty))
        self.btn_right.clicked.connect(lambda: move_right(self.marty))

        anim_layout = QGridLayout()
        self.btn_dance = QPushButton("Dance !")
        self.btn_celebrate = QPushButton("Celebrate")
        self.btn_kickL = QPushButton("Kick Left")
        self.btn_kickR = QPushButton("Kick Right")
        anim_layout.addWidget(self.btn_dance, 0, 0)
        anim_layout.addWidget(self.btn_celebrate, 0, 1)
        anim_layout.addWidget(self.btn_kickL, 1, 0)
        anim_layout.addWidget(self.btn_kickR, 1, 1)

        for i in range(anim_layout.count()):
            widget = anim_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(150, 60)

        anim_box = QGroupBox("Animations")
        anim_box.setLayout(anim_layout)
        bottom_layout.addWidget(anim_box)

        self.btn_dance.clicked.connect(lambda: move_dance(self.marty))

        emotion_layout = QGridLayout()
        self.btn_angry = QPushButton("Angryy !")
        self.btn_wide_open = QPushButton("Wide open")
        self.btn_excited = QPushButton("Excited")
        self.btn_wiggle = QPushButton("wiggle")
        self.btn_eyes_control = QPushButton("Eyes control")
        emotion_layout.addWidget(self.btn_angry, 0, 1)
        emotion_layout.addWidget(self.btn_wide_open, 0, 2)
        emotion_layout.addWidget(self.btn_excited, 1, 0)
        emotion_layout.addWidget(self.btn_wiggle, 1, 1)
        emotion_layout.addWidget(self.btn_eyes_control, 1, 2)

        for i in range(emotion_layout.count()):
            widget = emotion_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(150, 60)

        emotion_box = QGroupBox("Emotions")
        emotion_box.setLayout(emotion_layout)
        bottom_layout.addWidget(emotion_box)

        self.btn_angry.clicked.connect(lambda: angry(self.marty))
        self.btn_wide_open.clicked.connect(lambda: wide_open(self.marty))
        self.btn_excited.clicked.connect(lambda: excited(self.marty))
        self.btn_wiggle.clicked.connect(lambda: wiggle(self.marty))
        self.btn_eyes_control.clicked.connect(lambda: eyes_control(self.marty, 45, 100))

        self.setLayout(layout)
        layout.addLayout(top_layout)
        layout.addLayout(middle_layout)
        layout.addLayout(bottom_layout)
