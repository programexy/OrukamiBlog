import pygame
import sys

pygame.init()
def story(name1):
    pygame.init()
    FPS = 60

    class Human(pygame.sprite.Sprite):
        def __init__(self, img, pos):
            super().__init__()
            self.flip = False
            self.image = pygame.image.load(str(img)).convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)

        def update(self):
            screen.blit(pygame.transform.flip(self.image,self.flip, False), self.rect)


    class Player(pygame.sprite.Sprite):
        def __init__(self, pos):
            super().__init__()
            self.image = pygame.image.load('slash/player.png').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
            self.flip = False
        def update(self):
            screen.blit(pygame.transform.flip(self.image,self.flip,False), self.rect)
    class Text(pygame.sprite.Sprite):
        def __init__(self):
            self.font = pygame.font.SysFont('courier/CourierSWA.ttf',50)
            self.text_box = pygame.Surface((screen.get_width(),200))
            self.text_rect = self.text_box.get_rect(bottomleft=(0, screen.get_height()))
        def wrap_text(self,text):
            screen.blit(self.text_box,self.text_rect)
            da_text = text
            if len(list(text)) > 30:
                texts = list(text)
                for number in range(int(len(text)/30)):
                    texts.insert(30*(number+1), '\n')
                    da_text = ''
                    for _ in texts:
                        da_text += _
            words = da_text.split('\n')
            line_n = self.text_rect.y
            for line in words:
                self.image = self.font.render(line,True,(255,255,255))
                self.rect = (0,(line_n))
                screen.blit(self.image,self.rect)
                line_n += 35





    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('The story')

    text = Text()

    background = pygame.image.load('background.png').convert_alpha()
    background = pygame.transform.scale(background, (background.get_width()*5,background.get_height()*5))
    back_rect = background.get_rect()
    guard1 = Human('guard.png', (1000, 0))
    guard2 = Human('guard.png', (1000, 0))
    hadar = Human('hadar.png', (1000, 0))
    player = Player((100, 230))
    msgs = ['Long ago, an evil king came to the throne. His name was Hadar. >',
    'Hadar loved seeing death and defeat, so he had made a stadium for games and evil. One day he came to you... >',
    f'Hadar:Hello {name1}. >',
    f'Hadar:How is your day? >',
    f'Hadar:Well to bad, since today is the day that will be your day of shame, or your day of glory... >',
    f'Hadar:So, {name1}, come here with me. >',
    f"Hadar:Actually, I'm being to nice... TAKE {name1} DOWN!!! C'mon! Hup! Hup! Run! >",
    'So off you were sent to the stadium. >',
    '',
    'Sign: The Lava Mountains.']



    a = True
    slide = 0
    while a == True:
        pygame.time.Clock().tick(FPS)
        pygame.display.update()
        screen.fill((0,255,0))
        screen.blit(background, back_rect)
        guard1.update()
        player.update()
        guard2.update()
        hadar.update()

        text.wrap_text(msgs[slide])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    if not slide == -1:
                        slide += 1
                    else:
                        print('loading...')
                        pygame.quit()
                        a = False
                    if slide == 1:
                        hadar.rect.x = 200
                        hadar.rect.y = 200
                    if slide == 2:
                        hadar.flip = True
                    if slide == 6:
                        guard1.rect.x = 115
                        guard2.rect.x = 75
                        guard1.rect.y = guard2.rect.y = player.rect.y
        if slide >= 7:
            hadar.flip = False
            if (back_rect.x + background.get_width()) <= 500:
                pass
                hadar.rect.x = 10000
                player.rect.x = 10000
                guard1.rect.x = 10000
                guard2.rect.x = 10000
                slide = -1
            else:
                back_rect.x -= 10
                msgs.insert(-2,' ')
