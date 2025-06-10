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

        # css for control panel
        self.setStyleSheet("""
            QPushButton { background-color: #fff; padding: 15px; font-size: 15px; border-radius:10px }
        """)

        self.interface()

    def interface(self):
        layout = QVBoxLayout()

        # Layouts to structure the UI in 3 sections (top, middle, bottom)
        movement_layout = QHBoxLayout()
        animation_layout = QHBoxLayout()


        # Movement controls
        buttonM_layout = QGridLayout()
        # Create movement buttons
        self.btn_forward = QPushButton("Move forward")
        self.btn_backward = QPushButton("Move backward")
        self.btn_right = QPushButton("Move right")
        self.btn_left = QPushButton("Move left")

        # Placement in a grid layout
        buttonM_layout.addWidget(self.btn_forward, 0, 0)
        buttonM_layout.addWidget(self.btn_backward, 0, 1)
        buttonM_layout.addWidget(self.btn_right, 1, 0)
        buttonM_layout.addWidget(self.btn_left, 1, 1)

        # Set fixed size for movement buttons
        for i in range(buttonM_layout.count()):
            widget = buttonM_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(300, 120)

        # Group box for movement controls
        movement_box = QGroupBox("Controls")
        movement_box.setLayout(buttonM_layout)
        movement_layout.addWidget(movement_box)

        # Connect buttons to movement functions
        self.btn_forward.clicked.connect(lambda: move_forward(self.marty))
        self.btn_backward.clicked.connect(lambda: move_backward(self.marty))
        self.btn_left.clicked.connect(lambda: move_left(self.marty))
        self.btn_right.clicked.connect(lambda: move_right(self.marty))

        # Animation control
        anim_layout = QGridLayout()

        # Create animation buttons
        self.btn_dance = QPushButton("Dance !")
        self.btn_celebrate = QPushButton("Celebrate")
        self.btn_kickL = QPushButton("Kick Left")
        self.btn_kickR = QPushButton("Kick Right")

        # Placement in a grid layout
        anim_layout.addWidget(self.btn_dance, 0, 0)
        anim_layout.addWidget(self.btn_celebrate, 0, 1)
        anim_layout.addWidget(self.btn_kickL, 1, 0)
        anim_layout.addWidget(self.btn_kickR, 1, 1)

         # Set fixed size for animation buttons
        for i in range(anim_layout.count()):
            widget = anim_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(150, 60)

        # Group box for animation controls
        anim_box = QGroupBox("Animations")
        anim_box.setLayout(anim_layout)
        animation_layout.addWidget(anim_box)

        # Connect animation buttons
        self.btn_dance.clicked.connect(lambda: move_dance(self.marty))

        # Emotion controls 
        emotion_layout = QGridLayout()
        # Create emotion buttons
        self.btn_angry = QPushButton("Angryy !")
        self.btn_wide_open = QPushButton("Wide open")
        self.btn_excited = QPushButton("Excited")
        self.btn_wiggle = QPushButton("wiggle")
        self.btn_eyes_control = QPushButton("Eyes control")

        # Placement in a grid layout
        emotion_layout.addWidget(self.btn_angry, 0, 1)
        emotion_layout.addWidget(self.btn_wide_open, 0, 2)
        emotion_layout.addWidget(self.btn_excited, 1, 0)
        emotion_layout.addWidget(self.btn_wiggle, 1, 1)
        emotion_layout.addWidget(self.btn_eyes_control, 1, 2)

        # Set fixed size for emotion buttons
        for i in range(emotion_layout.count()):
            widget = emotion_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(150, 60)

        # Group box for emotion controls
        emotion_box = QGroupBox("Emotions")
        emotion_box.setLayout(emotion_layout)
        animation_layout.addWidget(emotion_box)

        # Connect emotion buttons to their functions
        self.btn_angry.clicked.connect(lambda: angry(self.marty))
        self.btn_wide_open.clicked.connect(lambda: wide_open(self.marty))
        self.btn_excited.clicked.connect(lambda: excited(self.marty))
        self.btn_wiggle.clicked.connect(lambda: wiggle(self.marty))
        self.btn_eyes_control.clicked.connect(lambda: eyes_control(self.marty, 45, 100))

         # Add all-layouts to the main layout
        self.setLayout(layout)
        layout.addLayout(movement_layout)
        layout.addLayout(animation_layout)
