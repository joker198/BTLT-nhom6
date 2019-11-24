import numpy as np
import winsound as ws
import sys
import pathlib as pl
import os

music_notes = sys.argv[1:]
number_music_note = len(music_notes)
type_os = sys.platform
current_path = os.getcwd()

# OS == Window
if type_os.startswith("win"):
    if number_music_note == 0:
        exit()

    if (number_music_note > 1):
        for note in music_notes:
            filename = note + "-sound.wav"
            print(filename)

            my_file = pl.Path(current_path + "/" + filename)
            if(my_file.is_file()):
                ws.PlaySound(filename, ws.SND_FILENAME)
            else:
                print("not found: " + filename)
    else:
        while True:
            filename = music_notes[0] + "-sound.wav"
            print(filename)

            my_file = pl.Path(current_path + "/" + filename)
            if(my_file.is_file()):
                ws.PlaySound(filename, ws.SND_FILENAME)
            else:
                print("not found: " + filename)
                exit()
