import pyaudio
import wave
import sys

def play_wav(file_path) -> None:
    '''
    播放.wav文件
    '''
    chunk = 1024
    wf = wave.open(file_path, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
    
    data = wf.readframes(chunk)
    
    while len(data) > 0:
        stream.write(data)
        data = wf.readframes(chunk)
    
    stream.stop_stream()
    stream.close()
    
    p.terminate()
    pass

 
if __name__ == '__main__':
    play_wav("wav_files\sound_contract.wav")
