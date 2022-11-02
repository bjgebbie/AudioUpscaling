from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import numpy as np

# read audio samples
input_data = read("./samples/8kHz_sample.wav")
data = input_data[1]
print(input_data[1])
# plot the sound wawve
# for x in range(len(audio)-80000):
#     plt.plot(x, audio[x][0],marker="o", markersize=2)

length = data.shape[0] / input_data[0]
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(data.shape[1])
print(data.shape[1])
# label the axes
plt.ylabel("Amplitude")
plt.xlabel("Seconds")
# set the title  
plt.title("Sample Wav")
# display the plot
plt.show()