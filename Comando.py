'''
Este arquivo contem os comandos necessarios para executarmos o modulo Pygame no python
evitando bugs sistematicos que a biblioteca tem.
Nessa atividade, nao sera necessario editar este arquivo,
use-o apenas para rodar seu codigo
'''  
#Primeiro importamos as bibliotecas externas que iremos usar   
import pygame
import random
import time
from os import path

#aqui importamos os dados e funcoes que criamos em nossos outros arquivos
#fique atento, se mudar o nome de alguma funcao, eh preciso atualizar aqui
# from configuracoes import WIDTH, HEIGHT, INIT, GAME, QUIT, FIM, GRAVITY
# from telas import init_screen
# from telas import game_screen
# from telas import end_game


# Agora, vamos iniciar o Pygame e abrir a tela
pygame.init()
pygame.mixer.init()

# definimos o tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Coloque o nome que voce quiser para o jogo
pygame.display.set_caption("ferias No Insper")

# Como dito acima, temos que colocar o comando para o jogo sempre fechar do jeito certo
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
