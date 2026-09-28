import random
from player import *
from cars import *
import pygame
from os import system, name


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')

# Then, whenever you want to clear the screen, just use this clear function as:

def App():
    pygame.init()
    colors = ['blue','green','grey','orange','purple','red','white','yellow']

    xandys = []

    screen = pygame.display.set_mode((600,600))
    clock = pygame.time.Clock()

    player = Player('chicken', (300,550))
    car = pygame.sprite.Group()
    for i in range(6):
        x = (random.randint(0, 10)*100)
        y = (random.randint(1, 2) * 50)
        xandys.append((x,y))
        car.add(Car(random.choice(colors), (x,y), screen))
    road = pygame.sprite.Group()
    track = pygame.sprite.Group()
    train = pygame.sprite.Group()
    font = pygame.font.SysFont('../courier/CourierSWA.ttf', 50)


    def setuproad(road):
        for i in range(21):
            x = i * 50
            for ir in range(1,3):
                y = ir*50
                road.add(Road('roadtile',(x,y), screen))
    def setuptrack(road):
        y = random.randint(2,4) * 100
        for i in range(21):
            x = i * 50
            for ir in range(1,3):
                road.add(Road('track',(x,y), screen))

        def setuptrain(train,y):
            pos = []
            for i in range(7):
                x = i*25+500
                pos.append((x,y))
            for thing in pos:
                if pos[0] == thing:
                    train.add(Train('trainhead', thing, screen))

                elif pos[-1] == thing:
                    train.add(Train('tail', thing, screen))
                else:
                    train.add(Train('middle', thing, screen))
        setuptrain(train,y)

    # for cars in car.sprites():
    #     if pygame.sprite.spritecollideany(cars, car):
    #         cars.rect.x += 100
    def restart():
        car.empty()
        road.empty()
        track.empty()
        train.empty()
        setuproad(road)
        setuptrack(track)
        for i in range(7):
            x = (random.randint(0, 10) * 100)
            y = (random.randint(1, 2) * 50)
            car.add(Car(random.choice(colors), (x, y), screen))

        for cars in car.sprites():
            if pygame.sprite.spritecollideany(cars, car):
                cars.rect.x += 100
    setuproad(road)
    setuptrack(track)
    groups = [car,train,road,track]
    mouse = pygame.mouse.get_pressed()
    run = True
    score = 0
    image = font.render(str(score), False, (255,255,255))
    while run:
        image = font.render(str(score), False, (255, 255, 255))
        mouse = pygame.mouse.get_pressed()
        pygame.display.update()
        screen.fill((0,150,0))
        clock.tick(60)
        road.update()
        track.update()
        train.update()
        car.update()
        player.update(screen)
        screen.blit(image, image.get_rect(center=(300, 20)))
        if pygame.sprite.spritecollideany(player, car) or pygame.sprite.spritecollideany(player, train):
            car.empty()
            train.empty()
            print(f'Your New score is {score}')
            score = 0
            restart()
        else:
            player.key_input()





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
                score += 1
    pygame.quit()

App()
