import numpy as np
from scipy.io.wavfile import write
samplerate = 44000
data = np.array([0,0])

x = 2000

s = np.sin(range(x))

c = 0
j = 0
l = []
for i in range(samplerate):
    if c >= (samplerate/x):
        c = 0
        j = j + 1
    l.append(s[j])
    c = c + 1
    
for i in range(samplerate): 
    t = [(l[i]*8000), 0]
    data = np.vstack([data, t])

write("samples/rising.wav", samplerate, data.astype(np.int16))