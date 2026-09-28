import pygame
import math

pygame.init()
pygame.font.init()



class Player(pygame.sprite.Sprite):
    def __init__(self, pos, skin, screen):
        super().__init__()
        self.image = pygame.image.load(f'pew{skin}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.5, self.image.get_height() * 0.5))
        self.rect = self.image.get_rect(topleft=pos)
        self.screen = screen
        self.dir = 'None'
        self.angle = 0
        self.launch = False
        self.dead = False
        self.lives = 20
        self.ghost = False
        self.ai = False
        self.distance = 0
        self.yeet = False
        self.font = pygame.font.SysFont('../courier/CourierSWA.ttf', 20)
        self.font_i = self.font.render(str(self.lives), False, (0,0,0))
        self.font_rect = self.font_i.get_rect(midbottom=self.rect.midtop)

    def k_input(self, target=None, UP=pygame.K_UP, DOWN=pygame.K_DOWN, LEFT=pygame.K_LEFT, RIGHT=pygame.K_RIGHT, yeet=pygame.K_n):
        if not self.ai:
            keys = pygame.key.get_pressed()
            if self.rect.y > 5:
                if keys[UP]:
                    self.rect.y -= 5
                    self.dir = 'up'
                    self.angle = 0
            if self.rect.y < 565:
                if keys[DOWN]:
                    self.rect.y += 5
                    self.dir = 'down'
                    self.angle = 180
            if self.rect.x > 5:
                if keys[LEFT]:
                    self.rect.x -= 5
                    self.dir = 'left'
                    self.angle = 90
            if self.rect.x < 765:
                if keys[RIGHT]:
                    self.rect.x += 5
                    self.dir = 'right'
                    self.angle = 270
            if keys[yeet]:
                self.yeet = True
            else:
                self.yeet = False
        else:
            x = abs(self.rect.x - target.rect.x)
            y = abs(self.rect.y - target.rect.y)
            self.distance = math.sqrt(x**2 + y**2)
            if self.rect.x > target.rect.x and 50 < self.distance < 200:
                self.rect.x -= 1
                self.angle = 90
            if self.rect.x < target.rect.x and 50 < self.distance < 200:
                self.rect.x += 1
                self.angle = 270
            if self.rect.y > target.rect.y and 50 < self.distance < 200:
                self.rect.y -= 1
                self.angle = 0
            if self.rect.y < target.rect.y and 50 < self.distance < 200:
                self.rect.y += 1
                self.angle = 180

            

    def update(self):
        self.font_i = self.font.render(str(self.lives), False, (0, 0, 0))
        self.font_rect = self.font_i.get_rect(midbottom=self.rect.midtop)
        if self.lives == 0:
            self.dead = True
            self.rect.x = 101000
        if not self.dead:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
            self.screen.blit(self.font_i,self.font_rect)
            self.screen.blit(pygame.transform.rotate(self.image, self.angle), self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, screen, launch=False):
        super().__init__()
        self.ammo = []
        self.image = pygame.Surface((10, 20))
        self.image.fill('white')
        self.player = player
        self.angle = self.player.angle
        self.rect = self.image.get_rect(center=(1000,0))
        self.screen = screen
        self.launch = launch
        self.hit = False

    def fire(self):
        if not self.launch:
            self.angle = self.player.angle
            self.rect = self.image.get_rect(center=self.player.rect.center)
            self.launch = True
    def move(self,speed=10):
        if self.launch:
            if self.angle == 0:
                self.rect.y -= speed
            if self.angle == 180:
                self.rect.y += speed
            if self.angle == 90:
                self.rect.x -= speed
            if self.angle == 270:
                self.rect.x += speed


    def update(self):
        if not self.hit:
            self.move()
            if not self.player.dead:
                self.screen.blit(pygame.transform.rotate(self.image, self.angle), self.rect)
