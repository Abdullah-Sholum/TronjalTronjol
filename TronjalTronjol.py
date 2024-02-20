# import library pygame
import pygame
import sys
import os

# Inisialisasi Pygame
pygame.init()

# inisiasi variabel ukuran frame
lebar = 800
tinggi = 800

# Membuat frame
# inisiasi variabel frame
frame = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Koalisi Tronjal Tronjol")

# Mengatur path ke gambar dan backsound
gambar_path = os.path.join(os.path.dirname(__file__), 'TronjalTronjol.jpg')
backsound_path = os.path.join(os.path.dirname(__file__), 'Rick Astley - Never Gonna Give You Up (Official Music Video).mp3')

# Memuat gambar background
background = pygame.image.load(gambar_path)
background = pygame.transform.scale(background, (lebar, tinggi))

# Memuat backsound
pygame.mixer.music.load(backsound_path)
pygame.mixer.music.play(-1)  # -1 untuk memutar berulang-ulang

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Menggambar background
    frame.blit(background, (0, 0))

    # Update layar
    pygame.display.flip()
