from pydub import AudioSegment



audio = AudioSegment.from_file('tester.mp3')

# Menyimpan file audio
audio.export('tester.mp3', format='mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('tester.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('tester.mp3', format='mp3')

audio.export('tester.wav', format='wav')

louder_audio = audio + 50  # Meningkatkan volume sebesar 10dB
louder_audio.export('tester.mp3', format='mp3')