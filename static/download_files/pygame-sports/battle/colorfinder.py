import pygame,sys
pygame.init()
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()
r =0
g =0
b =0
def key_input(r,g,b):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if r < 256:# or (b <= 255 and b >= 0) or (g <= 255 and g >= 0):
            if keys[pygame.K_r]:
                r += 1
        else:
            r = 255
        if keys[pygame.K_g]:
            if g < 256:# or (g <= 255 and g >= 0):
                g += 1
            else:
                g =255
        if keys[pygame.K_b]:
            if b < 256:
                b += 1
            else:
                b = 255
        
    if keys[pygame.K_DOWN]:
        if r >= 0:# or (b <= 255 and b >= 0) or (g <= 255 and g >= 0):
            if keys[pygame.K_r]:
                r -= 1
        else:
            r = 0

        if keys[pygame.K_g]:
            if g >= 0:# or (g <= 255 and g >= 0):
                g -= 1
            else:
                g = 0
        if keys[pygame.K_b]:
            if b >= 0:
                b -= 1
            else: 
                g = 0

    return r,g,b
font = pygame.font.SysFont('roboto fonts/Roboto-Black.ttf', 60)
while True:
    r,g,b = key_input(r,g,b)
    if (r <= 255 and r >= 0) or (b <= 255 and b >= 0) or (g <= 255 and g >= 0):
        screen.fill((r,g,b))

        write = font.render(f'({r},{g},{b})',False,(255,255,255))
        writerect = write.get_rect(center = (350,100))
        screen.blit(write,writerect)

    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    clock.tick(60)
    pygame.display.update()