import random
import pygame,sys
import Player
def App():


    pygame.font.init()

    font = pygame.font.SysFont('robot fonts/Roboto-Bold.ttf', 250)


    timelimit = 0.5
    time = 0
    many = input('How many players are there? There must be at least two and less than or equal to 4 players:\n>')
    name1 = input('Enter your name, Player 1:')
    name2 = input('Enter your name, Player 2:')
    if int(many) >= 3:
        name3 = input('Enter your name, Player 3:')
    if many == '4':
        name4 = input('Enter your name, Player 4:')

    pygame.init()
    SCREEN_W = 1000
    SCREEN_L = 600
    display = pygame.display
    screen = display.set_mode((SCREEN_W,SCREEN_L))

    def write(text, color):
        img = font.render(text, False, color)
        screen.blit()

    def tagger_generate():
        tagger = random.randint(1,int(many))
        if tagger == 1:
            player1.status = 'tag'
        if tagger == 2:
            player2.status = 'tag'

        if tagger == 3:
            player3.status = 'tag'
        if tagger == 4:
            player4.status = 'tag'
    def tag_new():
        player1.tag(player2)
        try:
            player1.tag(player3)
        except:
            pass
        try:
            player1.tag(player4)
        except:
            player2.tag(player1)
        try:
            player2.tag(player3)
        except:
            pass
        try:
            player2.tag(player4)
        except:
            pass
        try:
            player3.tag(player2)
            player3.tag(player1)
            try:
                player3.tag(player4)
            except:
                pass
        except:
            pass
        try:
            player4.tag(player2)
            try:
                player4.tag(player3)
            except:
                pass
            player4.tag(player1)
        except:
            pass
    player1 = Player.player(name1,'white',pygame.K_w,pygame.K_s,pygame.K_d,pygame.K_a,'top',(0,0),screen)
    player2 = Player.player(name2,'blue',
    pygame.K_UP,
    pygame.K_DOWN,
    pygame.K_RIGHT,
    pygame.K_LEFT,'top',(0,600-37)
    ,screen)
    try:
        player3 = Player.player(name3,'red',
        pygame.K_t,
        pygame.K_g,
        pygame.K_h,
        pygame.K_f,'top',(1000-37,0),
        screen)
    except:
        print('there is no player 3')
    try:
        player4 = Player.player(name4,
        'orange',
        pygame.K_i,
        pygame.K_k,
        pygame.K_l,
        pygame.K_j,'top',(1000-37,600-37),screen)
    except:
        print('there is no Player 4')


    tagger_generate()

    yeet = False


    class Tree(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((500,500))
            self.image.set_alpha(random.randint(128, 200))
            self.rect = self.image.get_rect(center=(random.randint(0,1000),random.randint(0,600)))
            self.image.fill((0,155,0))
        def update(self):
            screen.blit(self.image,self.rect)


    trees = pygame.sprite.Group()
    for i in range(int(random.randint(2,5)+1)):
        trees.add(Tree())
    while not yeet:
        if time >= timelimit* 120:
            if player1.status == 'tag':
                player1.kill()

        tag_new()
        screen.fill('green')
        player1.update()
        player2.update()


        if int(many) >= 3:
            player3.update()
        if many == '4':
            player4.update()
        trees.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                yeet = True
        display.update()
        pygame.time.Clock().tick(120)

App()
