import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QSlider, QGroupBox, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt
from martypy import Marty, MartyConnectException
from Movement import *
from Expression import *
from sensor import *

class ControlPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.setWindowTitle("Interface de pilotage du robot Marty")
        self.interface()

    def interface(self):
        layout = QVBoxLayout()

        middle_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        buttonM_layout = QGridLayout()
        self.btn_forward = QPushButton("Move forward")
        self.btn_backward = QPushButton("Move backward")
        self.btn_right = QPushButton("Move right")
        self.btn_left = QPushButton("Move left")

        buttonM_layout.addWidget(self.btn_forward,0,0)
        buttonM_layout.addWidget(self.btn_backward,0,1)
        buttonM_layout.addWidget(self.btn_right,1,0)
        buttonM_layout.addWidget(self.btn_left,1,1)

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

        anim_layout.addWidget(self.btn_dance, 0,0)
        anim_layout.addWidget(self.btn_celebrate,0,1)
        anim_layout.addWidget(self.btn_kickL,1,0)
        anim_layout.addWidget(self.btn_kickR,1,1)


        for i in range(anim_layout.count()):
            widget = anim_layout.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                widget.setFixedSize(150, 60)

        anim_box = QGroupBox("Animations")
        anim_box.setLayout(anim_layout)
        bottom_layout.addWidget(anim_box)

        self.btn_dance.clicked.connect(lambda: move_dance(self.marty))
        #self.btn_celebrate.clicked.connect()
        #self.btn_kickL.clicked.connect()
        #self.btn_kickR.clicked.connect()


        emotion_layout = QGridLayout()

        self.btn_angry = QPushButton("Angryy !")
        self.btn_wide_open = QPushButton("Wide open")
        self.btn_excited = QPushButton("Excited")
        self.btn_wiggle = QPushButton("wiggle")
        self.btn_eyes_control = QPushButton("Eyes control")

        emotion_layout.addWidget(self.btn_angry, 0,1)
        emotion_layout.addWidget(self.btn_wide_open,0,2)
        emotion_layout.addWidget(self.btn_excited,1,0)
        emotion_layout.addWidget(self.btn_wiggle,1,1)
        emotion_layout.addWidget(self.btn_eyes_control,1,2)

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
        self.btn_eyes_control.clicked.connect(lambda: eyes_control(self.marty,45,100))

        
        self.color_square = QLabel()
        self.color_square.setFixedSize(200, 200)
        self.color_square.setAutoFillBackground(True)

        couleur_layout = QGridLayout()
        self.btn_couleur = QPushButton("Couleur")
        couleur_layout.addWidget(self.color_square)
        couleur_layout.addWidget(self.btn_couleur)

        self.btn_couleur.clicked.connect(lambda: self.update_color(self.marty))
        
        box_couleur = QGroupBox("Couleur")
        box_couleur.setLayout(couleur_layout)
        bottom_layout.addWidget(box_couleur)
        
        self.color_square.setPalette(QPalette(QColor("gray")))

        self.setLayout(layout)

        layout.addLayout(middle_layout)
        layout.addLayout(bottom_layout)

    def update_color(self, marty):
        if(self.marty):
            color_str = getColor(marty)
            color = QColor(color_str)
            palette = self.color_square.palette()
            palette.setColor(QPalette.ColorRole.Window, color)
            self.color_square.setPalette(palette)
        else:
            return None
