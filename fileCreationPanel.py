from PyQt6.QtWidgets import (
    QWidget, QListWidget, QListWidgetItem, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QScrollArea, QComboBox, QInputDialog, QTextEdit, QSizePolicy, QGridLayout, QLineEdit, QGroupBox
)
from PyQt6.QtCore import Qt
import os

class ClickableLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.onClickCall = None

    def mousePressEvent(self, event):
        if self.onClickCall:
            self.onClickCall()


def itemModification(list_widget, index, text):
    item = list_widget.item(index)
    if item:
        item.setText(text)


class FileCreationPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty

        #  Selector between Absolute and Sequential
        self.mode_selector = QComboBox()
        self.mode_selector.addItems(["Séquentiel", "Absolu"])
        self.mode_selector.currentIndexChanged.connect(self.modeChanged)
        self.mode_selector.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        # Instruction list for sequentiel
        self.menu_widget = QListWidget()
        for i in range(4):
            item = QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.menu_widget.addItem(item)

        itemModification(self.menu_widget, 0, "Avancer")
        itemModification(self.menu_widget, 1, "Reculer")
        itemModification(self.menu_widget, 2, "Gauche")
        itemModification(self.menu_widget, 3, "Droite")

        self.menu_widget.itemClicked.connect(self.addingCommand)

        # Putting commands for sequentiel
        self.command_container = QWidget()
        self.command_layout = QVBoxLayout()
        self.command_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.placeholder_label = QLabel("Entrez vos commandes ici")
        self.command_layout.addWidget(self.placeholder_label)
        self.command_container.setLayout(self.command_layout)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.command_container)

        # Layout sequentiel
        self.left_layout = QVBoxLayout()
        self.left_layout.addWidget(self.menu_widget)
        self.left_widget = QWidget()
        self.left_widget.setLayout(self.left_layout)

        self.right_layout = QVBoxLayout()
        self.right_layout.addWidget(self.scroll_area)
        self.right_widget = QWidget()
        self.right_widget.setLayout(self.right_layout)

        self.sequential_container = QWidget()
        sequential_layout = QHBoxLayout()
        sequential_layout.addWidget(self.left_widget, 1)
        sequential_layout.addWidget(self.right_widget, 4)
        self.sequential_container.setLayout(sequential_layout)

        # Layout absolute
        self.absolute_input = QTextEdit()
        self.absolute_input.setPlaceholderText("Entrez des coordonnées au format x,y (une par ligne)")
        self.absolute_container = QWidget()
        absolute_layout = QVBoxLayout()
        absolute_layout.addWidget(self.absolute_input)
        self.absolute_container.setLayout(absolute_layout)
        self.absolute_container.setVisible(False)

        # button to create file
        self.file_creation_button = QPushButton("Création d'un fichier")
        self.file_creation_button.clicked.connect(self.executeCommands)


        choosingFileName_layout = QGridLayout()

        # Choose FileName
        self.choosing_file_name_label = QLabel("Choisir le nom du fichier (Ne pas renter de caractères spéciaux ou d'espaces) : ")
        self.choosing_file_name_input_field = QLineEdit() # Create a input line to put text

        # Create a layout where the widget will be put 
        choosingFileName_layout.addWidget(self.choosing_file_name_label)
        choosingFileName_layout.addWidget(self.choosing_file_name_input_field)
        
        # Create a box to contain these in the UI
        choosing_file_name = QGroupBox("Nom du fichier")
        choosing_file_name.setLayout(choosingFileName_layout)



        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(choosing_file_name)
        main_layout.addWidget(self.mode_selector)
        main_layout.addWidget(self.sequential_container)
        main_layout.addWidget(self.absolute_container)
        main_layout.addWidget(self.file_creation_button)
        self.setLayout(main_layout)

    def modeChanged(self, index):
        mode = self.mode_selector.currentText() # Look which mode is selected
        if mode == "Absolu":
            self.sequential_container.setVisible(False) # Remove SEQ section 
            self.absolute_container.setVisible(True) # show ABS section
        else:
            self.sequential_container.setVisible(True)  # show SEQ section
            self.absolute_container.setVisible(False)   # Remove ABS section 

    def addingCommand(self, item):
        # If the current mode is "Absolu" (Absolute), do nothing and return
        if self.mode_selector.currentText() == "Absolu":
            return

        # Delete the "Entrez une commande ici" text when you add a command
        if self.placeholder_label is not None:
            self.command_layout.removeWidget(self.placeholder_label)
            self.placeholder_label.deleteLater()
            self.placeholder_label = None

        # Ask the user to enter the number of times the action will be executed 
        # QInputDialog.getInt shows a dialog with a spin box:
        # Default value is 1, minimum is 1
        count, ok = QInputDialog.getInt(self, "Séquentiel", f"How many times for '{item.text()}'?", 1, 1)
        if not ok:
            # User cancelled the dialog, so stop here
            return

        # Create a clickable label widget that displays the command name and count and center it
        label = ClickableLabel(f"{item.text()} {count}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Define a function to delete this label when clicked
        def delete():
            # Remove the label from the layout and delete it from memory
            self.command_layout.removeWidget(label)
            label.deleteLater()

        # Assign the delete function as the callback to run on clicking the label
        label.onClickCall = delete
        # Add the new label widget to the command layout
        self.command_layout.addWidget(label)

    def executeCommands(self):
        # For Sequential, put the right letter for the corresponding action
        commandExpected = {
            "Avancer": "U",
            "Reculer": "B",
            "TournerDroite": "R",
            "TournerGauche": "L",
        }

        fileToWrite = self.choosing_file_name_input_field.text()

        if fileToWrite :
            name_for_file = fileToWrite + ".dance"
            print(name_for_file)
            filename = os.path.join(os.getcwd(), name_for_file)
        else :
            filename = os.path.join(os.getcwd(), "commands.dance")

        mode = self.mode_selector.currentText()
        fileBeingWrite = open(filename, "w")

        if mode == "Séquentiel":
            fileBeingWrite.write("SEQ 3\n")
            for i in range(self.command_layout.count()):
                widget = self.command_layout.itemAt(i).widget()
                if isinstance(widget, ClickableLabel):
                    try:
                        actionToDo, times = widget.text().split(" ") # Split the input in 2 variables by using " " as a separator
                        code = commandExpected[actionToDo] # Attribute the good letter to the selected action
                        fileBeingWrite.write(f"{times} {code}\n")
                    except:
                        pass
        else:
            fileBeingWrite.write("ABS 3\n")
            lines = self.absolute_input.toPlainText().splitlines()
            for line in lines:
                try:
                    x, y = map(int, line.strip().split(","))
                    fileBeingWrite.write(f"{x} {y}\n")
                except:
                    pass

        fileBeingWrite.close()
        print("[Fichier généré]", filename)
