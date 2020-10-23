import pygame
import gamelogic
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class healthBars():
    def __init__(self, positionX, positionY, display):
        
        self._positionX = positionX
        self._positionY = positionY
        #pygame.draw.rect(display, (127,255,0), ())
        self._health = 3
        self._healthList = []
    def drawHeatlh(self):
        x = 0
        for i in range(self._health):
            pygame.draw.rect(main_screen, (127,255,100), (self._positionX + x, self._positionY, 60, 10))
            pygame.display.update()
            self._healthList.append((self._positionX + x, self._positionY))
            x += 60
        
        self._healthList.reverse()
        

    def removeHitpoint(self):
        pygame.draw.rect(main_screen, (255,0,0), (self._healthList[0][0], self._healthList[0][1], 60, 10))
        self._healthList.pop(0)
        self._health -= 1
        pygame.display.update()

class Buttons:
    def __init__(self):
        self._rockButtonX = 330
        self._rockButtonY = 393
        main_screen.blit(rockbutton, (self._rockButtonX, self._rockButtonY))
        
        self._paperButtonX = 505
        self._paperButtonY = 393
        main_screen.blit(paperbutton, (self._paperButtonX, self._paperButtonY))
        
        self._scisButtonX = 330
        self._scisButtonY = 453
        main_screen.blit(scisbutton, (self._paperButtonX, self._paperButtonY))
        
        self._quitButtonX = 505
        self._quitButtonY = 453
        main_screen.blit(quitbutton, (self._paperButtonX, self._paperButtonY))
        pygame.display.update()
        
    def rockButton(self):
        return self._rockButtonX, self._rockButtonY
    def paperButton(self):
        return self._paperButtonX, self._paperButtonY
    def scisButton(self):
        return self._scisButtonX, self._scisButtonY
    def quitButton(self):
        return self._quitButtonX, self._quitButtonY
    
def draw_healthBars():
    enemyHealthX = 70
    enemyHealthY = 95

    playerHealthX = 475
    playerHealthY = 305
    
    enemyBar = healthBars(enemyHealthX,enemyHealthY, main_screen)
    enemyBar.drawHeatlh()

    playerBar = healthBars(playerHealthX,playerHealthY, main_screen)
    playerBar.drawHeatlh()
    pygame.display.update()
    return enemyBar,playerBar

def draw_main(enemy, player):
    main_screen.blit(background, (0,0))
    enemy.drawHeatlh()
    player.drawHeatlh()
    main_screen.blit(hpBar, (10,90))
    main_screen.blit(hpBar, (413,300))
# Start pygame
pygame.init()

# Sets the size of game window
display_width = 683
display_height = 512


main_screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

pygame.display.set_caption('Rock Paper Scissors')
iconurl = resource_path('Assets/newicon.png')
newicon = pygame.image.load(iconurl)
backgroundurl = resource_path('Assets/gamebackground.png')
background = pygame.image.load(backgroundurl)

rockbuttonurl = resource_path('Assets/rockButton.png')
rockbutton = pygame.image.load(rockbuttonurl).convert()
rockbutton = pygame.transform.scale(rockbutton, (175,60))

rockbuttonhigh = resource_path('Assets/rockButtonHighlighted.png')
rockbuttonhigh = pygame.image.load(rockbuttonhigh).convert()
rockbuttonhigh = pygame.transform.scale(rockbuttonhigh, (175,60))

paperbuttonurl = resource_path('Assets/paperButton.png')
paperbutton = pygame.image.load(paperbuttonurl).convert()
paperbutton = pygame.transform.scale(paperbutton, (175,60))

paperbuttonhighurl = resource_path('Assets/paperButtonHighlighted.png')
paperbuttonhigh = pygame.image.load(paperbuttonhighurl).convert()
paperbuttonhigh = pygame.transform.scale(paperbuttonhigh, (175,60))

scisbuttonurl = resource_path('Assets/scissbutton.png')
scisbutton = pygame.image.load(scisbuttonurl).convert()
scisbutton = pygame.transform.scale(scisbutton, (175,60))

scisbuttonhighurl = resource_path('Assets/scissbuttonHighlighted.png')
scisbuttonhigh = pygame.image.load(scisbuttonhighurl).convert()
scisbuttonhigh = pygame.transform.scale(scisbuttonhigh, (175,60))

quitbuttonurl = resource_path('Assets/quitbutton.png')
quitbutton = pygame.image.load(quitbuttonurl).convert()
quitbutton = pygame.transform.scale(quitbutton, (175,60))

quitbuttonhighurl = resource_path('Assets/quitbuttonhighlighted.png')
quitbuttonhigh = pygame.image.load(quitbuttonhighurl).convert()
quitbuttonhigh = pygame.transform.scale(quitbuttonhigh, (175,60))

rockimageurl = resource_path('Assets/rock.png')
rockimage = pygame.image.load(rockimageurl)
paperimgurl = resource_path('Assets/paper.png')
paperimg = pygame.image.load(paperimgurl)

scissorurl= resource_path('Assets/scissors.png')
scissorsimg = pygame.image.load(scissorurl)
resetbuttonurl = resource_path('Assets/tryagain.png')
resetbutton =  pygame.transform.scale(pygame.image.load(resetbuttonurl), (304,171))
hitmarkerurl = resource_path('Assets/hitmarker.png')
hitmarker = pygame.image.load(hitmarkerurl)
invhandurl = resource_path('Assets/invhand.png')
invhand = pygame.image.load(invhandurl)
invrockurl = resource_path('Assets/invrock.png')
invrock = pygame.image.load(invrockurl)
invscissurl = resource_path('Assets/invscis.png')
invsciss = pygame.image.load(invscissurl)

hpbarurl = resource_path('Assets/hpbar.png')
hpBar = pygame.image.load(hpbarurl)
hpBar = pygame.transform.scale(hpBar, (250,20))
pygame.display.set_icon(newicon)

selectionurl = resource_path('Assets/Audio/selection.wav')
selection = pygame.mixer.Sound(selectionurl)
selection.set_volume(0.1)
hiturl = resource_path('Assets/Audio/hit.wav')
hit = pygame.mixer.Sound(hiturl)
hit.set_volume(0.1)
musicurl = resource_path('Assets/Audio/backgroundsong.mp3')
music = pygame.mixer.music.load(musicurl)
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)
winmusicurl = resource_path('Assets/Audio/winsong.wav')
winmusic = pygame.mixer.Sound(winmusicurl)
winmusic.set_volume(0.1)
lostmusicurl = resource_path('Assets/Audio/lostnoise.wav')
lostmusic = pygame.mixer.Sound(lostmusicurl)
lostmusic.set_volume(0.1)


try_again = True
run_game = True
while run_game:
    while try_again:
        winmusic.stop()
        pygame.mixer.music.play(-1)
        enemyBar, playerBar = draw_healthBars()

        draw_main(enemyBar, playerBar)
    
        buttons = Buttons()
        fightButtonX, fightButtonY = buttons.rockButton()
        paperButtonX,paperButtonY = buttons.paperButton()
        scisButtonX, scisButtonY = buttons.scisButton()
        quitButtonX, quitButtonY = buttons.quitButton()

        pygame.display.flip()
        user_turn = None
        game_over = False
        user_counter = 0
        bot_counter = 0
        counter = 0
        while game_over is False:
            draw_main(enemyBar, playerBar)
            user_turn = None
            while user_turn is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run_game = False
                        game_over = True
                        user_turn = True
                        try_again = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selection.play()
                        x,y = event.pos
                        if rockbutton.get_rect(topleft=(fightButtonX, fightButtonY)).collidepoint(x,y):
                            user_turn = 0
                            main_screen.blit(pygame.transform.rotate(rockimage, -70), (150,180))
                        elif paperbutton.get_rect(topleft=(paperButtonX, paperButtonY)).collidepoint(x,y):
                            user_turn = 1
                            main_screen.blit(pygame.transform.rotate(paperimg, -70), (150,180))
                        elif scisbutton.get_rect(topleft=(scisButtonX, scisButtonY)).collidepoint(x,y):
                            user_turn = 2
                            main_screen.blit(pygame.transform.rotate(scissorsimg, -70), (150,180))
                        elif quitbutton.get_rect(topleft=(quitButtonX, quitButtonY)).collidepoint(x,y):
                            run_game = False
                            user_turn = True
                            game_over = True
                            try_again = False
                        
                if rockbutton.get_rect(topleft=(fightButtonX, fightButtonY)).collidepoint(pygame.mouse.get_pos()):
                    main_screen.blit(rockbuttonhigh, (fightButtonX,fightButtonY))
                else:
                    main_screen.blit(rockbutton, (fightButtonX,fightButtonY))
                if paperbutton.get_rect(topleft=(paperButtonX, paperButtonY)).collidepoint(pygame.mouse.get_pos()):
                    main_screen.blit(paperbuttonhigh, (paperButtonX,paperButtonY))
                else:
                    main_screen.blit(paperbutton, (paperButtonX,paperButtonY))
                        
                if scisbutton.get_rect(topleft=(scisButtonX, scisButtonY)).collidepoint(pygame.mouse.get_pos()):
                    main_screen.blit(scisbuttonhigh, (scisButtonX,scisButtonY))
                else:
                    main_screen.blit(scisbutton, (scisButtonX,scisButtonY))
                        
                if quitbutton.get_rect(topleft=(quitButtonX, quitButtonY)).collidepoint(pygame.mouse.get_pos()):
                    main_screen.blit(quitbuttonhigh, (quitButtonX,quitButtonY))
                else:
                    main_screen.blit(quitbutton, (quitButtonX,quitButtonY))
                    
                pygame.display.update()
                clock.tick(60)
            
            bot_turn = gamelogic.create_random()
            if bot_turn == 0:
                main_screen.blit(pygame.transform.rotate(invrock, 120), (320,100))
            elif bot_turn == 1:
                main_screen.blit(pygame.transform.rotate(invhand, 120), (320,100))
            elif bot_turn == 2:
                main_screen.blit(pygame.transform.rotate(invsciss, 120), (320,100))
            pygame.display.update()
            winner = gamelogic.rules(user_turn, bot_turn)
            
            if winner == gamelogic.tie:   
                pass
            else: 
                if winner == gamelogic.user_win:
                    user_counter += 1
                    enemyBar.removeHitpoint()
                    hit.play()
                    main_screen.blit(hitmarker, (310,-20))
                else:
                    bot_counter += 1
                    playerBar.removeHitpoint()
                    hit.play()
                    main_screen.blit(hitmarker, (-70,125))
                pygame.display.update()
            if user_counter == 3:
                pygame.mixer.music.stop()
                winmusic.play(1)
                game_over = True
            elif bot_counter == 3:
                pygame.mixer.music.stop()
                lostmusic.play()
                game_over = True
            pygame.time.wait(1800)   
                
        main_screen.blit(resetbutton, (200,200))
        pygame.display.update()
        try_again = None
        if user_turn is not True:
            while try_again is None:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run_game = False
                        game_over = True
                        user_turn = True
                        try_again = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if resetbutton.get_rect(topleft=(200, 200)).collidepoint(x,y):
                            try_again = True
            
        
            
pygame.quit()