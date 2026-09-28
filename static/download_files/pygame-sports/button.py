import pygame

pygame.init()
mouse = pygame.mouse.get_pos()
class Button(pygame.sprite.Sprite):
    def __init__(self,pic,pos,screen, size):
        super().__init__()
        if pic != None:
            self.image = pygame.image.load(f'{pic}.png').convert_alpha()
        else:
            self.image = pygame.Surface((100,50))
            self.image.fill('white')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*size,self.image.get_height()*size))
        self.rect = self.image.get_rect(topleft=pos)
        self.screen = screen
    def onclick(self,dostuff):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0]:
            if self.rect.collidepoint(mouse):
                dostuff()
    def update(self):
        self.screen.blit(self.image,self.rect)