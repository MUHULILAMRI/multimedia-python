import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment
import subprocess
import tempfile
import os

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Definisikan fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)

        # Membuat file sementara dengan delete=False
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio_file:
            temp_file_path = temp_audio_file.name
            audio.export(temp_file_path, format="mp3")
        
        # Memainkan audio dengan ffplay
        subprocess.call(['ffplay', '-nodisp', '-autoexit', temp_file_path])

        # Menghapus file sementara setelah pemutaran selesai
        os.remove(temp_file_path)

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()