# CS320 Programming Language
# Author: Joe Do & Stuart Larsen
# Date: Feb 20, 2018
# The purpose of this program is to create a clone of the Flappy Bird game

import pygame
import random
import time

# initiate pygame module
pygame.init()

# set text color
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)

# set width and height for the game
display_width  = 288
display_height = 512
bird_height    = 24
base_height    = 112

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()

# load all the graphics and sound here
startScreen  = pygame.image.load('assets/images/message.png')
birdImage    = pygame.image.load('assets/images/redbird-upflap.png')
pipeImage    = pygame.image.load('assets/images/pipe-red.png')
bg           = pygame.image.load('assets/images/background-night.png')
base         = pygame.image.load('assets/images/base.png')
gameover     = pygame.image.load('assets/images/gameover.png')
soundWing    = pygame.mixer.Sound('assets/audio/wing.wav')
soundDie     = pygame.mixer.Sound('assets/audio/die.ogg')
soundPoint   = pygame.mixer.Sound('assets/audio/point.ogg')

#display start screen as soon as game loads

# # create bird object
# class Bird(object):
#     def __init__(self, image = pygame.image.load('assets/images/redbird-upflap.png')):
#         self.image = image
#
# # inititate a new bird and load new image as parameter
# newBird = Bird(pygame.image.load('assets/images/bluebird-upflap.png'))

# bird function to display the bird
def bird(x, y):
    gameDisplay.blit(birdImage, (x, y)) # blit bird image in x and y coordinates

def movePipe():
   for x in range (0,5):
       pipePosition = pipeImage.get_rect().move(275,random.randint(175, 325))
       #invertPipePosition = redPipe.get_rect().move(275, 0)
       gameDisplay.blit(pipeImage, pipePosition)
       pygame.display.update()
       for x in range (200):
           gameDisplay.blit(bg, pipePosition, pipePosition)
           pipePosition = pipePosition.move(-2,0)
           gameDisplay.blit(pipeImage, pipePosition)
           gameDisplay.blit(startScreen,(55, 100))
           gameDisplay.blit(base,(0,400))
           pygame.display.update()
           pygame.time.delay(10)

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    message = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text, message)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    # message_display('You Crashed')
    game_loop()

def game_loop():

    # Keep track of x and y coordinates of the bird
    x = display_width / 3
    y = (display_height - base_height) / 2

    y_change = 0

    thing_startx = display_width + 20
    thing_starty = 0
    thing_speed  = 14
    thing_width  = 30
    thing_height = (display_height - base_height) / 2

    # when crashed is true, quit the game
    gameExit = False

    while not gameExit:
        for event in pygame.event.get(): # event-handling's loop
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN: # this event happens when a key is pressed
                if event.key == pygame.K_SPACE: # press spacebar to jump
                    soundWing.play()
                    y_change = -7

            if event.type == pygame.KEYUP: # this event happens when a key is released
                if event.key == pygame.K_SPACE:
                    y_change = 2

        y += y_change
        gameDisplay.blit(bg, (0, 0)) # draw background
        gameDisplay.blit(base,(0, display_height - 112)) # draw base

        # thingx, thingy, thingw, thingh, color
        # things(thing_startx, thing_starty, thing_width, thing_height, white)
        # thing_startx -= 10
        # thing_height = random.randrange(10, (display_height - base_height) / 2)

        bird(x, y) # draw bird
        # movePipe()
        # When bird hit base, pipe or top of screen, it will crash
        if y > (display_height - bird_height - base_height) or y < 0:
            soundDie.play()
            time.sleep(1)
            crash()

        if thing_startx < display_width:
            thing_startx = 0 + thing_speed

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
