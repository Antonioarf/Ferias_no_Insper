'''
Nesse texto, vamos criar o loop principal do jogo 
Recomendo que leiam antes o arquvio das classes
Com as classes ja definidas, vamos projeta-las na tela e definir as 
regras para que o jogo vai seguir.
'''

#novamente, vamos importar os aquivos internos e bibliotecas externas que utilizaremos
import pygame
import random
from os import path

from configuracoes import img_dir, snd_dir,fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, WHITE, RED, FPS, QUIT, FIM, GRAVITY, INIT, PLAYING, DONE, score, lives, GAME

from classes import Player, Tiro, load_assets, Back

#Vamos comecar definindo a tela de inicio
def init_screen(screen):
    # vamo carregar aqui todos os assets 
    assets = load_assets(img_dir, snd_dir, fnt_dir)
    # criamos nosso timer do jogo
    clock = pygame.time.Clock()

    # vamos criar um objeto com as caracteristicas da clase Back
    #e com a imagem do asset "back_init
    background_init = Back(assets["back_init"])
    #essas duas linhas servem para projetar na tela esse objeto
    all_sprites = pygame.sprite.Group()
    all_sprites.add(background_init)

#Agora vamos criar a possibilidade de fechar o jogo      
    running = True
    while running == True:
        
        # Ajusta a velocidade do jogo como definido no configuracoes.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botÃ£o, etc).
        for event in pygame.event.get():
            # Verifica se voce clicou no x no canto superior
            if event.type == pygame.QUIT:
                #se sim, vamos fechar o loop
                state = QUIT
                running = False
            #para evitar erros, colocamos duas vezes (uma clicando e outra soltando o botao)
            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        #se nao tivermos fechado, vamos atualizar a imagem
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state

#agora temos que fazer a funcao para o game over
def end_game(screen,score):
    #nosso indicador de fim de jogo sera o DONE
    DONE = 2
    
    assets = load_assets(img_dir, snd_dir, fnt_dir)
    #agora trocamos o fundo pela imagem de fundo
    background = assets["game_over"]
    background_rect = background.get_rect() 

    
    running = True
    #o unico movimento possivel eh fechar o jogo
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = DONE

                    
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        pygame.display.flip()
    return state
 

#essa funcao vai ser bem longa, pois define a tela durante o jogo propriamente               
def game_screen(screen):
    # Carrega todos os assets 
    assets = load_assets(img_dir, snd_dir, fnt_dir)

    # Variavel para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    background_rect = background.get_rect()   
    
    # Cria o jogador, com as caracteristicas da classe e a animacao
    player = Player(assets["boneco_anim"])
    score_font = assets["score_font"]
    #essas duas linhas servem para projetar na tela esse objeto
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    #Agora vamos criar um grupo para o canhao
    obstaculos = pygame.sprite.Group()
    #novamente, o objeto com as caracteristia da classe
    tiro = Tiro(assets["canhao"])
    #vamos projetar
    all_sprites.add(tiro)
    obstaculos.add(tiro)


    #enquanto estivesmos jogando, essas nao as possibilidades de botoes                      
    state = PLAYING
    while state != DONE:
    # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botoes, etc).
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = DONE
                
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade do jogador (que antes era 0)
                    if event.key == pygame.K_LEFT:
                        player.speedx = -8 #indo para tras
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 8 #indo para frente
#                     Se for um espaco, pula
                    if event.key == pygame.K_SPACE:
                        player.speedy =-30
                        
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0 #para de andar
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_SPACE:
                        player.speedy =40 #cai
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada classe.
        all_sprites.update()
        #temos que recomecar o loop por causa da linha de cima
        if state == PLAYING:
            #agora vamos definir o hit
            hits = pygame.sprite.spritecollide(player, obstaculos, True)
            if hits:
                player.rect.left = 100 #volta para a esquerda
                lives -=1
                if lives > 0:
                    #se nao tiver morto, coloca com novo missil
                    tiro = Tiro(assets["canhao"])
                    all_sprites.add(tiro)
                    obstaculos.add(tiro)
                
             
            if lives <= 0:
                #se tiver morto, vamos para o game over
                player.kill()
                pygame.mixer.music.stop()
                assets["musica_fim"].play()
                return FIM, score


            # A cada loop, redesenha o fundo e os sprites
            screen.fill(BLACK)
            screen.blit(background, background_rect)
            all_sprites.draw(screen)
 
            

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return QUIT
