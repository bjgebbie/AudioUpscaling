import cubic_spline as s
import piecewise_linear as p 
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
    precision = 10
    
    f = s.CubicSpline(X, Y)
    data = np.array([0,0])

    for x in range(len(Y) - 5):
        data = np.vstack([data, [Y[x],Y[x]]])
        c = 0
        for i in range(precision - 1):
            c = (1 / precision) + c
            k = f.interpolate(x, x + c)
            t = [k, k]
            data = np.vstack([data, t])
          


    # data = p.PiecewiseLinear(X, Y, precision).data
    


    write("./samples/upsampled_" + sys.argv[1], precision * samplerate, data.astype(np.int16))

    
if __name__ == "__main__":
    main()