import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QListWidget, QListWidgetItem, QLabel,
    QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, 
)
from PyQt6.QtCore import Qt
# from martypy import Marty
from instruction import *

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
    def __init__(self):
        super().__init__()
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

        self.setLayout(layout)


class CreationPanel(QWidget):
    def __init__(self, parent=None):
        super(CreationPanel, self).__init__(parent)

        self.menu_widget = QListWidget()

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


if __name__ == "__main__":
    # adresse_ip = "192.168.0.101" # à modifier
    # marty = Marty("wifi", adresse_ip) # connexion à Marty
    app = QApplication(sys.argv)
    fenetre = CreationPanel()
    fenetre.show()
    app.exec()

