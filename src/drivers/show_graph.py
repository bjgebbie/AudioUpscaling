from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np
import sys

# read audio samples
input_data = read("./samples/"+sys.argv[1])
# Getting amplitude data
data = input_data[1]

plt.plot(data[:, 0], label="Left channel")

plt.ylabel("Amplitude")
plt.xlabel("x")
plt.title("Wav File")
plt.show()