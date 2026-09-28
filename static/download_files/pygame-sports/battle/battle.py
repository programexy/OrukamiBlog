import os


def clear():
    os.system('cls||clear')
# def App():
import random
from Story import story

while True:
    name1 = input('What is your name? >').title()
    if len(name1) > 50:
        print('That name is too long! It must be less than 50 characters!')
    else:
        break

print('Hello ' + name1 + '!')

FPS = 120



def start():
    answer = input('Do you want to know the story? Please only type y or n >').lower()
    if answer == 'y':
        story(name1)
    answer = input('Do you want to know the instructions? Please only type y or n >').lower()
    if answer == 'y':
        print('Press [enter] after you finish each line to continue\nIntructions:')
        clear()
        input('Use arrow keys to move. >')
        clear()
        input('Press space for attack. >')
        clear()
        input('DO NOT FALL OF THE BATTLE STAGE! >')
        clear()
        input('Try not to get killed by the enemy. >')
        clear()
        input('You are the man with a blue sword, the other one is your enemy. >')
        clear()
        input('click the new window that pops up on the bottom of the screen >')
        clear()
        input('Enter to start. >')
        clear()

start()


# ai = input('Do you want to play with the ai?\n please only type "y" or "n" >').lower()
# if ai == 'y':

import math
import pygame
import sys
ai = True
name = random.choice(['Fred', 'Bob', 'Brutus', 'Felix'])

# else:
#     ai = False
#     name = input('What is your name, player 2? >').title()

pygame.init()
clear()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('AI battle')
clock = pygame.time.Clock()

pygame.font.init()


class PLAYER(pygame.sprite.Sprite):
    def __init__(self, pos, name):
        super().__init__()
        self.img = pygame.image.load('slash/0.png').convert_alpha()
        self.rect = self.img.get_rect(topleft=pos)
        self.slash = False
        self.hitting = False
        self.flip = False
        self.speed = 0
        self.lives = 50
        # lives box

        self.box = pygame.Surface((((self.lives) + 0.1), 10))
        self.box.fill('blue')
        self.brect = self.box.get_rect(midtop=(self.rect.y - 50, self.rect.x))

        self.dead = False

        self.font = pygame.font.SysFont('robot fonts/Roboto-Black.ttf', 25)
        self.font_img = self.font.render(name, False, (0, 0, 0))
        self.font_rect = self.font_img.get_rect(midbottom=(self.rect.x + 20, self.rect.y - 10))
        self.name = name

        self.animation_speed = 0.15

        self.damage = 1

    def key_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.slash = True
            self.hitting = True
        if keys[pygame.K_x]:
            self.damage = 5
            self.slash = True
            self.hitting = True
            self.animation_speed = 0.2
        else:
            self.damage = 1
        if keys[pygame.K_UP]:
            if self.rect.y != stage_rect.y:
                self.rect.y -= 5
            else:
                self.rect.y += 0
        if keys[pygame.K_DOWN]:
            if self.rect.y != stage_rect.bottom:
                self.rect.y += 5
        if keys[pygame.K_LEFT]:
            if self.rect.left != stage_rect.left:
                self.rect.x -= 5
                self.flip = True
        if keys[pygame.K_RIGHT]:
            if self.rect.right != stage_rect.right:
                self.rect.x += 5
                self.flip = False

    def animate(self):
        if self.slash:
            self.speed += self.animation_speed
            if self.speed < 3:
                self.img = pygame.image.load(f'slash/{int(self.speed)}.png').convert_alpha()
            else:
                self.speed = 0
                self.slash = False
                self.img = pygame.image.load(f'slash/{int(self.speed)}.png').convert_alpha()

    def attacktrue(self, enemy):
        x = self.rect.x
        xp = enemy.rect.x
        y = self.rect.y
        yp = enemy.rect.y

        xx = abs(x - xp)
        yy = abs(y - yp)

        xx2 = xx ** 2
        yy2 = yy ** 2
        end = xx2 + yy2
        direc = math.sqrt(end)

        if enemy.lives > 0:
            if direc < 90 and self.slash == True:
                enemy.lives -= self.damage
                if self.rect.x > enemy.rect.x:
                    enemy.rect.x -= 40
                else:
                    enemy.rect.x += 40
                if self.rect.y > enemy.rect.y:
                    enemy.rect.y -= 40
                else:
                    enemy.rect.y += 40
        else:
            enemy.dead = True
            text = font.render(f'{self.name} WON!', False, (0, 0, 0))
            text_rect = text.get_rect(center=(350, 350))
            screen.blit(text, text_rect)

    def fall_off_cliff(self):
        if not self.rect.colliderect(stage_rect):
            if not self.rect.colliderect(bridge_rect):
                self.lives = 0
                text = font.render(f'{enemy.name} WON!', False, (0, 0, 0))
                text_rect = text.get_rect(center=(350, 350))
                screen.blit(text, text_rect)

    def update(self,enemy):
        self.attacktrue(enemy)
        self.key_input()
        self.animate()
        screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)
        self.box = pygame.Surface((((self.lives * 10) / 8 + 0.1), 10))
        self.box.fill('sky blue')
        self.brect = self.box.get_rect(topleft=(self.rect.x, self.rect.y - 50))
        screen.blit(self.box, self.brect)
        self.fall_off_cliff()
        self.font_rect = self.font_img.get_rect(midbottom=(self.rect.x + (self.img.get_width() / 2), self.rect.y - 10))
        screen.blit(self.font_img, self.font_rect)


class ENEMY(pygame.sprite.Sprite):
    def __init__(self, pos, ai, name):
        super().__init__()
        self.img = pygame.image.load('enemyslash/0.png').convert_alpha()
        self.rect = self.img.get_rect(topleft=pos)
        self.slash = False
        self.flip = False
        self.speed = 0
        self.lives = 50
        self.hitting = False
        # lives box

        self.box = pygame.Surface(((self.lives / 10) + 0.5, 20))
        self.box.fill('red')
        self.brect = self.box.get_rect(midtop=(self.rect.y - 50, self.rect.x))
        self.ai = ai
        self.dead = False
        self.name = name
        # name:
        self.font = pygame.font.SysFont('robot fonts/Roboto-Black.ttf', 25)
        self.font_img = self.font.render(name, False, (0, 0, 0))
        self.font_rect = self.font_img.get_rect(midbottom=(self.rect.x + 20, self.rect.y - 10))

    def move(self, speed=2):  # chase movement
        if self.ai:
            # Movement along x direction
            if self.rect.x > player.rect.x:
                self.rect.x -= speed
                self.flip = False
            elif self.rect.x < player.rect.x:
                self.rect.x += speed
                self.flip = True
            # Movement along y direction
            if self.rect.y < player.rect.y:
                self.rect.y += speed
            elif self.rect.y > player.rect.y:
                self.rect.y -= speed
            # slash
            x = self.rect.x
            xp = player.rect.x
            y = self.rect.y
            yp = player.rect.y

            xx = abs(x - xp)
            yy = abs(y - yp)

            xx2 = xx ** 2
            yy2 = yy ** 2
            end = xx2 + yy2
            direc = math.sqrt(end)

            if direc < 20:
                self.slash = True
            else:
                self.slash = False
            if player.lives > 0:
                if self.slash == True and direc < 10:
                    player.lives -= 1

        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                self.slash = True
                self.hitting = True
            if keys[pygame.K_w]:
                if self.rect.y != stage_rect.y:
                    self.rect.y -= 5
                else:
                    self.rect.y += 0
            if keys[pygame.K_s]:
                if self.rect.y != stage_rect.bottom:
                    self.rect.y += 5
            if keys[pygame.K_a]:
                if self.rect.left != stage_rect.left:
                    self.rect.x -= 5
                    self.flip = False
            if keys[pygame.K_d]:
                if self.rect.right != stage_rect.right:
                    self.rect.x += 5
                    self.flip = True

    def fall_off_cliff(self):
        if not self.rect.colliderect(stage_rect):
            if not self.rect.colliderect(bridge_rect):
                self.lives = 0
                text = font.render(f'{enemy.name} WON!', False, (0, 0, 0))
                text_rect = text.get_rect(center=(350, 350))
                screen.blit(text, text_rect)

    def attacktrue(self, enemy):
        x = self.rect.x
        xp = enemy.rect.x
        y = self.rect.y
        yp = enemy.rect.y

        xx = abs(x - xp)
        yy = abs(y - yp)

        xx2 = xx ** 2
        yy2 = yy ** 2
        end = xx2 + yy2
        direc = math.sqrt(end)

        if enemy.lives > 0:
            if direc < 90 and self.slash == True:
                enemy.lives -= 1
                if self.rect.x > enemy.rect.x:
                    enemy.rect.x -= 40
                else:
                    enemy.rect.x += 40
                if self.rect.y > enemy.rect.y:
                    enemy.rect.y -= 40
                else:
                    enemy.rect.y += 40
                # enemy.rect.y += 1
        else:
            enemy.dead = True
            text = font.render(f'{self.name} WON!', False, (0, 0, 0))
            text_rect = text.get_rect(center=(350, 350))
            screen.blit(text, text_rect)

    def animate(self):
        if self.slash == True:
            self.speed += 0.15
            if self.speed < 3:
                self.img = pygame.image.load(f'enemyslash/{int(self.speed)}.png').convert_alpha()
            else:
                self.speed = 0
                self.slash = False
                self.img = pygame.image.load(f'enemyslash/{int(self.speed)}.png').convert_alpha()

    def update(self):
        self.animate()
        self.move()
        self.attacktrue(player)
        screen.blit(pygame.transform.flip(self.img, self.flip, False), self.rect)
        self.box = pygame.Surface((((self.lives * 10) / 8 + 0.1), 10))
        self.box.fill('red')
        self.brect = self.box.get_rect(topleft=(self.rect.x, self.rect.y - 50))
        screen.blit(self.box, self.brect)
        self.fall_off_cliff()
        self.font_rect = self.font_img.get_rect(midbottom=(self.rect.x + (self.img.get_width() / 2), self.rect.y - 10))
        screen.blit(self.font_img, self.font_rect)


# typewriter
font = pygame.font.SysFont('roboto fonts/Roboto-Black.ttf', 60)

stage = pygame.image.load('battlestage.png').convert_alpha()
stage = pygame.transform.scale(stage, (stage.get_width() * 3, stage.get_height() * 3))
stage_rect = stage.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

bridge = pygame.image.load('bridge.png').convert_alpha()
bridge = pygame.transform.scale(bridge, (10000, bridge.get_height() * 10))
bridge_rect = bridge.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

player = PLAYER((0, screen.get_height() / 2), name1)
enemy = ENEMY((screen.get_width() - 100, screen.get_height() / 2), ai, name)
runny = True
clear()
pic = [(145, 14, 18), (150, 14, 18), (155, 14, 18)]
animation = 0

while runny:
    clock.tick(FPS)
    pygame.display.update()
    if animation < 2:
        animation += 0.05
    else:
        animation = 0
    # print(enemy.lives, player.lives)
    screen.fill(pic[int(animation)])
    screen.blit(bridge, bridge_rect)
    screen.blit(stage, stage_rect)
    if not player.dead:
        player.update(enemy)
    if not enemy.dead:
        enemy.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# App()