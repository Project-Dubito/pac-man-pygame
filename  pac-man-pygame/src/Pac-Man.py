'''
Created on 2011-4-6

@author: panweijing@corp.netease.com
'''
import pygame
import random

black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)

wall_height = 2
wall_width = 64 + wall_height
screen_width = 800
screen_height = 700
alien_mid = 15
row = 10
col = 10

class Object(pygame.sprite.Sprite):  
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self) 

        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, horizontal):
        pygame.sprite.Sprite.__init__(self) 
        if horizontal == True:
            self.image = pygame.Surface([wall_width, wall_height])
        else:
            self.image = pygame.Surface([wall_height, wall_width])
        self.image.fill(color)
        self.rect = self.image.get_rect()

pygame.init()
screen = pygame.display.set_mode([screen_width,screen_height])

walls = pygame.sprite.RenderPlain()
aliens = pygame.sprite.RenderPlain()
all_sprites = pygame.sprite.RenderPlain()

player = Object("res/ufo.png")
player.rect.x = wall_height
player.rect.y = wall_height

all_sprites.add(player)

wall_list = []
for r in range(row):
    for c in range(col):
        wall = None
        tag = random.randrange(3) 
        wall_list.append(tag)
        if r == 0 or tag & 1:
            wall = Wall(blue, True)
            wall.rect.x = (wall_height + player.rect.width) * c
            wall.rect.y = (wall_height + player.rect.height) * r
            walls.add(wall)
            all_sprites.add(wall)
        if c == 0 or tag & 2:
            wall = Wall(blue, False)
            wall.rect.x = (wall_height + player.rect.width) * c
            wall.rect.y = (wall_height + player.rect.height) * r
            walls.add(wall)
            all_sprites.add(wall)
        if c == col - 1:
            wall = Wall(blue, False)
            wall.rect.x = (wall_height + player.rect.width) * col
            wall.rect.y = (wall_height + player.rect.height) * r
            walls.add(wall)
            all_sprites.add(wall)
        if r == row - 1:
            wall = Wall(blue, True)
            wall.rect.x = (wall_height + player.rect.width) * c
            wall.rect.y = (wall_height + player.rect.height) * row
            walls.add(wall)
            all_sprites.add(wall)
        
        alien = Object("res/alien.png")
        alien.rect.x = (wall_height + player.rect.width) * c + wall_height + alien_mid
        alien.rect.y = (wall_height + player.rect.height) * r + wall_height + alien_mid
        aliens.add(alien)
        all_sprites.add(alien)

done = False
clock = pygame.time.Clock()
score = 0
while done==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if tuple(screen.get_at((player.rect.x - 1, player.rect.y)))[2] == 0:
                    player.rect.x -= wall_height + player.rect.width
            if event.key == pygame.K_RIGHT:
                if tuple(screen.get_at((player.rect.x + player.rect.width + 1, player.rect.y)))[2] == 0:
                    player.rect.x += wall_height + player.rect.width
            if event.key == pygame.K_UP:
                if tuple(screen.get_at((player.rect.x, player.rect.y - 1)))[2] == 0:
                    player.rect.y -= wall_height + player.rect.height
            if event.key == pygame.K_DOWN:
                if tuple(screen.get_at((player.rect.x, player.rect.y + player.rect.height + 1)))[2] == 0:
                    player.rect.y += wall_height + player.rect.height
            
    screen.fill(black)
    Objects_hit_list = pygame.sprite.spritecollide(player, aliens, True)  
    
    if len(Objects_hit_list) > 0:
        score += len(Objects_hit_list)
        print( score )
        
    all_sprites.draw(screen)
    clock.tick(20)
    pygame.display.flip()

pygame.quit()


