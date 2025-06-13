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

        # |-----------------Part corresponding to the Input field corresponding to the choosing volume part ----------------------------------------------|
        # GroupBox with sound button
        sound_box = QGroupBox("Choose a sound to play")
        sound_layout = QVBoxLayout()

        choosingVolume_layout = QGridLayout()

        # Set volume
        self.choosing_volume_label = QLabel("Volume :")
        self.choosing_volume_input_field = QLineEdit() # Create a input line to put text
        self.choosing_volume_button = QPushButton("Choisir le volume")

        # Create a layout where the widget will be put 
        choosingVolume_layout.addWidget(self.choosing_volume_label)
        choosingVolume_layout.addWidget(self.choosing_volume_input_field)
        choosingVolume_layout.addWidget(self.choosing_volume_button)
        # Create a box to contain these in the UI
        choosing_volume = QGroupBox("Volume Set up")
        choosing_volume.setLayout(choosingVolume_layout)

        # Make the button with typing set the corresponding volume
        self.choosing_volume_button.clicked.connect(self.set_volume_from_text )

        layout.addWidget(choosing_volume)

        # |-----------------------------------------------------------------------------------------------------------------------------------------|

        #Put the appropriate sound for the right button
        for label, sound_id in self.preset_sounds_mp3.items():
            btn = QPushButton(label)
            btn.clicked.connect(lambda _, s=sound_id: self.play_sound(s))
            sound_layout.addWidget(btn)

        sound_box.setLayout(sound_layout)
        layout.addWidget(sound_box)


        # |-----------------Part corresponding to the Input field corresponding to the choosen sound playing part ----------------------------------------------|
        choosingSound_layout = QGridLayout()

        # Choose Sound to play
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

        # Make the button with typing launch the corresponding sound
        self.choosing_sound_button.clicked.connect( self.play_sound_from_text )

        layout.addWidget(choosing_sound)
        # |-----------------------------------------------------------------------------------------------------------------------------------------------------|

        
        self.setLayout(layout)

    def play_sound(self, sound_name):
        try:
            if self.marty:
                playChoosenSound(self.marty, sound_name) # Call the playChoosenSound function from playSound.py that play sound from the corresponding sound when the appropriate button is clicked
                print(f"Playing sound: {sound_name}")
            else:
                print("Marty not connected.")
        except Exception as e:
            print(f"Error playing sound '{sound_name}': {e}")

    def play_sound_from_text(self) :
        sound_to_play = self.choosing_sound_input_field.text() # Takes the input field value as a string
        try:
            playChoosenSound(self.marty, sound_to_play) # Call the playChoosenSound function from playSound.py that play sound from a string 
        except Exception as e:
            print(f"Error playing sound from text': {e}")

    def set_volume_from_text(self) : 
        choosen_volume_to_change = self.choosing_volume_input_field.text() # Takes the input field value as a string because we need to apply the int() function
        if choosen_volume_to_change :
            int_choosen_volume_to_change = int(choosen_volume_to_change) # Marty setVolume property takes int values
            setVolumeFromInput(self.marty, int_choosen_volume_to_change); # Call the setVolumeFromInput function from playSound.py
        else : 
            print("Choosen Volume is None")



