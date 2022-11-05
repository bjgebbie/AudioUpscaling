import cubic_spline as s
from scipy.io.wavfile import read, write
import sys
import numpy as np

def main():
    wav_file = "./samples/"+sys.argv[1]
    # read audio samples
    input_data = read(wav_file)
    # Getting amplitude data
    samplerate = input_data[0]
    Y = input_data[1][:, 0]
    X = range(len(Y))

    f = s.CubicSpline(X, Y)
    data = np.array([0,0])
    precision = 4

    for x in range(len(Y) - 5):
        data = np.vstack([data, [Y[x],Y[x]]])
        
        for i in range(precision - 1):
            c = (1 / precision)
            k = f.interpolate(x, x + c + (1 / precision))
            c = (1 / precision)
            k = round(k,0)
            t = [k, k]
            data = np.vstack([data, t])

    write("./samples/upsampled_" + sys.argv[1], precision * samplerate, data.astype(np.int16))

    
if __name__ == "__main__":
    main()