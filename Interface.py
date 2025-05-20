import sys
from PyQt6.QtWidgets import QApplication, QSlider, QGroupBox, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from martypy import Marty, MartyConnectException
from Movement import *

class ControlPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.setWindowTitle("Interface de pilotage du robot Marty")
        self.setFixedSize(1000, 800)
        self.interface()

    def interface(self):
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        middle_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        robot_info = QGridLayout()
        robot_name = QLabel("Nom du robot")
        battery_label = QLabel("Battery : 100%")
        statut_robot = QPushButton("Disconnect")
        statut_robot.setStyleSheet("background-color: #E57373")
        robot_info.addWidget(robot_name)
        robot_info.addWidget(battery_label)
        robot_info.addWidget(statut_robot)
        top_layout.addLayout(robot_info)

        speed_slider = QSlider(Qt.Orientation.Horizontal)
        speed_slider.setMinimum(1)
        speed_slider.setMaximum(10)
        speed_slider.setValue(5)
        speed_label = QLabel("Speed")
        speed_layout = QVBoxLayout()
        speed_layout.addWidget(speed_label)
        speed_layout.addWidget(speed_slider)
        top_layout.addLayout(speed_layout)

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
                widget.setFixedSize(300, 120)

        anim_box = QGroupBox("Animations")
        anim_box.setLayout(anim_layout)
        bottom_layout.addWidget(anim_box)

        self.setLayout(layout)
        layout.addLayout(top_layout)
        layout.addLayout(middle_layout)
        layout.addLayout(bottom_layout)