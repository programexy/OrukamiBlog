import pygame
import sys
from button import Button
import os

pygame.init()
screen = pygame.display.set_mode((750,200))
pygame.display.set_caption('Choose your destiny')
pygame.font.init()
font = pygame.font.SysFont('./courier/CourierSWA.ttf', 50)
image = font.render('Choose what game you want to play:', False, (255,255,255))
battle_b = Button('battle', (10,50), screen, 6)
crossy_b = Button('crossy', (400,120), screen,6)
laser_b = Button('elimination', (10,120), screen, 6)
tag_b = Button('tag', (250,50), screen, 6)
tennis_b = Button('tennis', (400,50), screen, 6)

def Tennis():
    os.chdir('tennis')
    os.system('python3 tennis.py')
    os.chdir('..')

def Battle():
    os.chdir('battle')
    os.system('python3 battle.py')
    os.chdir('..')

def Crossy():
    os.chdir('crossyroad')
    os.system('python3 crossy.py')
    os.chdir('..')

def Tag():
    os.chdir('tag')
    os.system('python3 tag.py')
    os.chdir('..')

def Elim():
    os.chdir('piu')
    os.system('python3 piupiu.py')
    os.chdir('..')
run = True
while run:
    battle_b.update()
    crossy_b.update()
    laser_b.update()
    tag_b.update()
    tennis_b.update()
    tennis_b.onclick(Tennis)
    battle_b.onclick(Battle)
    crossy_b.onclick(Crossy)
    laser_b.onclick(Elim)
    tag_b.onclick(Tag)

    screen.blit(image, (10,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
