import pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, skin, pos):
        super().__init__()
        self.image = pygame.image.load(f'{skin}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.score = 0
    def key_input(self):
        keys = pygame.key.get_pressed()
        if self.rect.x > 0:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.rect.x -= 10

        if self.rect.x < 600 - self.image.get_width():
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.rect.x += 10

    def update(self, screen):
        screen.blit(self.image, self.rect)
