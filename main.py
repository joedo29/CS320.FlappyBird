# CS320 Programming Language
# Author: Joe Do & Stuart Larsen
# Date: Feb 20, 2018
# The purpose of this program is to create a clone of the Flappy Bird game

import pygame

# initiate pygame module
pygame.init()

# set width and height for the game
display_width = 288
display_height = 512

white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()

# load all the graphics here
birdImage = pygame.image.load('assets/images/redbird-upflap.png')

# bird function to display the bird
def bird(x, y):
    gameDisplay.blit(birdImage, (x, y)) # blit bird image in x and y coordinates

# Keep track of x and y coordinates of the bird
x = display_width / 2
y = display_height / 2

y_change = 0

# Adding background to the game
bg = pygame.image.load('assets/images/background-night.png')

# when crashed is true, quit the game
crashed = False

while not crashed:
    for event in pygame.event.get(): # event-handling's loop
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN: # this event happens when a key is pressed
            if event.key == pygame.K_j: # press 'j' to jump
                y_change = -10

        if event.type == pygame.KEYUP: # this event happens when a key is released
            if event.key == pygame.K_j:
                y_change = 2

    y += y_change
    # gameDisplay.fill(white)
    gameDisplay.blit(bg, (0, 0))
    bird(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
