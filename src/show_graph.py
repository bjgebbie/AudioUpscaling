import threading
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import sys
import play_sound as ps

wav_file = "./samples/"+sys.argv[1]

# read audio samples
input_data = read(wav_file)
# Getting amplitude data
data = input_data[1]

plt.plot(data[:, 0], label="Left channel")

plt.ylabel("Amplitude")
plt.xlabel("x")
plt.title("Wav File")
x = threading.Thread(target=ps.PlaySound, args=(wav_file,))
x.start()
y = threading.Thread(target=plt.show(), args=(None,))
y.start()
y.join()
