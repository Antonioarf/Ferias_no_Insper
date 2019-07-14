from os import path

# Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'Imagens')
snd_dir = path.join(path.dirname(__file__), 'Sons')
fnt_dir = path.join(path.dirname(__file__), 'font')

# Dados gerais do jogo.
WIDTH = 1000 # Largura da tela
HEIGHT = 700 # Altura da tela
FPS = 55 # Frames por segundo

# Define algumas variÃ¡veis com as cores bÃ¡sicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicaÃ§Ã£o
INIT = 0
GAME = 1
QUIT = 2
FIM = 4

GRAVITY = 3