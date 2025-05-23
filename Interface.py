import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QSlider, QGroupBox, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
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
        self.setFixedSize(1000, 800)
        self.interface()

    def interface(self):
        layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        middle_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        robot_info = QGridLayout()
        self.robot_name = QLabel("Name : None" )
        self.battery_label = QLabel("Battery : None")
        self.statut_robot = QPushButton("Disconnected")
        self.statut_robot.setStyleSheet("background-color: #E57373")
        robot_info.addWidget(self.robot_name)
        robot_info.addWidget(self.battery_label)
        robot_info.addWidget(self.statut_robot)
        top_layout.addLayout(robot_info)

        self.statut_robot.clicked.connect(lambda: move_forward(self.marty))

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
        

        connexion_layout = QGridLayout()
        self.label = QLabel("Adresse IP :")
        self.input_field = QLineEdit()

        self.button = QPushButton("Ok")
        self.button.clicked.connect(self.connect)
        connexion_layout.addWidget(self.label)
        connexion_layout.addWidget(self.input_field)
        connexion_layout.addWidget(self.button)
        connexion = QGroupBox("Connexion")
        connexion.setLayout(connexion_layout)
        top_layout.addWidget(connexion)

        '''
        self.color_square = QLabel()
        self.color_square.setFixedSize(200, 200)
        self.color_square.setAutoFillBackground(True)

        layout.addWidget(self.color_square, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

        self.update_color("gray")


        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)
        '''
        self.setLayout(layout)


        layout.addLayout(top_layout)
        layout.addLayout(middle_layout)
        layout.addLayout(bottom_layout)



    def connect(self):
        texte = self.input_field.text()
        try:
            marty = Marty("wifi", texte) 
            print("Marty connecté !")
            self.marty = marty
            self.statut_robot.setText("Connected")
            self.statut_robot.setStyleSheet("background-color: #9FE855")
            self.robot_name.setText("Name : " + getName(self.marty))
            self.battery_label.setText("Battery : " + getBattery(self.marty) + " %")
        except MartyConnectException as e:
            print("Impossible de se connecter à Marty")
            marty = None
            self.statut_robot.setText("Disconnected")
            self.statut_robot.setStyleSheet("background-color: #E57373")
            self.robot_name.setText("Name : None")
            self.battery_label.setText("Battery : None ")