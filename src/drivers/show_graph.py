import threading
from scipy.io.wavfile import read
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import sys
import play_sound as ps
import numpy as np

wav_file = "./samples/"+sys.argv[1]

actual = "./samples/8kHz_sample.wav"
# read audio samples

input_data = read(wav_file)
actual_data = read(actual)
# Getting amplitude data
data = input_data[1]
adata = actual_data[1]

x = range(len(data[:, 0]))
ax = range(len(adata[:, 0]))

y = data[:, 0]
ay = adata[:, 0]

x = np.asanyarray(x)
ax = np.asanyarray(ax)

smooth = make_interp_spline(x, y)
asmooth = make_interp_spline(ax, ay)

a = 100
b = 25
xa = np.linspace(x.min(), x.max(), len(x)*b)
xa2 = np.linspace(ax.min(), ax.max(), len(ax)*b)
ya = smooth(xa)
ya2 = asmooth(xa2)
plt.plot(x[89722:89822],y[89722:89822], color='b', marker='o', label='Discrete',linestyle = 'None',)

plt.plot(xa[int(89722/10*b):int(89822/10*b)]*10,ya2[int(89722/10*b):int(89822/10*b)], color='g', label='Actual')
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.title("Wav File")
x = threading.Thread(target=ps.PlaySound, args=(wav_file,))
x.start()
y = threading.Thread(target=plt.show(), args=(None,))
y.start()
y.join()
