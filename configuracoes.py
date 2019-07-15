'''
Para facilitar, vamos definir nesse arquivo vamos carregar todas as variaveis e 
arquivos que vamos usar ao longo do codigo, mantendo as informacoes organizadas
'''
from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'Imagens')
snd_dir = path.join(path.dirname(__file__), 'Sons')
fnt_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo.
WIDTH = 1000 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 50 # Frames por segundo

# Define algumas variaveis com as cores basicas a partir do sistema RGB (na ordem)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do jogo
INIT = 0
GAME = 1
QUIT = 2
FIM = 4
PLAYING =  0
DONE = 2

score = 0
GRAVITY = 3
lives = 3
