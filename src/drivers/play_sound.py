from time import sleep
import pyaudio
import wave

class PlaySound:
    def __init__(self, wav_file) -> None:
        self.wav_file = wav_file
        #define stream chunk   
        chunk = 1024  
        #open a wav format music  
        f = wave.open(self.wav_file,"rb")  
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

