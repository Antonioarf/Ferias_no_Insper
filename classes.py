#gameover_dir = path.join(path.dirname(__file__), 'Imagens', "gameover")
'''
Nesse arquivo vamos criar as classes necessarias para o jogo, comecando com 'player',
o tiro (primeiro obstaculo) e o plano de fundo
cada classe possui suas proprias caracteristicas definidas no formato self.____ 
as classes a seguir estão commentadas por partes  
'''
import pygame
import random
from os import path
from configuracoes import img_dir, snd_dir,fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, WHITE, RED, FPS, QUIT, FIM, GRAVITY, GAME



# Classe Jogador que representa o boneco
class Player(pygame.sprite.Sprite):
    
    # Afuncao __init__ define as caracteristicas gerais e o estado inicial (toda classe tem)
    def __init__(self,player_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        #agora vamos definir as caracteristicas
        self.images = player_img
        self.currentimg = 0
        #ajustando o tamanho dela 
        self.image = pygame.transform.scale(self.images[self.currentimg], (60, 103))

        # estabelecemos que o espaco ocupado eh igual ao da figura (importante para o hit)
        #ja que muitas figuras tem bordas maiores que o personagem propriamente
        self.rect = self.image.get_rect()
        

        
        # Qual a posicao inicial dele
        self.rect.centerx = 200 #eixo X
        self.rect.bottom = 400  #eixo y
        
        # Velocidade inicial
        self.speedx = 0
        self.speedy= 0
        
        # Melhora a colisao estabelecendo um raio de um circulo
        self.radius = 25
        
        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()
        # Controle de ticks de animacao: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
    
    # Toda classe tem o update para saber o que fazr a cada frame
    def update(self):
        #define o moimento (mas porenqaunto v=0)
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        #Mantem dentro da tela
        if self.rect.right >= WIDTH:
            self.rect.right = 60

        if self.rect.left <= 0:
            self.rect.left = 0
            #cria o piso
        if self.rect.bottom >= 635:
            self.rect.bottom = 635       
        #mantem o personagem sempre indo para baixo   
        self.speedy += GRAVITY
        


        #essa eh a parte referente a mudanca de imagem
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudanca de frame.
        elapsed_ticks = now - self.last_update

        # Se ja¡ estiver na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avanca um quadro.
            self.currentimg += 1

            # Verifica se ja chegou no final da animacao.
            if self.currentimg == len(self.images):
                # Se sim, recomeca
                self.currentimg=0
            self.image = self.images[self.currentimg]




#quase tudo vai ser igual aqui
class Tiro(pygame.sprite.Sprite):
    
    
    def __init__(self, tiro_img):
        
        pygame.sprite.Sprite.__init__(self)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(tiro_img, (60, 30))
        self.rect = self.image.get_rect()

        # Agora vamos usar uma funcao para retirar a borda preta
        #tente comentar essa linha para ver a mudanca
        self.image.set_colorkey(BLACK)
        
        # Qual a posicao x inicial dele
        x = 1000
        y = 600
        self.rect.centerx = x
        self.rect.bottom = y
        #definindo a velocidade dele
        self.speedx = -6
        self.speedy = 0
        
        # Melhora a colisaoo estabelecendo um raio de um circulo
        self.radius = int(self.rect.width / 2.5)
        
    def update(self):
        #faz com que o missil volte para o comeco da tela e ataque de novo
        if self.rect.left <= 0:
            self.rect.right = WIDTH
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            





            




#essa classe eh mais simples pois nao tem movimento
#cria o plano de fundo
class Back(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,back_img):
        
        pygame.sprite.Sprite.__init__(self)

        
        self.images = back_img
        self.currentimg = 0
        #agora fazemos o fundo ocupar a tela toda
        self.image = pygame.transform.scale(back_img, (1000,700))
        self.rect = self.image.get_rect()

    #toda classe tem que ter a funcao update, mas nem sempre temos o que fazer com ela
    #nesses casos, usamos o comando pass
    def update(self):      
        pass



#Agora que acabamos as classes, precisamos carregar os assets
#os assets sao os arquivos de imagem e som que vao representar cada classe
#pra isso importamos de novo as pastas com esses arquivos
def load_assets(img_dir, snd_dir, fnt_dir):
    assets = {}
    #As imagens
    assets["game_over"] = pygame.image.load(path.join(img_dir, "gameover1.png")).convert()
    assets ["background_init"] = pygame.image.load(path.join(img_dir, 'imagem 1.jpeg')).convert()
    assets["background"] = pygame.image.load(path.join(img_dir, 'imagem de fundo_ 1.jpg')).convert()
    assets["parado"] = pygame.image.load(path.join(img_dir, 'boneco_1.png')).convert()
    assets["canhao"] = pygame.image.load(path.join(img_dir, 'bala.png')).convert()
    assets["back_init"] = pygame.image.load(path.join(img_dir, 'imagem 1.jpeg')).convert()
    #Uma fonte para escrevermos na tela (por enquanto nao estamos usando)
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    #Um primeiro arquivo de som
    assets["musica_fim"] = pygame.mixer.Sound(path.join(snd_dir, 'Game Over Sound Effects High Quality-[AudioTrimmer.com].ogg'))


    #para o boneco, vamos criar um loop que vai trocando qual a imagem
    boneco_anim = []
    #com sao 5 imagens, o loop vai ate 5
    for i in range(5):
        #a funcao format(i) substitui o valor de i nas chaves
        filename = 'boneco_{}.png'.format(i)
        #agora editamos a imagem como fizemos com todas as classes
        img0 = pygame.image.load(path.join(img_dir,filename)).convert()
        img0 = pygame.transform.scale(img0, (60, 103))        
        img0.set_colorkey(BLACK)
        boneco_anim.append(img0)
    assets["boneco_anim"] = boneco_anim
    
    

    return assets
