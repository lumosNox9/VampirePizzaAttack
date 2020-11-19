#Import libraries
import pygame
from pygame import *

pygame.init()


#create window
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
WINDOW_RES = (WINDOW_WIDTH,WINDOW_HEIGHT)

GAME_WINDOW = display.set_mode(WINDOW_RES)
display.set_caption('Attack of the Vampire Pizzas!')

#setting up images
pizza_img = image.load('gameassets/vampire.png')
pizza_surf = Surface.convert_alpha(pizza_img)
VAMPIRE_PIZZA = transform.scale(pizza_surf, (100,100))
GAME_WINDOW.blit(VAMPIRE_PIZZA, (900,400))


#pepperoni
draw.circle(GAME_WINDOW, (255,0,0), (925, 425), 25, 0)

#rectangle brown
draw.rect(GAME_WINDOW, (160,82,45), (895,395,110,110), 5)

draw.rect(GAME_WINDOW, (160,82,45), (895,295,110,110), 0)

#game loop
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False
    display.update()


pygame.quit()
