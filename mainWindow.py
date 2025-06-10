import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QGridLayout, QGroupBox, QLineEdit, QLabel
from martypy import Marty
from controlPanel import ControlPanel
from creationPanel import CreationPanel
from soundPanel import SoundPanel
from sensor import *

class MainWindow(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.interface()


    def interface(self):

        self.control_panel = ControlPanel(self.marty)
        self.creation_panel = CreationPanel(self.marty)
        self.sound_panel = SoundPanel(self.marty)

        self.stack = QStackedWidget()
        self.stack.addWidget(self.control_panel)
        self.stack.addWidget(self.creation_panel)
        self.stack.addWidget(self.sound_panel)

        self.btn_control = QPushButton("Control Panel")
        self.btn_creation = QPushButton("Creation Panel")
        self.btn_sound = QPushButton("Sound Panel")

        
        # Connexion layout 

        connexion_layout = QGridLayout()

        # Choose IP Address
        self.label = QLabel("Adresse IP :")
        self.ip_address_input_field = QLineEdit()
        self.connexionButton = QPushButton("Ok")

        self.connexionButton.clicked.connect(self.connect) # When connexion button is clicked, it calls the function connect
        connexion_layout.addWidget(self.label)
        connexion_layout.addWidget(self.ip_address_input_field)
        connexion_layout.addWidget(self.connexionButton)
        connexion = QGroupBox("Connexion")
        connexion.setLayout(connexion_layout)
        
        # Robot Informations

        robot_info = QGridLayout()
        self.robot_name = QLabel("Name : None" )
        self.battery_label = QLabel("Battery : None")
        self.statut_robot = QPushButton("Disconnected")
        self.statut_robot.setStyleSheet("background-color: #E57373")
        robot_info.addWidget(self.robot_name)
        robot_info.addWidget(self.battery_label)
        robot_info.addWidget(self.statut_robot)
        
        # choosing menu panel, button connectivity
        self.btn_control.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_creation.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btn_sound.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        # choosing panel set up 
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_control)
        btn_layout.addWidget(self.btn_creation)
        btn_layout.addWidget(self.btn_sound)
        
        # main page screen
        main_layout = QVBoxLayout()
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(connexion)
        main_layout.addLayout(robot_info)
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)
        self.setWindowTitle("Switch Panels")


    def connect(self):
        texte = self.ip_address_input_field.text()
        try:
            marty = Marty("wifi", texte) 
            print("Marty connecté !")
            self.marty = marty
            self.statut_robot.setText("Connected")
            self.statut_robot.setStyleSheet("background-color: #9FE855")
            self.robot_name.setText("Name : " + getName(self.marty))
            self.battery_label.setText("Battery : " + getBattery(self.marty) + " %")
            self.updateMarty(marty)
        except MartyConnectException:
            print("Impossible de se connecter à Marty")
            marty = None
            self.statut_robot.setText("Disconnected")
            self.statut_robot.setStyleSheet("background-color: #E57373")
            self.robot_name.setText("Name : None")
            self.battery_label.setText("Battery : None ")
    
    def updateMarty(self, marty):
        # Remove old panels
        self.stack.removeWidget(self.control_panel)
        self.stack.removeWidget(self.creation_panel)
        self.stack.removeWidget(self.sound_panel)

        # Create new panels with the updated marty
        self.control_panel = ControlPanel(marty)
        self.creation_panel = CreationPanel(marty)
        self.sound_panel = SoundPanel(marty)

        # Add new panels
        self.stack.addWidget(self.control_panel)
        self.stack.addWidget(self.creation_panel)
        self.stack.addWidget(self.sound_panel)



