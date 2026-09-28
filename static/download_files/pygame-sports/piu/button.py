import pygame

pygame.init()
mouse = pygame.mouse.get_pos()
class Button(pygame.sprite.Sprite):
    def __init__(self,n,pos,screen):
        super().__init__()
        self.n = n
        self.image = pygame.image.load(f'{n}pp.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4,self.image.get_height()*4))
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen
    def update(self):
        self.screen.blit(self.image,self.rect)