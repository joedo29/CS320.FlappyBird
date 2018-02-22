# CS320 Programming Language
# Author: Joe Do & Stuart Larsen
# Date: Feb 20, 2018
# The purpose of this program is to create a clone of the Flappy Bird game
#testing committ stuff
#test round 2!
#comment for push request
#testing startscreen branch

import pygame
import random

# initiate pygame module
pygame.init()

# set width and height for the game
display_width = 288
display_height = 512

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()

# load all the graphics here
start_screen = pygame.image.load('assets/images/message.png')
birdImage = pygame.image.load('assets/images/redbird-upflap.png')
bg = pygame.image.load('assets/images/background-night.png')
base = pygame.image.load('assets/images/base.png')
gameover = pygame.image.load('assets/images/gameover.png')
soundFly = pygame.mixer.Sound('assets/audio/wing.wav')
soundFall = pygame.mixer.Sound('assets/audio/die.ogg')

#display start screen as soon as game loads

# create bird object
class Bird(object):
    def __init__(self, image = pygame.image.load('assets/images/redbird-upflap.png')):
        self.image = image

# inititate a new bird and load new image as parameter
newBird = Bird(pygame.image.load('assets/images/bluebird-upflap.png'))

# bird function to display the bird
def bird(x, y):
    gameDisplay.blit(newBird.image, (x, y)) # blit bird image in x and y coordinates

# Keep track of x and y coordinates of the bird
x = display_width / 2
y = display_height / 2

y_change = 0

# when crashed is true, quit the game
crashed = False

while not crashed:
    for event in pygame.event.get(): # event-handling's loop
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN: # this event happens when a key is pressed
            if event.key == pygame.K_SPACE: # press BACKSPACE to jump
                soundFly.play()
                y_change = -10

        if event.type == pygame.KEYUP: # this event happens when a key is released
            if event.key == pygame.K_SPACE:
                y_change = 2
                # soundFall.play()

    y += y_change
    gameDisplay.blit(bg, (0, 0))
    gameDisplay.blit(base,(0, display_height - 112))
    bird(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
