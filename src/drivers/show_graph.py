from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import sys

# read audio samples
input_data = read("./samples/"+sys.argv[1])
# Getting amplitude data
data = input_data[1]
# plot the sound wawve
# for x in range(len(audio)-80000):
#     plt.plot(x, audio[x][0],marker="o", markersize=2)

plt.plot(data[:, 0], label="Left channel")

plt.ylabel("Amplitude")
plt.xlabel("x")
plt.title("Wav File")
plt.show()