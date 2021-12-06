import pygame, sys, numpy, keyboard
from pygame.locals import *
from PIL import Image, ImageDraw

(width, height) = (1900, 1050)

pygame.init()
screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)
pygame.display.set_caption('TLP')

start_height=2000
start_width=2000

v=2
#size = (1594*.5, 1277*.5)
#size = (1236, 937)
#size = (3168*.45, 2144*.45)
size = (5655*3, 3879*3)
#map=pygame.image.load('lakemap.png')
map=pygame.image.load('WestIsland_v1.png')
og_map=map
map= pygame.transform.scale(map, size)
#map= pygame.transform.scale(map, (1236, 937))
rect=map.get_rect()
screen.blit(map,rect)

bg=pygame.image.load('bg.png')
txtbox=pygame.image.load('txtbox.png')

myfont = pygame.font.SysFont('High Tower Text', 50)
state=""
last_state="down"
ctr=0
expander=-3
screen.fill((255,255,255))

tr1=pygame.image.load('lucas.png')
tr2=pygame.image.load('dawn.png')

not_selected=True

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key==pygame.K_1:
                not_selected=False
                sprites=pygame.image.load('sprites1.png')
                sprites = pygame.transform.scale(sprites, (256,256))
            elif event.key==pygame.K_2:
                not_selected=False
                sprites=pygame.image.load('sprites2.png')
                sprites = pygame.transform.scale(sprites, (256,256))
            elif event.key==pygame.K_s:
                v=10
            else:
                v=2
        elif event.type == MOUSEBUTTONDOWN and not not_selected:
            pygame.display.update()
    if not_selected:
        screen.blit(bg,(0,0))
        screen.blit(tr1,(width/2-75,50))
        screen.blit(tr2,(width/2+75,50))
        txtbox = pygame.transform.scale(txtbox, (1430, 600))
        screen.blit(txtbox,(280,180))
        txtbox2 = pygame.transform.scale(txtbox, (490, 300))
        screen.blit(txtbox2,(750,220))
        text = myfont.render('Enter the number of the character you want to play with.', False, (0, 0, 0))
        screen.blit(text,(width/2-550,410))
        number1 = myfont.render('1', False, (0, 0, 0))
        screen.blit(number1,(width/2-20,320))
        number2 = myfont.render('2', False, (0, 0, 0))
        screen.blit(number2,(width/2+110,320))
        pygame.display.update()
    else:
        #screen.blit(map,(0,0),rect)
        screen.blit(bg,(0,0))
        blue=(0,0,255)
        green=(0,255,0)
        red=(255,0,0)
        """""
        pygame.draw.rect(screen, blue, pygame.Rect(700*.8, 0*.8, 127*.8, 85*.8),2)
        pygame.draw.rect(screen, blue, pygame.Rect(733*.8, 60*.8, 126*.8, 120*.8),2)
        pygame.draw.rect(screen, blue, pygame.Rect(765*.8, 90*.8, 126*.8, 150*.8),2)
        pygame.draw.rect(screen, blue, pygame.Rect(850*.8, 125*.8, 71*.8, 95*.8),2)
        pygame.draw.rect(screen, blue, pygame.Rect(733*.8, 222*.8, 126*.8, 125*.8),2)
        pygame.draw.rect(screen, blue, pygame.Rect(733*.8, 347*.8, 155*.8, 125*.8),2)
        pygame.draw.rect(screen, blue, pygame.Rect(700*.8, 380*.8, 220*.8, 60*.8),2)
        pygame.draw.rect(screen, green, pygame.Rect(0, 0, 1594*.8, 280*.8),2)
        pygame.draw.rect(screen, green, pygame.Rect(0, 915, 1594*.8, 280*.8),2)
        pygame.draw.rect(screen, green, pygame.Rect(0, 765, 200, 280*.8),2)
        pygame.draw.rect(screen, green, pygame.Rect(203, 205, 533, 210*.8),2)
        pygame.draw.rect(screen, green, pygame.Rect(0, 0, 100, 600),2)
        pygame.draw.rect(screen, green, pygame.Rect(1073, 355, 220, 570),2)"""

        
        smol_rect = pygame.Rect(start_width-450,start_height-450,900,900)
        screen.blit(map,(500,100),(smol_rect))
        #sub = screen.subsurface(smol_rect)
        #sub = pygame.transform.scale(sub, (900, 900))
        #screen.blit(bg,(0,0))
        #screen.blit(sub,(500,100))
        #txtbox = pygame.transform.scale(txtbox, (1200, 400))
        #screen.blit(txtbox,(340,-120))
        pygame.draw.rect(screen, (209,141,178), pygame.Rect(500,100,900,900),10)


        if keyboard.is_pressed('left'):
            state="left"
        if keyboard.is_pressed('down'):
            state="down"
        if keyboard.is_pressed('right'):
            state="right"
        if keyboard.is_pressed('up'):
            state="up"

        if state=="down":
            start_height+=v
            screen.blit(pygame.transform.scale(sprites, (512, 512)), (width/2-60,height/2-80), (ctr*128,0,128,128))
        elif state=="up":
            start_height-=v
            screen.blit(pygame.transform.scale(sprites, (512, 512)), (width/2-60,height/2-80), (ctr*128,384,128,128))
        elif state=="left":
            start_width-=v
            screen.blit(pygame.transform.scale(sprites, (512, 512)), (width/2-60,height/2-80), (ctr*128,128,128,128))
        elif state=="right":
            start_width+=v
            screen.blit(pygame.transform.scale(sprites, (512, 512)), (width/2-60,height/2-80), (ctr*128,256,128,128))
        else:
            if last_state=="down":
                screen.blit(pygame.transform.scale(sprites, (512, 512)), (width/2-60,height/2-80), (0,0,128,128))
            elif last_state=="up":
                screen.blit(pygame.transform.scale(sprites, (512, 512)), (width/2-60,height/2-80), (0,384,128,128))
            elif last_state=="left":
                screen.blit(pygame.transform.scale(sprites, (512, 512)), (width/2-60,height/2-80), (0,128,128,128))
            elif last_state=="right":
                screen.blit(pygame.transform.scale(sprites, (512, 512)), (width/2-60,height/2-80), (0,256,128,128))

        if not state=="":        
            last_state=state
        state=""

        if expander<10:
            expander+=1
        else:
            expander=-3

        if expander==10:
            if ctr<3:
                ctr+=1
            else:
                ctr=0


        '''''
        if start_height<85:
            start_height+=10
        if start_height>1150*.8:
            start_height-=30
        if start_width<81:
            start_width+=10
        if start_width>1560*.8:
            start_width-=10
        '''
        pygame.display.update()