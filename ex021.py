# FAÇA UM PROGRAMA QUE ABRA E REPRODUZA UM ARQUIVO EM MP3

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#ERRO AO CARREGAR A BIBLIOTECA PYGAME E NÃO RECONHECE O ARQUIVO MP3

