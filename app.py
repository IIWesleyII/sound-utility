import os
from pydub import AudioSegment, effects 
import ffmpeg 

location = 'sounds'
for file in os.listdir(location):
    raw_audio = AudioSegment.from_file(f'sounds/{file}', 'wav')  
    norm_audio_amp = effects.normalize(raw_audio) 
    norm_audio_amp.export(f'normalized_sounds/norm_{file}.wav', format='wav') 

