import numpy as np
import time, sys
import os
import pathlib as pl

def playSound(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

music_notes = sys.argv[1:]
number_music_note = len(music_notes)
type_os = sys.platform
current_path = os.getcwd()

# OS == Window
if type_os.startswith("win"):
    try:
        import winsound as ws
    except Exception as ex:
        print(str(ex))
        print("Please install this module")

# OS == linux || OSX
if (type_os.startswith("linux") or type_os.startswith("darwin")):
    try:
        import pygame
        pygame.init()
    except Exception as ex:
        print(str(ex))
        print("Please install this module")

if number_music_note == 0:
    exit()
else:
    if (number_music_note > 1):
        for note in music_notes:
            filename = note + "-sound.wav"
            path_file = current_path + "/" + filename
            print(filename)

            my_file = pl.Path(path_file)
            if(my_file.is_file()):
                # OS == window
                if type_os.startswith("win"):
                    ws.PlaySound(filename, ws.SND_FILENAME)

                # OS == Linux || OSX
                if (type_os.startswith("linux") or type_os.startswith("darwin")):
                    playSound(filename)
                    time.sleep(1)

            else:
                print("not found: " + filename)
    else:
        while True:
            filename = music_notes[0] + "-sound.wav"
            path_file = current_path + "/" + filename
            print(filename)

            my_file = pl.Path(current_path + "/" + filename)
            if(my_file.is_file()):
                # OS == window
                if type_os.startswith("win"):
                    ws.PlaySound(filename, ws.SND_FILENAME)

                # OS == Linux || OSX
                if (type_os.startswith("linux") or type_os.startswith("darwin")):
                    playSound(filename)
                    time.sleep(1)

            else:
                print("not found: " + filename)
                exit()