import pygame
import random
from os import path

from configuracoes import img_dir, snd_dir,fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, WHITE, RED, FPS, QUIT, FIM, GRAVITY, GAME

gameover_dir = path.join(path.dirname(__file__), 'Imagens', "gameover")
# Classe Jogador que representa a nave
class Player(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,player_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        
        self.images = player_img
        self.currentimg = 0
        self.image = pygame.transform.scale(self.images[self.currentimg], (60, 103))

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        

        
        # Centraliza embaixo da tela.
        self.rect.centerx = WIDTH - 800
        self.rect.bottom = HEIGHT - 300 
        
        # Velocidade da nave
        self.speedx = 0
        self.speedy= 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = 25
        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animaÃ§Ã£o: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
    
    # Metodo que atualiza a posiÃ§Ã£o da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
#Mantem dentro da tela
        if self.rect.right >= WIDTH:
            self.rect.right = 60

        if self.rect.left <= 0:
            self.rect.left = 0
            
        self.speedy += GRAVITY
#        if self.rect.bottom <= 137:
#            self.speedy = 10
        if self.rect.bottom >= 635:
            self.rect.bottom = 635
#        if self.rect.bottom <= 500:
#            self.speedy = 10
            
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudanÃ§a de frame.
        elapsed_ticks = now - self.last_update

        # Se jÃ¡ estÃ¡ na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # AvanÃ§a um quadro.
            self.currentimg += 1

            # Verifica se jÃ¡ chegou no final da animaÃ§Ã£o.
            if self.currentimg == len(self.images):
                # Se sim, tchau explosÃ£o!
                self.currentimg=0
            self.image = self.images[self.currentimg]


                    
# Classe Mob que representa os meteoros
class HOLE(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, hole_img):
        
        x = random.randint(450,1000)
        y = 710
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(hole_img, (70, 80))
        
#        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = y
        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posiÃ§Ã£o do meteoro
    def update(self):
        
        pass


class UNIC(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, uni_anim):
        
        x =  1000
        y = random.randint(635 - 160,635 - 110) 
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.images = uni_anim
        self.currentimg = 0
        self.image = pygame.transform.scale(self.images[self.currentimg], (50 , 70))
        
#        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = y
        # Sorteia uma velocidade inicial
        self.speedx = -4
        self.speedy = 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .65 / 2)
    
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animaÃ§Ã£o: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
        
    # Metodo que atualiza a posio do meteoro
    def update(self):
        
        if self.rect.left <= 0:
            self.rect.right = WIDTH
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudanÃ§a de frame.
        elapsed_ticks = now - self.last_update

        # Se jÃ¡ estÃ¡ na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # AvanÃ§a um quadro.
            self.currentimg += 1

            # Verifica se jÃ¡ chegou no final da animaÃ§Ã£o.
            if self.currentimg == len(self.images):
                # Se sim, tchau explosÃ£o!
                self.currentimg=0
            self.image = self.images[self.currentimg]


class LIVES(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, lives_img,x):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(lives_img, (35, 40))
       
        
#        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect() 
        
        # Sorteia um lugar inicial em x
        self.rect.left = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = 635 +40  

        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posiÃ§Ã£o do meteoro
    def update(self):        
        # Se o tiro passar do inicio da tela, morre.
#        if self.rect.bottom < 0:
            #self.kill()
        pass


class BARRIL(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, bar_anim):
        
        x =  1000
        y =  670
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.images = bar_anim
        self.currentimg = 0
        self.image = pygame.transform.scale(self.images[self.currentimg], (40, 80))
        self.image.set_colorkey(BLACK)
##        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = y
        # Sorteia uma velocidade inicial
        self.speedx = -1.5
        self.speedy = 0
                                     
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
    
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()


        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
        
    # Metodo que atualiza a posição do meteoro
    def update(self):
        
        if self.rect.left <= 0:
            self.rect.right = WIDTH
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        self.image.set_colorkey(BLACK)

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:

            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.currentimg += 1

            # Verifica se já chegou no final da animação.
            if self.currentimg == len(self.images):
                # Se sim, tchau explosão!
                self.currentimg=0
            self.image = self.images[self.currentimg]
            

class Premio(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, premio_img):
        q = [635 - 110, 635]
        x = random.randint(750,900)
        y = 635 - 110
    
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(premio_img, (47, 39))
        self.image.set_colorkey(WHITE)
#        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.centerx = x
        # Sorteia um lugar inicial em y
        self.rect.bottom = y
        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0
        
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .45 / 2)

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()


        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
        
    # Metodo que atualiza a posiÃ§Ã£o do meteoro
    def update(self):
        
    	pass


class PREMIO (pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self, saco_2):
        q = [635 - 110, 635]
    
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(saco_2, (47, 39))
        self.image.set_colorkey(WHITE)
#        # Deixando transparente.
#        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        # Sorteia uma velocidade inicial
        self.speedx = 0
        self.speedy = 0


        self.rect.left = 100
        # Sorteia um lugar inicial em y
        self.rect.top = 65
        # Melhora a colisÃ£o estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .45 / 2)

        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()


        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 75
        
    # Metodo que atualiza a posiÃ§Ã£o do meteoro
    def update(self):
        
    	pass
        
class Back(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self,back_img):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        
        self.images = back_img
        self.currentimg = 0
        self.image = pygame.transform.scale(self.images[self.currentimg], (1000, 700))
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        
        # Guarda o tick da primeira imagem
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animaÃ§Ã£o: troca de imagem a cada self.frame_ticks milissegundos.
        self.frame_ticks = 350
    
    # Metodo que atualiza a posiÃ§Ã£o da navinha
    def update(self):
        
        now = pygame.time.get_ticks()

        # Verifica quantos ticks se passaram desde a ultima mudanÃ§a de frame.
        elapsed_ticks = now - self.last_update

        # Se jÃ¡ estÃ¡ na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
 
            # Marca o tick da nova imagem.
            self.last_update = now

            # AvanÃ§a um quadro.
            self.currentimg += 1
            # Verifica se jÃ¡ chegou no final da animaÃ§Ã£o.
            if self.currentimg == len(self.images):
                # Se sim, tchau explosÃ£o!
                self.currentimg=0 
            self.image = self.images[self.currentimg]



# Carrega todos os assets uma vez sÃ³.
def load_assets(img_dir, snd_dir, fnt_dir):
    assets = {}
    assets["game_over"] = pygame.image.load(path.join(img_dir, "gameover1.png")).convert()
    assets["hole_img"] = pygame.image.load(path.join(img_dir, "buraco.png")).convert()
    assets["premio_img"] = pygame.image.load(path.join(img_dir, "saco_1.png")).convert()
    assets["lives_img"] = pygame.image.load(path.join(img_dir, "coracao.png")).convert()
    assets ["background_init"] = pygame.image.load(path.join(img_dir, 'imagem 1.jpeg')).convert()
    assets["background"] = pygame.image.load(path.join(img_dir, 'imagem de fundo_ 1.jpg')).convert()
    assets["background2"] = pygame.image.load(path.join(img_dir, 'imagem de fundo_ 2.png')).convert()
    assets["background3"] = pygame.image.load(path.join(img_dir, 'imagem de fundo_ 3.png')).convert()
    assets["musica_fim"] = pygame.mixer.Sound(path.join(snd_dir, 'Game Over Sound Effects High Quality-[AudioTrimmer.com].ogg'))
    assets["pulando"] = pygame.mixer.Sound(path.join(snd_dir, 'Mario Jump - Gaming Sound Effect (HD)-[AudioTrimmer.com].ogg'))
    assets["unicornio"] = pygame.mixer.Sound(path.join(snd_dir, 'Unicorn Puking Sound effect COPYRIGHT FREE-[AudioTrimmer.com]-[AudioTrimmer.com].ogg'))
    assets["parado"] = pygame.image.load(path.join(img_dir, 'boneco_1.png')).convert()
    assets["score_font"] = pygame.font.Font(path.join(fnt_dir, "PressStart2P.ttf"), 28)
    assets["saco_2"] = pygame.image.load(path.join(img_dir, 'saco_2.png')).convert()


    bar_anim=[]
    for i in range(4):
        filename ='barril_{}.png'.format(i)
        img3 = pygame.image.load(path.join(img_dir,filename)).convert()
        img3 = pygame.transform.scale(img3, (50, 45))
        bar_anim.append(img3)
    assets["bar_anim"]=bar_anim
    
    uni_anim = []
    for i in range (10):
        filename = 'uni_{}.png'.format(i)
        img2 = pygame.image.load(path.join(img_dir,filename)).convert()
        img2 = pygame.transform.scale(img2, (80, 70))
        uni_anim.append(img2)
    assets["uni_anim"]=uni_anim
    
    back_anim = []
    for i in range (2):
        filename = 'imagem {}.jpeg'.format(i)
        img1 = pygame.image.load(path.join(img_dir,filename)).convert()
        img1 = pygame.transform.scale(img1, (1000, 700))
        back_anim.append(img1)
    assets["back_anim"]=back_anim
        
    boneco_anim = []
    for i in range(5):
        filename = 'boneco_{}.png'.format(i)
        img0 = pygame.image.load(path.join(img_dir,filename)).convert()
        img0 = pygame.transform.scale(img0, (60, 103))        
        img0.set_colorkey(BLACK)
        boneco_anim.append(img0)
    assets["boneco_anim"] = boneco_anim
    
    

    return assets