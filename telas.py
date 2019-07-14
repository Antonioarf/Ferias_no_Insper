import pygame
import random
from os import path

from configuracoes import img_dir, snd_dir,fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, WHITE, RED, FPS, QUIT, FIM, GRAVITY, GAME

from classes import Player, Back, load_assets,Tiro


def init_screen(screen):
    # Carrega todos os assets uma vez sÃ³ e guarda em um dicionÃ¡rio
    assets = load_assets(img_dir, snd_dir, fnt_dir)
    # VariÃ¡vel para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background_init = Back(assets["background_init"])
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(background_init)
    





    
    running = True
    while running == True:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botÃ£o, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        all_sprites.update()
        # A cada loop, redesenha o fundo e os sprites
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state


def end_game(screen,score):
    assets = load_assets(img_dir, snd_dir, fnt_dir)

    background = assets["game_over"]
    score_font = assets["score_font"]
    background_rect = background.get_rect() 
    score_font = assets["score_font"]
    
    
#    text_surface = score_font.render("X ", True, BLUE)
#    text_rect = text_surface.get_rect()
#    text_rect.left = 40
#    #posicoes do texto
#    text_rect.top = 25
#    text_rect.bottom = 70
#
#    screen.blit(text_surface, text_rect)  
    

    
    running = True
    while running == True:
        text_surface = score_font.render("Your score:", True, BLUE)
        text_rect = text_surface.get_rect()
        text_rect.left = WIDTH/2
        text_rect.top = 225
        screen.blit(text_surface, text_rect)  
        
        text_surface = score_font.render("{:0}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.left = WIDTH/2
        text_rect.top = 195

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_y:
                    pygame.mixer.music.set_volume(0) 
                    state = GAME
                    running = False
                
                if event.key == pygame.K_n:
                    state = QUIT
                    running = False
                    
        screen.fill(BLACK)
        screen.blit(background, background_rect)

        screen.blit(text_surface, text_rect)

        


        pygame.display.flip()
    return state
                
def game_screen(screen):
    # Carrega todos os assets uma vez sÃ³ e guarda em um dicionÃ¡rio
    assets = load_assets(img_dir, snd_dir, fnt_dir)

    # VariÃ¡vel para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo do jogo
    background = assets["background"]
    background_rect = background.get_rect() 
    
    #Criao personagem
    player = Player(assets["boneco_anim"])
    score_font = assets["score_font"]

#    # Carrega a fonte para desenhar o score.
#    score_font = assets["score_font"]

    # Cria um grupo de todos os sprites e adiciona.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Cria um grupo dos meteoros

    obstaculo = pygame.sprite.Group()

    #Agora o mesmo para o tiro
                    
    bala = Tiro(assets["tiro"])
    all_sprites.add(bala)
    obstaculo.add(bala)


    lives = 3
    PLAYING =  0
    DONE = 2
    contador = 0
        
    
                           
    state = PLAYING
    while state != DONE:
    # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        if state == PLAYING:
            # Processa os eventos (mouse, teclado, botÃ£o, etc).
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    state = DONE
                
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = -8
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 9
#                     Se for um espaÃ§o atira!
                    if event.key == pygame.K_SPACE:
                        player.speedy =-30
                        assets["pulando"].play()

                        
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_SPACE:
                        player.speedy =50
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        all_sprites.update()
        
        if state == PLAYING:
            hits = pygame.sprite.spritecollide(player, obstaculo, True)
            if hits:
                player.rect.left = 100 
                lives -=1 
                life.empty()
                bala = Tiro(assets["tiro"])
                all_sprites.add(bala)
                obstaculo.add(bala)
                life.draw(screen)
            
            if lives <= 0:
                player.kill()
                pygame.mixer.music.stop()
                assets["musica_fim"].play()
                return FIM, score


            # A cada loop, redesenha o fundo e os sprites
            screen.fill(BLACK)
            screen.blit(background, background_rect)
            all_sprites.draw(screen)
            life.draw(screen)


            text_surface = score_font.render("{:0}X ".format(score), True, YELLOW)
            text_rect = text_surface.get_rect()
            text_rect.left = 45

            text_rect.top = 51
            text_rect.bottom = 101

            screen.blit(text_surface, text_rect)   
            

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return QUIT, tesouros
