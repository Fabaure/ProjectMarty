from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGroupBox, QHBoxLayout, QGridLayout, QLineEdit
from PyQt6.QtCore import Qt
from martypy import Marty
from playSound import *

class SoundPanel(QWidget):
    def __init__(self, marty):
        super().__init__()
        self.marty = marty
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        # Preset sound mp3 list for the button
        self.preset_sounds_mp3 = {
            "Pierre qui roule": "rick.mp3",
            "Mii": "wiichan.mp3",
        }

        # GroupBox contenant les boutons de sons
        sound_box = QGroupBox("Choose a sound to play")
        sound_layout = QVBoxLayout()

        for label, sound_id in self.preset_sounds_mp3.items():
            btn = QPushButton(label)
            btn.clicked.connect(lambda _, s=sound_id: self.play_sound(s))
            sound_layout.addWidget(btn)

        sound_box.setLayout(sound_layout)
        layout.addWidget(sound_box)

        choosingSound_layout = QGridLayout()

        # Choose IP Address
        self.choosing_sound_label = QLabel("Quel fichier audio lire :")
        self.choosing_sound_input_field = QLineEdit() # Create a input line to put text
        self.choosing_sound_button = QPushButton("Jouer le son")

        # Create a layout where the widget will be put 
        choosingSound_layout.addWidget(self.choosing_sound_label)
        choosingSound_layout.addWidget(self.choosing_sound_input_field)
        choosingSound_layout.addWidget(self.choosing_sound_button)
        # Create a box to contain these in the UI
        choosing_sound = QGroupBox("Son personnalise")
        choosing_sound.setLayout(choosingSound_layout)

        self.choosing_sound_button.clicked.connect( self.play_sound_from_text )

        layout.addWidget(choosing_sound)
        self.setLayout(layout)

    def play_sound(self, sound_id):
        try:
            if self.marty:
                playChoosenSound(self.marty, sound_id)
                print(f"Playing sound: {sound_id}")
            else:
                print("Marty not connected.")
        except Exception as e:
            print(sound_id)
            print(f"Error playing sound '{sound_id}': {e}")

    def play_sound_from_text(self) :
        sound_to_play = self.choosing_sound_input_field.text()
        try:
            playChoosenSound(self.marty, sound_to_play)
        except Exception as e:
            print(f"Error playing sound from text': {e}")


