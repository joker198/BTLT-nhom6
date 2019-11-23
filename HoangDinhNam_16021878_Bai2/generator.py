from scipy.io.wavfile import write
from numpy import linspace, sin, pi, int16
import numpy as np

def note(freq, len, amp=1, rate=22050):
    t = linspace(0, len, len*rate)
    data = sin(2*pi*freq*t)*amp
    return data.astype(int16)

start_freq = 440
end_freq = 880
freq_music_notes = np.geomspace(start_freq, end_freq,num=12)
label_music_notes = ['A', 'Bb', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'Ab']
print(freq_music_notes.shape)
print(label_music_notes)
leng_time = 1 # sec
rate = 22050 # sample/s

i = 0
for f in freq_music_notes:
    tone = note(f, leng_time, amp=5000)
    name_file = label_music_notes[i] + '-sound.wav'
    i+=1
    write(name_file, rate, tone)

