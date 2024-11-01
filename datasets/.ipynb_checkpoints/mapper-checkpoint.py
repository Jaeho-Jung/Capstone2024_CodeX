import os
import csv

from words import WORDS

# Directories
_AUDIO_DIR = 'audio/'
_TRANSCRIPT_DIR = 'transcript/'
_OUTPUT_FILE = _TRANSCRIPT_DIR + 'train.csv'

mapping = []

for audio_file in os.listdir(_AUDIO_DIR):
    if not audio_file.endswith('.wav'):
        continue
    file_name = os.path.splitext(audio_file)[0]
    file_name_list = file_name.split('_')
    
    # words = WORDS.values()
    # transcription = [word for word in words if word in file_name_list]
    transcription = file_name_list[2]    
    
    mapping.append({'file': audio_file, 'text': transcription})

# Write to CSV
with open(_OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['file', 'text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in mapping:
        writer.writerow(item)

