import numpy as np
import winsound as ws
import sys

music_notes = sys.argv[1:]
number_music_note = len(music_notes)

if number_music_note == 0:
    exit()

if (number_music_note > 1):
    for note in music_notes:
        filename = note + "-sound.wav"
        print(filename)
        ws.PlaySound(filename, ws.SND_FILENAME)
else:
    while True:
        filename = music_notes[0] + "-sound.wav"
        print(filename)
        ws.PlaySound(filename, ws.SND_FILENAME)