import numpy as np
from scipy.io.wavfile import write
samplerate = 8000
data = np.array([0,0])

#IMPORTANT: sample rate must be higher than the note and divide it evenly
note = 2000

s = np.sin(range(note))

c = 0
j = 0
l = []
for i in range(samplerate):
    if c >= (samplerate/note):
        c = 0
        j = j + 1
    l.append(s[j])
    c = c + 1
    
for i in range(samplerate): 
    t = [(l[i]*8000), (l[i]*8000)]
    data = np.vstack([data, t])

write("samples/note.wav", samplerate, data.astype(np.int16))