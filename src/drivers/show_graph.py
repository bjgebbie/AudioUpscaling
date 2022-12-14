import threading
from scipy.io.wavfile import read
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import sys
import play_sound as ps
import numpy as np

wav_file = "./samples/"+sys.argv[1]

# read audio samples
input_data = read(wav_file)
# Getting amplitude data
data = input_data[1]
x = range(len(data[:, 0]))
y = data[:, 0]
x = np.asanyarray(x)

smooth = make_interp_spline(x, y)

xa = np.linspace(x.min(), x.max(), len(x)*25)
ya = smooth(xa)
plt.plot(x[:100],y[:100], color='b', marker='o', label='Discrete',linestyle = 'None',)
plt.plot(xa[:100*25],ya[:100*25], color='g', label='Actual')
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.title("Wav File")
x = threading.Thread(target=ps.PlaySound, args=(wav_file,))
x.start()
y = threading.Thread(target=plt.show(), args=(None,))
y.start()
y.join()
