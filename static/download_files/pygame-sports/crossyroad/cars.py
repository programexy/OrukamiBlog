import pygame
import random

pygame.init()


class Car(pygame.sprite.Sprite):
    def __init__(self, color, pos, screen):
        super().__init__()
        self.image = pygame.image.load(f'{color}.png').convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(midleft=pos)
        self.screen = screen
        self.speed = 10

    def move(self, speed=5):
        self.rect.x -= speed
        if self.rect.x <= 0:
            self.rect.x = self.screen.get_width()
    def move_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y += 10
        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     self.rect.y -= 10
    def reset(self):
        if self.rect.y >= self.screen.get_height():
            self.rect.y = 0
            self.speed += 5
    def update(self):
        self.reset()
        self.move_down()
        self.move(self.speed)
        self.screen.blit(self.image, self.rect)
class Train(pygame.sprite.Sprite):
    def __init__(self, color, pos, screen):
        super().__init__()
        self.image = pygame.image.load(f'{color}.png').convert_alpha()
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect(midleft=pos)
        self.screen = screen
        self.speed = random.randint(5,10)
    def move(self, speed=30):
        self.rect.x -= speed
        if self.rect.x <= 0:
            self.rect.x = self.screen.get_width() + 10000
    def move_down(self):
        self.rect.y += 10
    def reset(self):
        if self.rect.y >= self.screen.get_height():
            self.rect.y = 0
            self.speed += 5
    def update(self):
        self.reset()
        self.move()
        self.screen.blit(self.image, self.rect)

class Road(pygame.sprite.Sprite):
    def __init__(self, type, pos, screen):
        super().__init__()
        self.image = pygame.image.load(f'{type}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4,self.image.get_height()*4))
        self.rect = self.image.get_rect(midleft=pos)
        self.screen = screen

    def move_down(self):
        self.rect.y += 10
    def reset(self):
        if self.rect.y >= self.screen.get_height():
            self.rect.y = 0

    def update(self):
        self.reset()
        self.screen.blit(self.image, self.rect)