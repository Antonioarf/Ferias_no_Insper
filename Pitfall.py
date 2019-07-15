     
import pygame
import random
import time


from os import path

from configuracoes import WIDTH, HEIGHT, INIT, GAME, QUIT, FIM, GRAVITY
from telas import init_screen
from telas import game_screen
from telas import end_game


# InicializaÃ§Ã£o do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Pitfall")

# Comando para evitar travamentos.
try:
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = init_screen(screen)
        elif state == GAME:
            state, tesouro = game_screen(screen)
        elif state == FIM:
            state = end_game(screen,tesouro)
        else:
            state = QUIT
finally:
    pygame.quit()
