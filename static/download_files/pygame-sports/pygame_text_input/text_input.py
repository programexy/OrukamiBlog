import pygame

pygame.init()

class TextInput(pygame.sprite.Sprite):
    def __init__(self,screen, pos, color='white',size_x=10,size_y=50):
        super().__init__()
        self.screen = screen
        self.image = pygame.Surface((size_x,size_y))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
