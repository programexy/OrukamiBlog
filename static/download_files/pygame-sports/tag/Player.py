import pygame

pygame.init()
pygame.font.init()

class player(pygame.sprite.Sprite):
    def __init__(self,name,play,keyup,keydw,keyrt,keylt,direc,pos,display):
        super().__init__()

        self.status = 'normal'

        self.direc = pygame.math.Vector2(1,0)

        self.img = pygame.Surface((20,20))
        self.img.fill(play)
        self.rect = self.img.get_rect(topleft = pos)

        self.keyup,self.keydw,self.keyleft,self.keyright = keyup,keydw,keylt,keyrt
        self.direcstr = direc

        self.scale = 1.5
        self.display = display

        #name
        self.font = pygame.font.SysFont('robot fonts/Roboto-Black.ttf', 25)
        self.font_img = self.font.render(name,False,(0,0,0))
        self.font_rect = self.font_img.get_rect(midbottom=(self.rect.x+20,self.rect.y-10))
    def key_input(self):
        key = pygame.key.get_pressed()

        if key[self.keyup]:
            if self.rect.y >= 0:   
                self.direc.y = -1
                self.direcstr = 'top'
                #self.hand_rect = self.hand.get_rect(topleft = self.rect.bottomleft)
            else:
                self.rect.y = 0

        elif key[self.keydw]:
            if self.rect.y <= 600-20:
                #self.rect.y = 600-20
                self.direc.y = 1
                self.direcstr = 'bottom'
            else:
                self.rect.y = 600-20
                #self.hand_rect = self.hand.get_rect(bottomright = self.rect.topright)
        else:
            self.direc.y = 0

        if key[self.keyright]:
            if self.rect.x <= 1000-20:
                #self.rect.x = 1000-20
                self.direc.x = 1
                self.direcstr = 'right'
            else:
                self.rect.x = 1000-20      

        elif key[self.keyleft]:
            if self.rect.x >= 0:
                self.direc.x = -1
                self.direcstr = 'left'
            else:
                self.rect.x = 0
        else:
            self.direc.x = 0
            
    def update(self):
        self.key_input()
        self.font_rect = self.font_img.get_rect(midbottom=(self.rect.x+(self.img.get_width()/2),self.rect.y-10))
        #self.find_stage()
        self.display.blit(self.img,self.rect)
        self.move()
        self.display.blit(self.font_img, self.font_rect)
        #screen.blit(self.hand,self.hand_rect)
    def move(self):
            self.rect.x += self.direc.x*5
            self.rect.y += self.direc.y*5

    def tag(self,other):
        if self.status == 'tag':
            if self.scale == 1.5:
                self.img = pygame.transform.scale(self.img, (self.img.get_width()*self.scale,self.img.get_height()*self.scale))
                self.scale = 0
            if self.rect.colliderect(other.rect):
                other.status = 'tag'
                self.status = 'normal'
                other.rect.y += 40

        else:
            if self.scale != 1.5:
                self.scale = 1.5
                self.img = pygame.transform.scale(self.img, (self.img.get_width()*1/self.scale,self.img.get_height()*1/self.scale))
                