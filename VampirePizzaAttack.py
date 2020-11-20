#Import libraries
import pygame
from pygame import *
from random import randint

pygame.init()

clock=time.Clock()

#create window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH,WINDOW_HEIGHT)

#tile
WIDTH = 100
HEIGHT = 100

#colors
WHITE = (255, 255, 255)

SPAWN_RATE = 360
FRAME_RATE=60

REG_SPEED = 2
SLOW_SPEED = 1

#create window
GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')

#background
background_img = image.load('gameassets/restaurant.jpg')
background_surf = Surface.convert_alpha(background_img)
BACKGROUND = transform.scale(background_surf, WINDOW_RES)
GAME_WINDOW.blit(BACKGROUND, (0,0))


#setting up images
pizza_img = image.load('gameassets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (WIDTH,HEIGHT))


#------------------------------
#set up classes

class VampireSprite(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed=REG_SPEED
        self.lane=randint(0,4)
        all_vampires.add(self)
        self.image=VAMPIRE_PIZZA.copy()
        y=50 + self.lane*100
        self.rect=self.image.get_rect(center=(1100,y))

    def update(self,game_window):
        #erase last image
        game_window.blit(BACKGROUND, (self.rect.x, self.rect.y), self.rect)
        #change location
        self.rect.x-=self.speed
        #draw image to new location
        game_window.blit(self.image, (self.rect.x, self.rect.y))
        
class BackgroundTile(sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.effect=False
        self.rect=rect
#--------------------
#class instances and groupd
all_vampires=sprite.Group()





#loop and draw tiles
tile_grid=[]
tile_color=WHITE
for row in range(6):
    row_of_tiles=[]
    tile_grid.append(row_of_tiles)
    
    for column in range(11):
        tile_rect=Rect(WIDTH*column, HEIGHT*row, WIDTH, HEIGHT)
        new_tile=BackgroundTile(tile_rect)
        row_of_tiles.append(new_tile)
        draw.rect(BACKGROUND, tile_color, (WIDTH*column,HEIGHT*row,WIDTH,HEIGHT),1)
    
GAME_WINDOW.blit(BACKGROUND, (0,0))


#-------------------------------------
#game loop
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False

#event for when a user clicks in a space
        elif event.type == MOUSEBUTTONDOWN:
            coordinates=mouse.get_pos()
            x=coordinates[0]
            y=coordinates[1]
            tile_y=y//100
            tile_x=x//100
            tile_grid[tile_y][tile_x].effect=True
           

#spawn sprites
    if randint(1,SPAWN_RATE)==1:
        VampireSprite()

#--------------------------------------
#collission detection
    for vampire in all_vampires:
        tile_row=tile_grid[vampire.rect.y // 100]
        vamp_left_side=vampire.rect.x//100
        vamp_right_side=(vampire.rect.x + vampire.rect.width)//100

        if 0 <= vamp_left_side <= 10:
            left_tile = tile_row[vamp_left_side]
        else:
            left_tile = None

        if 0 <= vamp_right_side <=10:
            right_tile = tile_row[vamp_right_side]
        else:
           right_tile=None
           

        #check left side
        if bool(left_tile) and left_tile.effect:
            vampire.speed=SLOW_SPEED
            
        #check right side
        if bool(right_tile) and right_tile.effect:
            if right_tile!=left_tile:
                vampire.speed=SLOW_SPEED
                
#delete when it leaves the screen
        if vampire.rect.x<=0:
            vampire.kill()
    

#--------------------------------------
#update displays
    for vampire in all_vampires:
        vampire.update(GAME_WINDOW)
            
    display.update()

clock.tick(FRAME_RATE)
#--------------------

#clean up
pygame.quit()
