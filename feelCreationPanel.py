from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QListWidget, QListWidgetItem
)
import os

class FeelCreationPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty


        layout = QVBoxLayout()

        # Champs d'entrée
        input_layout = QHBoxLayout()
        self.color_input = QLineEdit()
        self.color_input.setPlaceholderText("Couleur (ex: red)")
        self.emotion_input = QLineEdit()
        self.emotion_input.setPlaceholderText("Émotion (ex: angry)")
        self.hex_input = QLineEdit()
        self.hex_input.setPlaceholderText("Code hexadécimal (ex: ff0000)")

        input_layout.addWidget(self.color_input)
        input_layout.addWidget(self.emotion_input)
        input_layout.addWidget(self.hex_input)

        # Bouton d'ajout
        self.add_button = QPushButton("Ajouter")
        self.add_button.clicked.connect(self.add_line)

        # Liste des lignes
        self.line_list = QListWidget()

        # Bouton de sauvegarde
        self.save_button = QPushButton("Sauvegarder fichier .feel")
        self.save_button.clicked.connect(self.save_file)

        layout.addLayout(input_layout)
        layout.addWidget(self.add_button)
        layout.addWidget(self.line_list)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def add_line(self):
        color = self.color_input.text().strip()
        emotion = self.emotion_input.text().strip()
        hex_code = self.hex_input.text().strip()

        if not color or not emotion or not hex_code:
            return  # Optionnel: afficher un message d'erreur

        line = f"{color};{emotion};{hex_code}"
        self.line_list.addItem(QListWidgetItem(line))

        self.color_input.clear()
        self.emotion_input.clear()
        self.hex_input.clear()

    def save_file(self):
        filename = os.path.join(os.getcwd(), "emotions.feel")
        if filename:
            with open(filename, "w") as fileToWrite:
                for i in range(self.line_list.count()):
                    line = self.line_list.item(i).text()
                    fileToWrite.write(line + "\n")
            print(f"[Fichier .feel enregistré] {filename}")
