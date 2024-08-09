from PIL import Image
from PIL import ImageFilter

#memuat gaambar
Image = Image.open('foto formal.jpeg')

#menyimmpan gambar

Image.save('foto formal.jpeg')


#CROPPING 
cropped_Image = Image.crop((10,10,200,200))
cropped_Image.save('foto formal.jpeg')

#RESIZING
resized_Image = cropped_Image.resize((100, 100))
resized_Image.save('foto formal.jpeg')

#FILTERING
filtered_Image = resized_Image.filter(ImageFilter.BLUR)
filtered_Image.save('foto formal.jpeg')