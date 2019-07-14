import pygame
import random
from os import path

from configuracoes import img_dir, snd_dir,fnt_dir, WIDTH, HEIGHT, BLACK, YELLOW, WHITE, RED, FPS, QUIT, FIM, GRAVITY, GAME

from classes import Player, HOLE, UNIC, LIVES, BARRIL, Premio, Back, load_assets,PREMIO


def init_screen(screen):
    # Carrega todos os assets uma vez sÃ³ e guarda em um dicionÃ¡rio
    assets = load_assets(img_dir, snd_dir, fnt_dir)
    # VariÃ¡vel para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background_init = Back(assets["back_anim"])
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(background_init)
        
    running = True
    while running:
        
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
    
    
#    text_surface = score_font.render("{:0}X ".format(tesouros), True, YELLOW)
    text_surface = score_font.render("X ", True, YELLOW)
    text_rect = text_surface.get_rect()
    text_rect.left = 40

    text_rect.top = 25

    text_rect.bottom = 70

    screen.blit(text_surface, text_rect)  
    

    
    running = True
    while running:
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
 
    pygame.mixer.music.load(path.join(snd_dir, 'LightingGrass+Wind EffectSound Test-[AudioTrimmer.com].ogg'))
    pygame.mixer.music.set_volume(0.4)
    
  # Cria uma nave. O construtor serÃ¡ chamado automaticamente.
    player = Player(assets["boneco_anim"])
    score_font = assets["score_font"]

#    # Carrega a fonte para desenhar o score.
#    score_font = assets["score_font"]

    # Cria um grupo de todos os sprites e adiciona a nave.
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Cria um grupo dos meteoros

    mobs1 = pygame.sprite.Group()
    mobs2 = pygame.sprite.Group()
    mobs3 = pygame.sprite.Group()
    mobs4 = pygame.sprite.Group()
    mobs5 = pygame.sprite.Group()
    life = pygame.sprite.Group()


    # Cria 2 meteoros e adiciona no grupo meteoros

    m = HOLE(assets["hole_img"])
    all_sprites.add(m)
    mobs1.add(m)

    w = HOLE(assets["hole_img"])

                    
    u = UNIC(assets["uni_anim"])
    all_sprites.add(u)
    mobs2.add(u)
    
    b = BARRIL(assets["bar_anim"])
    all_sprites.add(b)
    mobs3.add(b)

    p = Premio(assets["premio_img"])
    all_sprites.add(p)
    mobs4.add(p)

    p2 = PREMIO(assets["saco_2"])
    all_sprites.add(p2)
    mobs5.add(p2)


    lives = 3
    PLAYING =  0
    DONE = 2
    x = 00
    score = 0
    tesouros = 0
    contador = 0
        
    
    pygame.mixer.music.play(loops=-1)
    
    for i in  range(lives):
            
            l = LIVES(assets["lives_img"],x)
            life.add(l)
            x+=40
                           
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
#                  
            # Verifica se houve colisÃ£o entre nave e meteoro
            if player.rect.left >= 930:
                x = lives*40
                lives += 1
                l = LIVES(assets["lives_img"],x)
                life.add(l)
                life.draw(screen)
                b.rect.left = 1000 
                u.rect.left = 1000
                score += 100
                if score>= 700:
                    all_sprites.remove(w)
                    mobs1.remove(w)                   
                    u.speedx = -7
                    b.speedx =-3
                    all_sprites.add(w)
                    mobs1.add(w)
                    w.rect.left = m.rect.left +250
                if contador == 1 or contador%4 == 3: 
                    p = Premio(assets["premio_img"])
                    all_sprites.add(p)
                    mobs4.add(p)
                    p.rect.left = random.randint(750,900)
                    p.rect.bottom =  635 - 110
        
                contador +=1
                if contador % 3 == 1:
                    background = assets["background2"]
                    background_rect = background.get_rect() 
                    m.rect.left = random.randint(450,1000)
                    m.rect.bottom = 710
                            
                elif contador % 3 == 2:
                    background = assets["background3"]
                    background_rect = background.get_rect()
                    m.rect.left = random.randint(450,1000)
                    m.rect.bottom = 710
                
                elif contador % 3 == 0:
                    background = assets["background"]
                    background_rect = background.get_rect()
                    m.rect.left = random.randint(450,1000)
                    m.rect.bottom = 710
                
            for e in [mobs1, mobs2, mobs3]:
                hits = pygame.sprite.spritecollide(player, e, True)
                if hits:

                    player.rect.left = 100 
                    lives -=1 
                    life.empty()
                    if e ==  mobs1 and score <700:
                        m = HOLE(assets["hole_img"])
                        all_sprites.add(m)
                        mobs1.add(m)
                    elif e ==  mobs1 and score >=700:
                        m.kill()
                        w.kill()
                        m = HOLE(assets["hole_img"])
                        all_sprites.add(m)
                        mobs1.add(m)
                        w = HOLE(assets["hole_img"])
                        all_sprites.add(w)
                        mobs1.add(w)
                        w.rect.left = m.rect.left - random.randint(200,400)
                    if e ==  mobs2:
                        assets["unicornio"].play()
                        u = UNIC(assets["uni_anim"])
                        all_sprites.add(u)
                        mobs2.add(u)
                    if e ==  mobs3:  
                        b = BARRIL(assets["bar_anim"])
                        all_sprites.add(b)
                        mobs3.add(b)                        
                    a = 0
                    for i in  range(lives):
                         l = LIVES(assets["lives_img"],a)
                         life.add(l)
                         
                         a+=40
                    life.draw(screen)
                
                
            hits = pygame.sprite.spritecollide(player, mobs4, True)
            
            if hits: 
                tesouros += 1 
                score += 150
            if len(str(score)) == 1:
                p2.rect.left =100
            elif len(str(score)) == 3:
                p2.rect.left =150
            elif len(str(score)) == 4:
                p2.rect.left =175
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