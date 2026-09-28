import sys
from player import *
from button import Button
import pygame
from random import randint as rand
import os
from wrap_text import *




class Tree(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('tree.png').convert_alpha()
        self.image.set_alpha(225)
        self.pos = pos
        self.rect = self.image.get_rect(center=pos)
        self.size = 50
        self.max_size = rand(50,400)

    def grow(self):
        if self.size > self.max_size-1:
            self.size = self.max_size
        else:
            self.size += 0.5

    def update(self):
        self.rect = self.image.get_rect(center=self.pos)
        self.grow()
        screen.blit(pygame.transform.scale(self.image, (self.size,self.size)),self.rect)


class Rock(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('rock.png').convert_alpha()
        self.size = rand(50, 100)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.pos = pos
        self.rect = self.image.get_rect(center=pos)

    def not_in(self, player):
        if not player.yeet:
            if self.rect.colliderect(player):
                if player.dir == 'down':
                    player.rect.bottom = self.rect.top
                elif player.dir == 'up':
                    player.rect.top = self.rect.bottom
                elif player.dir == 'left':
                    player.rect.left = self.rect.right
                elif player.dir == 'right':
                    player.rect.right = self.rect.left
    def got_hit(self):
        global bullet_list
        for missiles in bullet_list:
            for missile in missiles:
                if self.rect.colliderect(missile):
                    missile.rect.x = 10000
                    missile.hit = True

    def update(self):
        self.got_hit()
        for a_player in [player1,player2,player3,player4]:
            self.not_in(a_player)
        screen.blit(self.image,self.rect)

pygame.init()

screen = pygame.display.set_mode((800, 600))

player1 = Player((rand(0, 795), rand(0, 595)), 1, screen)
player2 = Player((rand(0, 795), rand(0, 595)), 2, screen)
player3 = Player((rand(0, 795), rand(0, 595)), 3, screen)
player4 = Player((rand(0, 795), rand(0, 595)), 4, screen)

button1 = Button(1, (400, 250), screen)
button2 = Button(2, (400, 300), screen)
button3 = Button(3, (400, 350), screen)
button4 = Button(4, (400, 400), screen)

mouse = pygame.mouse.get_pos()

bullets1 = []
bullets1.append(Bullet(player1, screen))
bullets2 = []
bullets2.append(Bullet(player2, screen))
bullets3 = []
bullets3.append(Bullet(player3, screen))
bullets4 = []
bullets4.append(Bullet(player4, screen))

trees = pygame.sprite.Group()

clock = pygame.time.Clock()

maximum = rand(15,30)

rocks = pygame.sprite.Group()

def create_tree():
    trees.add(Tree((rand(0,795), rand(0,595))))
def create_rock():
    rocks.add(Rock((rand(0,795), rand(0,595))))

for i in range(int(rand(20,25)+1)):
    create_rock()

background = pygame.image.load('pew1.png').convert_alpha()
background = pygame.transform.scale(background, (background.get_width()*5, background.get_height()*5))
background_rect = background.get_rect(center=(400,300))

pygame.font.init()
color = ''
font = pygame.font.SysFont('./courier/CourierSWA.ttf', 100)
font3 = pygame.font.SysFont('./courier/CourierSWA.ttf', 125)
font2 = pygame.font.SysFont('./courier/CourierSWA.ttf', 30)
title = font.render('ELIMINATION!', False, (255,255,255))
title2 = font2.render('The Piu Piu Game.', False, (255,255,255))
title2_rect = title2.get_rect(center=(400,220))
title_rect = title.get_rect(center=(400,170))
eliminated = font3.render(f'{color} IS ELIMINATED!', False, (255,255,255))
eliminated = pygame.transform.rotate(eliminated, 35)
elim_rect = eliminated.get_rect(center=(400,300))

bullet_list = [bullets1, bullets2, bullets3, bullets4]

players = 2
players_alive = 4
SEC = 2
timer =SEC*120
elimination = False
slide = 0
colors = ''
msgs = [f'{color} IS ELIMINATED!',f'{colors} WON!']
able = True
start = True
run = True
while run:
    # if elim == True:

    pygame.display.update()
    msgs = [f'{color} IS ELIMINATED!', f'{colors} WON']
    eliminated = font3.render(msgs[slide], False, (255, 255, 255))
    eliminated = pygame.transform.rotate(eliminated, 35)
    elim_rect = eliminated.get_rect(center=(400, 300))
    press = pygame.mouse.get_pressed()
    if start:

        screen.fill('black')
        screen.blit(background,background_rect)
        screen.blit(title,title_rect)
        screen.blit(title2,title2_rect)
        wrap_text_m(font2, 'Instructions:\nGreen player: Arrow keys to move, Space to shoot\nRed player: WSAD to move, E to shoot\nBlue player: TGFH to move, Y to shoot\nGreen player: IKJL keys to move, O to shoot\nRemember, no need to shift!\nESCAPE to go to menu.', screen, 400,420,'center', 20)
        button1.update()
        button2.update()
        button3.update()
        button4.update()
        if press[0]:
            if button1.rect.collidepoint(pygame.mouse.get_pos()):
                players = 2
                player2.ai = True
                start = False
                players_alive = players
            if button2.rect.collidepoint(pygame.mouse.get_pos()):
                players = 2
                start = False
                players_alive = players
            elif button3.rect.collidepoint(pygame.mouse.get_pos()):
                players = 3
                start = False
                players_alive = players
            elif button4.rect.collidepoint(pygame.mouse.get_pos()):
                players = 4
                start = False
                players_alive = players
    else:
        screen.fill('green')

        for bullet in bullets1:
            bullet.update()
            if bullet.rect.colliderect(player2):
                bullet.hit = True
                bullet.rect.x = 10000
                player2.lives -= 1
            if bullet.rect.colliderect(player3):
                bullet.hit = True
                bullet.rect.x = 10000
                player3.lives -= 1
            if bullet.rect.colliderect(player4):
                bullet.hit = True
                bullet.rect.x = 10000
                player4.lives -= 1

        for bullet in bullets2:
            bullet.update()
            if bullet.rect.colliderect(player1):
                bullet.hit = True
                bullet.rect.x = 10000
                player1.lives -= 1
            if bullet.rect.colliderect(player3):
                bullet.hit = True
                bullet.rect.x = 10000
                player3.lives -= 1
            if bullet.rect.colliderect(player4):
                bullet.hit = True
                bullet.rect.x = 10000
                player4.lives -= 1
        player1.update()
        player1.k_input()
        player2.update()
        player2.k_input(player1, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
        if players > 2:
            for bullet in bullets3:
                bullet.update()
                if bullet.rect.colliderect(player2):
                    bullet.hit = True
                    bullet.rect.x = 10000
                    player2.lives -= 1
                if bullet.rect.colliderect(player1):
                    bullet.hit = True
                    bullet.rect.x = 10000
                    player1.lives -= 1
                if bullet.rect.colliderect(player4):
                    bullet.hit = True
                    bullet.rect.x = 10000
                    player4.lives -= 1
            player3.update()
            player3.k_input(None, pygame.K_t, pygame.K_g, pygame.K_f, pygame.K_h)
        else:
            player3.rect.x = 10000
        if players > 3:
            for bullet in bullets4:
                bullet.update()
                if bullet.rect.colliderect(player2):
                    bullet.hit = True
                    bullet.rect.x = 10000
                    player2.lives -= 1
                if bullet.rect.colliderect(player3):
                    bullet.hit = True
                    bullet.rect.x = 10000
                    player3.lives -= 1
                if bullet.rect.colliderect(player1):
                    bullet.hit = True
                    bullet.rect.x = 10000
                    player1.lives -= 1
            player4.update()
            player4.k_input(None, pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l)
        else:
            player4.rect.x = 10000
        rocks.update()
        # for bullets in bullet_list:
        #     for bullet in bullets:
        #         if pygame.sprite.spritecollideany(bullet, rocks):
        #             bullet.hit = True
        #             bullet.rect.x = 10000
        trees.update()
        if maximum >= 2:
            create_tree()
            maximum -= 1
        if elimination:
            screen.blit(eliminated, elim_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                run = False
            if event.key == pygame.K_r:
                start = True
            if event.key == pygame.K_SPACE:
                for bullet in bullets1:
                    bullet.fire()
                bullets1.append(Bullet(player1, screen))
                # winsound.PlaySound('piu.wav', winsound.SND_ASYNC)
            if players > 2:
                if event.key == pygame.K_y:
                    for bullet in bullets3:
                        bullet.fire()
                    bullets3.append(Bullet(player3, screen))
                    # winsound.PlaySound('piu.wav', winsound.SND_ASYNC)
            if event.key == pygame.K_e:
                for bullet in bullets2:
                    bullet.fire()
                bullets2.append(Bullet(player2, screen))
                # winsound.PlaySound('piu.wav', winsound.SND_ASYNC)
            if players > 3:
                if event.key == pygame.K_o:
                    for bullet in bullets4:
                        bullet.fire()
                    bullets4.append(Bullet(player4, screen))
                    # winsound.PlaySound('piu.wav', winsound.SND_ASYNC)

    if elimination:
        timer -= 1
    if timer <= 0:
        if timer == 0:
            players_alive -= 1
        timer = -1
        if not player1.ghost and player1.dead:
            player1.ghost = True
        if not player2.ghost and player2.dead:
            player2.ghost = True
        if not player3.ghost and player3.dead:
            player3.ghost = True
        if not player4.ghost and player4.dead:
            player4.ghost = True
        elimination = False
        timer = SEC*120
    if player1.dead and not player1.ghost:
        color = 'Green'
        if not player1.ghost:
            elimination = True
        player1.ghost = True
    if player2.dead and not player2.ghost:
        color = 'Red'
        if not player2.ghost:
            elimination = True
        player2.ghost = True
    if player3.dead and not player3.ghost:
        color = 'Blue'
        if not player3.ghost:
            elimination = True
        player3.ghost = True
    if player4.dead and not player4.ghost:
        color = 'Yellow'
        if not player4.ghost:
            elimination = True
        player4.ghost = True
    if players_alive <= 1:
        if not player1.dead:
            colors = 'Green'
        if not player2.dead:
            colors = 'Red'
        if players > 2:
            if not player3.dead:
                colors = 'Blue'
            if players > 3:
                if not player4.dead:
                    colors = 'Yellow'
        slide = 1
        elimination = True
    if player2.ai and player2.distance <= 205:
        chance = rand(1,21)
        if chance == 1:
            for bullet in bullets2:
                bullet.fire()
            bullets2.append(Bullet(player2, screen))
    clock.tick(players * 60)


