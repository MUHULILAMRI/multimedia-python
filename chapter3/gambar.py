import tkinter as tk
from PIL import Image, ImageTk

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Memuat gambar menggunakan Pillow
image = Image.open('Shopee-Food-Symbol.png')
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Menjalankan loop acara Tkinter
root.mainloop()