import pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar
image = pygame.image.load('naruto.jpg')

# Memuat suara
sound = pygame.mixer.Sound('audio.mp3')

# Memutar suara
sound.play()

# Loop utama permainan
running = True
x = 0  # Initialize the variable 'x'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Menggambar gambar
    screen.blit(image, (100, 100))

    # Memperbarui tampilan
    pygame.display.flip()

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()


pygame.quit()