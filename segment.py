import os
from pydub import AudioSegment

# define the desired duration in milliseconds
DURATION_MS = 5000

# define the folder path containing the WAV files
folder_path = 'path/to/folder'

# iterate over all the WAV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        # load the audio file using pydub
        audio = AudioSegment.from_wav(os.path.join(folder_path, filename))
        
        # get the current duration of the audio file in milliseconds
        current_duration_ms = len(audio)
        
        if current_duration_ms < DURATION_MS:
            # if the audio is shorter than the desired duration, add silence to the end
            silence_duration_ms = DURATION_MS - current_duration_ms
            silence = AudioSegment.silent(duration=silence_duration_ms)
            audio = audio + silence
        elif current_duration_ms > DURATION_MS:
            # if the audio is longer than the desired duration, cut it to the desired duration
            audio = audio[:DURATION_MS]
        
        # export the modified audio file to the same folder with the same filename
        audio.export(os.path.join(folder_path, filename), format='wav')
