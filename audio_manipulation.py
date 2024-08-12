from pydub import AudioSegment
from pydub.playback import play

def manipulate_audio(input_path, output_path):
    try:
        # Memuat file audio
        audio = AudioSegment.from_file(input_path)
        print("✅ Audio berhasil dimuat")

        # Operasi Pemotongan dengan validasi durasi
        if len(audio) > 10000:
            clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
            clipped_audio.export('clipped3_' + output_path, format='mp3')
            print("✅ Pemotongan berhasil")
        else:
            raise ValueError("Durasi audio terlalu pendek untuk dipotong 10 detik")

        # Operasi Penggabungan dengan validasi durasi
        combined_audio = audio + clipped_audio
        combined_audio.export('combined3_' + output_path, format='mp3')
        print("✅ Penggabungan berhasil")

        # Operasi Konversi Format
        audio.export('result3.wav', format='wav')
        print("✅ Konversi format berhasil")

        # Operasi Pengaturan Volume dengan validasi
        if audio.dBFS < -5:  # Mengubah threshold agar lebih fleksibel
            louder_audio = audio + 5  # Meningkatkan volume dengan level yang lebih rendah
            louder_audio.export('louder3_' + output_path, format='mp3')
            print("✅ Pengaturan volume berhasil")
        else:
            # Masih lakukan ekspor meskipun tanpa peningkatan volume
            audio.export('louder3_' + output_path, format='mp3')
            print("✅ Pengaturan volume dilewati, volume sudah cukup tinggi")

        # Operasi Pemutaran Audio
        print("🔊 Memutar audio hasil manipulasi...")
        play(audio)

    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

if __name__ == "__main__":
    manipulate_audio('tester.mp3', 'audio.mp3')
