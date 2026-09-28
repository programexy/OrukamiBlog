import pygame, sys, random

screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption('tennis')
pygame.init()
clock = pygame.time.Clock()


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.img = pygame.image.load('tennisplayer.png')
        self.img = pygame.transform.scale(self.img, (self.img.get_width() * 3, self.img.get_height() * 3))
        self.rect = self.img.get_rect(topleft=pos)
        self.flip = False
        self.angle = 0
        self.auto = False
        self.score = 0

    def input(self,UP=pygame.K_UP, DOWN=pygame.K_DOWN, LEFT=pygame.K_LEFT, RIGHT=pygame.K_RIGHT, HIT=pygame.K_SPACE, AUTO=pygame.K_n):
        keys = pygame.key.get_pressed()
        if keys[UP]:
            self.rect.y -= 10
            ball.play = True
        if keys[DOWN]:
            self.rect.y += 10
            ball.play = True
        if keys[LEFT]:
            self.rect.x -= 10
            self.flip = True
            ball.play = True
        if keys[RIGHT]:
            self.rect.x += 10
            self.flip = False
            ball.play = True
        if keys[HIT]:
            if self.rect.colliderect(ball.rect):
                ball.bx *= -1
                if self.rect.y > 300:
                    ball.by = -3
                elif self.rect.y < 300:
                    ball.by = 3

            if self.rect.x < 450:
                self.angle = -10
            else:
                self.angle = 10
            ball.play = True
        else:
            self.angle = 0

        if keys[AUTO]:
            if not self.auto:
                self.auto = True
            else:
                self.auto = False
            ball.play = True

    def move(self, speed=1):
        if self.rect.y < ball.rect.y:
            self.rect.y += speed
        if self.rect.y > ball.rect.y:
            self.rect.y -= speed

        if self.rect.x > 750:
            if self.rect.x < ball.rect.x:
                self.rect.x += speed
                self.flip = False
            if self.rect.x > ball.rect.x:
                self.rect.x -= speed
                self.flip = True
        if self.rect.colliderect(ball.rect):
            ball.bx *= -1
            if self.rect.y > 300:
                ball.by = -3
            elif self.rect.y < 300:
                ball.by = 3

    def update(self):
        screen.blit(pygame.transform.rotate(pygame.transform.flip(self.img, self.flip, False),self.angle), self.rect)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ball.png').convert_alpha()
        self.rect = self.image.get_rect(center=(450, 300))
        self.bx = 20
        self.by = 4
        self.angle = 0
        self.hit = 151
        self.play = False

    def update(self):
        global player, ai_player
        screen.blit(pygame.transform.rotate(self.image, int(self.angle)), self.rect)
        self.angle += 0.15
        if self.play:
            self.rect.x += self.bx
            self.rect.y += self.by
        if self.rect.x < 11 or self.rect.x > screen.get_width() - 9:
            if ball.rect.x < 11:
                ai_player.score += 1
            elif ball.rect.x > screen.get_width() - 9:
                player.score += 1
            self.goto(450, 300)
            self.play = False

        if self.rect.y < 11 or self.rect.y > screen.get_height() - 9:
            if ball.rect.x < 450:
                ai_player.score += 1
            elif ball.rect.x > 450:
                player.score += 1
            self.goto(450, 300)
            self.play = False

    def goto(self, x, y):
        self.rect.x = x
        self.rect.y = y


player = Player((0, 250))
ai_player = Player((880, 250))
ball = Ball()

net = pygame.Surface((1, 600))


court_img = pygame.image.load('tennis-court.png')
court_rect = court_img.get_rect(topleft=(0, 200))
pygame.font.init()
font = pygame.font.SysFont('CourierSWA.ttf', 50)
scores = font.render(f'{player.score}  {ai_player.score}', True, (255, 255, 255))
da_player = 'NO one'
winning = font.render(f'{da_player} WON!', True, (255, 255, 255))

while True:
    winning = font.render(f'{da_player} WON!', True, (255, 255, 255))
    # print(f'{player.score}:{ai_player.score}')
    scores = font.render(f'{player.score}  {ai_player.score}', True, (255, 255, 255))
    screen.fill('light green')
    screen.blit(net, (450, 0))
    screen.blit(scores, scores.get_rect(center=(450,100)))
    player.update()
    ai_player.update()
    if player.score < 30:
        player.input()
    else:
        da_player = 'The player on the left'
        screen.blit(winning, (300,300))
    if ai_player.score < 30:
        ai_player.input(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_e, pygame.K_q)
    else:
        da_player = 'This player on the right'
        screen.blit(winning, (600, 300))
    if ai_player.auto:
        ai_player.move()
    if player.auto:
        player.move()
    if player.score < 30 or ai_player.score < 30:
        ball.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    clock.tick(30)
