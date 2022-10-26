from scipy.io.wavfile import write, read
import pyaudio  
import wave  


def main():
    #define stream chunk   
    chunk = 1024  

    #open a wav format music  
    # f = wave.open(r"./samples/44.1kHz_sample.wav","rb")  
    # f = wave.open(r"./samples/8kHz_sample.wav","rb")  
    f = wave.open(r"./samples/44.1kHz_sample.wav","rb")  
    #instantiate PyAudio  
    p = pyaudio.PyAudio()  
    #open stream  
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                    channels = f.getnchannels(),  
                    rate = f.getframerate(),  
                    output = True)  
    #read data  
    data = f.readframes(chunk)  

    #play stream  
    while data:  
        stream.write(data)  
        data = f.readframes(chunk)  

    #stop stream  
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()

if __name__ == "__main__":
    main()