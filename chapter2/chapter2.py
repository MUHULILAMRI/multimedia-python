# from PIL import Image
# from PIL import ImageFilter

# #memuat gaambar
# Image = Image.open('foto formal.jpeg')

# #menyimmpan gambar

# Image.save('foto formal.jpeg')


# #CROPPING 
# cropped_Image = Image.crop((10,10,200,200))
# cropped_Image.save('foto formal.jpeg')

# #RESIZING
# resized_Image = cropped_Image.resize((100, 100))
# resized_Image.save('foto formal.jpeg')

# #FILTERING
# filtered_Image = resized_Image.filter(ImageFilter.BLUR)
# filtered_Image.save('foto formal.jpeg')

# # Jika gambar dalam mode RGBA, ubah menjadi RGB
# if filtered_Image.mode == 'RGBA':
#     filtered_Image = filtered_Image.convert('RGB')

from PIL import ImageFilter, Image

# Membuka gambar
image = Image.open('foto formal.jpeg')

# Mengubah ukuran gambar
resized_image = image.resize((100, 100))

# Menambahkan efek blur
filtered_image = resized_image.filter(ImageFilter.BLUR)

# Menyimpan gambar hasil sebagai PNG tanpa perlu mengonversi mode warna
filtered_image.save('filtered_result.png')