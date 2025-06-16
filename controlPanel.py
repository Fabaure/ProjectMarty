from PyQt6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QGridLayout, QGroupBox, QSlider, QLineEdit, QDialog, QColorDialog, QMessageBox
)
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt
from Movement import *
from sensor import *
from Expression import *

class ControlPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.setWindowTitle("Interface de pilotage du robot Marty")

        # css for control panel


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
        self.btn_forward.clicked.connect(lambda: move_forward(self.marty, 2))
        self.btn_backward.clicked.connect(lambda: move_backward(self.marty, 2))
        self.btn_left.clicked.connect(lambda: move_left(self.marty, 1))
        self.btn_right.clicked.connect(lambda: move_right(self.marty, 1))

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
        self.btn_celebrate.clicked.connect(lambda: move_celebrate(self.marty))
        self.btn_kickL.clicked.connect(lambda: move_kickL(self.marty))
        self.btn_kickR.clicked.connect(lambda: move_kickR(self.marty))

        # Emotion controls 
        emotion_layout = QGridLayout()
        # Create emotion buttons
        self.btn_angry = QPushButton("Angryy !")
        self.btn_wide_open = QPushButton("Wide open")
        self.btn_excited = QPushButton("Excited")
        self.btn_wiggle = QPushButton("wiggle")
        self.btn_eyes_control = QPushButton("Eyes control")
        self.open_dialog_btn = QPushButton("Ouvrir contrôle couleur")
        self.calibC = QPushButton("Calibe couleur")

        # Placement in a grid layout
        emotion_layout.addWidget(self.btn_angry, 0,0)
        emotion_layout.addWidget(self.btn_wide_open,0,1)
        emotion_layout.addWidget(self.btn_excited,0,2)
        emotion_layout.addWidget(self.btn_wiggle,1,0)
        emotion_layout.addWidget(self.btn_eyes_control,1,1)
        emotion_layout.addWidget(self.open_dialog_btn, 1,2)

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
        self.open_dialog_btn.clicked.connect(self.open_color_control)

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
        animation_layout.addWidget(box_couleur)
        
        self.color_square.setPalette(QPalette(QColor("gray")))

        self.btn_run_path = QPushButton("Suivre le parcours")
        self.btn_run_path.setFixedSize(300, 120)
        self.btn_run_path.clicked.connect(self.suivre_parcours)
        movement_layout.addWidget(self.btn_run_path)

         # Add all-layouts to the main layout
        self.setLayout(layout)
        layout.addLayout(movement_layout)
        layout.addLayout(animation_layout)

    
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
        except MartyConnectException:
            print("Impossible de se connecter à Marty")
            marty = None
            self.statut_robot.setText("Disconnected")
            self.statut_robot.setStyleSheet("background-color: #E57373")
            self.robot_name.setText("Name : None")
            self.battery_label.setText("Battery : None ")

    def update_color(self, marty):
        if(self.marty):
            color_str = getColor(marty)
            print("test : " + str(color_str))
            color = QColor(color_str)
            palette = self.color_square.palette()
            palette.setColor(QPalette.ColorRole.Window, color)
            self.color_square.setPalette(palette)
        else:
            return None

    def open_color_control(self):
        dialog = ColorControlDialog(self.marty)
        dialog.exec()


    def suivre_parcours(self):
        import time
        try:
            path = "test.dance"
            taille, coordonnees = lire_fichier(path)

            for i in range(len(coordonnees)-1):
                start = coordonnees[i]
                end = coordonnees[i + 1]
                chemin = chemin_fct(start, end)

                for pos in chemin:
                    x_diff = pos[0]-start[0]
                    y_diff = pos[1]-start[1]

                    if x_diff == 1:
                        move_right(self.marty, 5)
                    elif x_diff == -1:
                        move_left(self.marty, 5)
                    elif y_diff == 1:
                        move_backward(self.marty, 6)
                    elif y_diff == -1:
                        move_forward(self.marty, 6)

                    start = pos
                    time.sleep(3)

        except Exception as e:
            print(f"Erreur dans le suivi du parcours : {e}")

        
class ColorControlDialog(QDialog):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.setWindowTitle("Contrôle de Couleur")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.color_label = QLabel("Couleur : aucune")
        layout.addWidget(self.color_label)

        self.choose_color_btn = QPushButton("Choisir une couleur")
        self.choose_color_btn.clicked.connect(self.choose_color)
        layout.addWidget(self.choose_color_btn)

        self.pattern_input = QLineEdit()
        self.pattern_input.setPlaceholderText("Entrer le pattern (1 ou 2)")
        layout.addWidget(self.pattern_input)

        self.time_input = QLineEdit()
        self.time_input.setPlaceholderText("Entrer le temps (secondes)")
        layout.addWidget(self.time_input)

        self.submit_btn = QPushButton("Lancer")
        self.submit_btn.clicked.connect(self.submit)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)
        self.color = "#000000"

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color.name()
            self.color_label.setText(f"Couleur : {self.color}")
            self.color_sans_hass = self.color.lstrip("#")
            print(self.color_sans_hass)

    def submit(self):
        pattern = self.pattern_input.text()
        time_set = self.time_input.text()
        if pattern and time_set:
            color_control(self.marty, self.color_sans_hass, pattern, time_set)
