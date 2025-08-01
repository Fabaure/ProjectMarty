from PyQt6.QtWidgets import (
    QWidget, QListWidget, QListWidgetItem, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QScrollArea
)
from PyQt6.QtCore import Qt
from Movement import *
from Expression import *

def itemModification(menu_widget: QListWidget, index: int, newText: str):
    if 0 <= index < menu_widget.count():
        item = menu_widget.item(index)
        item.setText(newText)

class ClickableLabel(QLabel):
    def __init__(self, text, onClickCall=None):
        super().__init__(text)
        self.onClickCall = onClickCall

    def mousePressEvent(self, event):
        if self.onClickCall:
            self.onClickCall()

class InstructionListPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.menu_widget = QListWidget()

        for i in range(10):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.menu_widget.addItem(item)


        itemModification(self.menu_widget, 0, "Avancer")
        itemModification(self.menu_widget, 1, "Reculer")
        itemModification(self.menu_widget, 2, "TournerDroite")
        itemModification(self.menu_widget, 3, "TournerGauche")
        itemModification(self.menu_widget, 4, "Dancer")
        itemModification(self.menu_widget, 5, "Celebration")
        itemModification(self.menu_widget, 6, "PiedGauche")
        itemModification(self.menu_widget, 7, "PiedDroit")
        itemModification(self.menu_widget, 8, "Colere")
        itemModification(self.menu_widget, 9, "Exitation")
        itemModification(self.menu_widget, 10, "Chokbar")
        itemModification(self.menu_widget, 11, "Gigote")


        self.menu_widget.itemClicked.connect(self.addingCommand)

        self.command_container = QWidget()
        self.command_layout = QVBoxLayout()
        self.command_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.placeholder_label = QLabel("Entrez vos commandes ici")
        self.command_layout.addWidget(self.placeholder_label)
        self.command_container.setLayout(self.command_layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.command_container)

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
        if self.placeholder_label is not None:
            self.command_layout.removeWidget(self.placeholder_label)
            self.placeholder_label.deleteLater()
            self.placeholder_label = None

        label = ClickableLabel(item.text())
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        def delete():
            self.command_layout.removeWidget(label)
            label.deleteLater()

        label.onClickCall = delete
        self.command_layout.addWidget(label)

    def executeCommands(self):
        for i in range(self.command_layout.count()):
            widget = self.command_layout.itemAt(i).widget()
            if isinstance(widget, QLabel):
                command = widget.text().lower()
                method = getattr(self, command, None)
                if callable(method):
                    method()
                else:
                    print(f"Commande inconnue : {command}")

    def avancer(self):
        print("Avancer -> envoyer")
        move_forward(self.marty, 2)

    def reculer(self):
        print("Reculer -> envoyer")
        move_backward(self.marty, 2)

    def tournerdroite(self):
        print("TournerDroite -> envoyer")
        move_right(self.marty, 1)

    def tournergauche(self):
        print("TournerGauche -> envoyer")
        move_left(self.marty, 1)

    def dancer(self):
        print("Dancer -> envoyer")
        move_dance(self.marty)

    def celebration(self):
        print("Celebration -> envoyer")

    def piedgauche(self):
        print("PiedGauche -> envoyer")

    def pieddroit(self):
        print("PiedDroit -> envoyer")
    
    def colere(self):
        print("Colere -> envoyer")
        angry(self.marty)

    def exitation(self):
        print("Exitation -> envoyer")
        excited(self.marty)

    def chokbar(self):
        print("Chokbar -> envoyer")
        wide_open(self.marty)

    def gigote(self):
        print("Gigote -> envoyer")
        wiggle(self.marty)