from pydub import AudioSegment
import pydub

pydub.AudioSegment.converter = 'c:\ffmpeg\bin\ffmpeg.exe'
f = AudioSegment.from_wav("trek.wav")

def speed_change(sound, speed=1.0):
    s = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
    return s.set_frame_rate(sound.frame_rate)\

print('Введите значение замедления >0 (<1) или ускорения (>1)')

i = input()

fast = speed_change(f, float(i))

fast.export("новая.wav", format="wav")