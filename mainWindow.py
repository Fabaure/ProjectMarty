import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QGridLayout, QGroupBox, QLineEdit, QLabel
from martypy import Marty
from controlPanel import ControlPanel
from instructionListPanel import InstructionListPanel
from soundPanel import SoundPanel
from fileCreationPanel import FileCreationPanel
from feelCreationPanel import FeelCreationPanel
from sensor import *

class MainWindow(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.interface()

        self.setStyleSheet("""
            QPushButton { padding: 5px;  border-radius:10px; background-color: #fff; }
            QPushButton:pressed { background-color: #404040; color: #fff }
            QGroupBox { font-size: 18px }
            
        """)


    def interface(self):
        # Adding the different panel
        self.control_panel = ControlPanel(self.marty)
        self.instruction_list_panel = InstructionListPanel(self.marty)
        self.sound_panel = SoundPanel(self.marty)
        self.file_creation_panel = FileCreationPanel(self.marty)
        self.feel_creation_panel = FeelCreationPanel(self.marty)

        # Put the different panel in a stackedWidget
        self.stack = QStackedWidget()
        self.stack.addWidget(self.control_panel)
        self.stack.addWidget(self.instruction_list_panel)
        self.stack.addWidget(self.sound_panel)
        self.stack.addWidget(self.file_creation_panel)
        self.stack.addWidget(self.feel_creation_panel)
        
        # Button to switch to the different panel
        self.btn_control = QPushButton("Control Panel")
        self.btn_instruction_list = QPushButton("Instruction List Panel")
        self.btn_sound = QPushButton("Sound Panel")
        self.btn_file_creation = QPushButton("File Creation Panel")
        self.btn_feel_creation = QPushButton("Feel Creation Panel")

        
        # Connexion layout 

        connexion_layout = QGridLayout()

        # Choose IP Address
        self.label = QLabel("Adresse IP :")
        self.ip_address_input_field = QLineEdit() # Create the input to put text
        
        self.connexionButton = QPushButton("Ok") # button
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
        
        # choosing menu panel, button connectivity, link to the stacked widget 
        self.btn_control.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_instruction_list.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btn_sound.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        self.btn_file_creation.clicked.connect(lambda: self.stack.setCurrentIndex(3))
        self.btn_feel_creation.clicked.connect(lambda: self.stack.setCurrentIndex(4))


        # choosing panel set up 
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_control)
        btn_layout.addWidget(self.btn_instruction_list)
        btn_layout.addWidget(self.btn_sound)
        btn_layout.addWidget(self.btn_file_creation)
        btn_layout.addWidget(self.btn_feel_creation)
        
        # main page screen
        main_layout = QVBoxLayout()
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(connexion)
        main_layout.addLayout(robot_info)
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)
        self.setWindowTitle("Switch Panels")


    def connect(self):
        ipaddressText = self.ip_address_input_field.text() # take the ip address from the input text
        try:
            marty = Marty("wifi", ipaddressText) #send the ip to marty
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
        self.stack.removeWidget(self.instruction_list_panel)
        self.stack.removeWidget(self.sound_panel)
        self.stack.removeWidget(self.file_creation_panel)
        self.stack.removeWidget(self.feel_creation_panel)

        # Create new panels with the updated marty
        self.control_panel = ControlPanel(marty)
        self.instruction_list_panel = InstructionListPanel(marty)
        self.sound_panel = SoundPanel(marty)
        self.file_creation_panel = FileCreationPanel(marty)
        self.feel_creation_panel = FeelCreationPanel(marty)

        # Add new panels
        self.stack.addWidget(self.control_panel)
        self.stack.addWidget(self.instruction_list_panel)
        self.stack.addWidget(self.sound_panel)
        self.stack.addWidget(self.file_creation_panel)



