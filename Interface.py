import sys
from martypy import Marty, MartyConnectException 
from Expression import *
from PyQt6.QtWidgets import ( 
    QApplication, QWidget, QListWidget, QListWidgetItem, QLabel,
    QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QStackedWidget, QSlider, QGroupBox, QGridLayout
)
from PyQt6.QtCore import Qt 

adresse_ip = "192.168.0.100" 
marty = Marty("wifi", adresse_ip) 

def itemModification(menu_widget: QListWidget, index: int, newText: str):
    if 0 <= index < menu_widget.count():
        item = menu_widget.item(index)
        item.setText(newText)

class ClickableLabel(QLabel):
    # onClickCall will call a function we designed so when the label is clicked on it will execute the selected function

    def __init__(self, text, onClickCall=None):
        super().__init__(text)
        self.onClickCall = onClickCall

    def mousePressEvent(self, event):
        if self.onClickCall:
            self.onClickCall()

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
        if(self.marty):
            statut_robot = QPushButton("Connected")
            statut_robot.setStyleSheet("background-color: #9FE855")
        else:
            statut_robot = QPushButton("Disconnected")
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

        self.setLayout(layout)
        layout.addLayout(top_layout)
        layout.addLayout(middle_layout)
        layout.addLayout(bottom_layout)


class CreationPanel(QWidget):
    def __init__(self, marty, parent=None):
        super(CreationPanel, self).__init__(parent)

        self.menu_widget = QListWidget()
        self.marty = marty

        #Button Creation
        for i in range(5):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.menu_widget.addItem(item)
        
        # button Style (CSS)

        self.setStyleSheet("""
            QListWidget {
                color: #FFFFFF;
                background-color: #33373B;
            }

            QListWidget::item {
                height: 50px;
            }

            QListWidget::item:selected {
                background-color: #2ABf9E;
            }

            QLabel {
                background-color: #FFFFFF;
                qproperty-alignment: AlignCenter;
            }

            QPushButton {
                background-color: #2ABf9E;
                padding: 20px;
                font-size: 18px;
            }
        """)

        # button text
        itemModification(self.menu_widget, 0, "Avancer")
        itemModification(self.menu_widget, 1, "Reculer")
        itemModification(self.menu_widget, 2, "Tourner")
        itemModification(self.menu_widget, 3, "Dancer")
        itemModification(self.menu_widget, 4, "Emotion")

        # case when button click
        self.menu_widget.itemClicked.connect(self.addingCommand)

        self.command_container = QWidget()
        self.command_layout = QVBoxLayout()
        self.command_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Placeholder text
        self.placeholder_label = QLabel("Entrez vos commandes ici")
        self.command_layout.addWidget(self.placeholder_label)

        self.command_container.setLayout(self.command_layout)
        
        # scrolling zone for the command prompt
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.command_container)

        # Button to make the command
        button = QPushButton("Envoyez la liste de commande")
        button.clicked.connect(self.executeCommands)

        content_layout = QVBoxLayout()
        content_layout.addWidget(scroll_area)
        content_layout.addWidget(button)

        main_widget = QWidget()
        main_widget.setLayout(content_layout)

        layout = QHBoxLayout()
        layout.addWidget(self.menu_widget, 1)
        layout.addWidget(main_widget, 4)

        self.setLayout(layout)

    def addingCommand(self, item):

        # Delete the placeholder label to put the command label
        if self.placeholder_label is not None:
            self.command_layout.removeWidget(self.placeholder_label)
            self.placeholder_label.deleteLater()
            self.placeholder_label = None

        # Command label
        # use of a special Class to make the label clickable and delete it when click on it
        label = ClickableLabel(item.text())
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # label supression 
        def delete():
            self.command_layout.removeWidget(label)
            label.deleteLater()

        # label got deleted, the selected function for onClickCall will be delete so it will delete the label
        label.onClickCall = delete
        self.command_layout.addWidget(label)
    
    def executeCommands(self):
        # Seek all widget from the layer
        for i in range(self.command_layout.count()):
            widget = self.command_layout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                command = widget.text().lower()  # "Avancer" -> "avancer"
                # call the correct method
                method = getattr(self, command, None)
                if callable(method):
                    method()
                else:
                    print(f"Commande inconnue : {command}")
    
    def avancer(self):
        print("Avancer -> envoyer")
        move_forward(self.marty)

    def reculer(self):
        print("Reculer -> envoyer")

    def tourner(self):
        print("Tourner -> envoyer")

    def dancer(self):
        print("Dancer -> envoyer")

    def emotion(self):
        print("Emotion -> envoyer")



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Crée tes panels
        self.control_panel = ControlPanel(marty)
        self.creation_panel = CreationPanel(marty)

        # QStackedWidget pour gérer l'affichage
        self.stack = QStackedWidget()
        self.stack.addWidget(self.control_panel)  # index 0
        self.stack.addWidget(self.creation_panel) # index 1

        # Boutons cliquables pour changer de vue
        self.btn_control = QPushButton("Control Panel")
        self.btn_creation = QPushButton("Creation Panel")

        self.btn_control.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btn_creation.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        # Layout boutons
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.btn_control)
        btn_layout.addWidget(self.btn_creation)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.stack)

        self.setLayout(main_layout)
        self.setWindowTitle("Switch Panels")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    app.exec()
