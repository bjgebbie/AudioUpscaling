from scipy.io.wavfile import write
import numpy as np

samplerate = 8000
data = np.array([[1000,1],[-1000,1],[1000,1]])
print(data)

b = False
for i in range(16000):
    if b:
        t = [-i, 0]
    else:
        t = [i, 0]
    b = not b

    data = np.vstack([data, t])

print(data)
write("samples/rising.wav", samplerate, data.astype(np.int16))
