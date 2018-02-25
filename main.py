#it's now 11:22
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
pipe_height    = 320

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

# Flip the pipe over
pipeInvert   = pygame.transform.rotate(pipeImage,180)

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
    randomY = random.randint(175,325)
    pipePosition = pipeImage.get_rect().move(275,randomY)
    pipePositionInvert = pipeInvert.get_rect().move(275, randomY-400)

    gameDisplay.blit(pipeInvert, pipePositionInvert)
    gameDisplay.blit(pipeImage, pipePosition)

    # pygame.display.update()
    gameDisplay.blit(bg, pipePositionInvert, pipePositionInvert)
    gameDisplay.blit(bg, pipePosition, pipePosition)

    pipePositionInvert = pipePositionInvert.move(-2,0)
    pipePosition = pipePosition.move(-2,0)

    gameDisplay.blit(pipeInvert, pipePositionInvert)
    gameDisplay.blit(pipeImage, pipePosition)
    # gameDisplay.blit(startScreen,(55, 100))

    gameDisplay.blit(base,(0,400))

    pygame.display.update()
    pygame.time.delay(10)

# Display pipe up side down
def bottomPipe(xCoordinate, yCoordinate):
    gameDisplay.blit(pipeImage, (xCoordinate, yCoordinate))
    # pygame.display.update()

# Display pipe from bottom up
def topPipe(xCoordinate, yCoordinate):
    gameDisplay.blit(pipeInvert, (xCoordinate, yCoordinate))
    # pygame.display.update()

# def things(thingx, thingy, thingw, thingh, color):
#     pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

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

#def game_intro():
#    startInitialized = False
#    while not startInitialized:
#        gameDisplay.blit(bg, (0, 0))
#        gameDisplay.blit(startScreen,(55,80))
#        gameDisplay.blit(base,(0, display_height - 112))
#        pygame.display.update()
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                quit()
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_SPACE:
#                    startInitialized = True

def game_loop():

    # Keep track of x and y coordinates of the bird
    birdX       = display_width / 3
    birdY       = (display_height - base_height) / 2
    birdMove    = 0
    pipeStartX  = display_width + 10
    pipeBottomY = 250
    pipeTopY    = -170
    pipe_speed  = 4


    # display start screen at start of game, and when player loses
    startInitialized = False
    while not startInitialized:
        gameDisplay.blit(bg, (0, 0))
        gameDisplay.blit(startScreen,(55,80))
        gameDisplay.blit(base,(0, display_height - 112))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
              #  quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    startInitialized = True
                    
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
                    birdMove = -7

            if event.type == pygame.KEYUP: # this event happens when a key is released
                if event.key == pygame.K_SPACE:
                    birdMove = 2

        birdY += birdMove
        gameDisplay.blit(bg, (0, 0)) # draw background

        # draw top pipe
        bottomPipe(pipeStartX, pipeBottomY)

        gameDisplay.blit(base,(0, display_height - 112)) # draw base

        bird(birdX, birdY) # draw bird

        # draw the bottom pipe
        topPipe(pipeStartX, pipeTopY)

        pipeStartX -= pipe_speed # make the pipe move left four pixel at a time

        # When bird hit base, pipe or top of screen, it will crash
        if birdY > (display_height - bird_height - base_height) or birdY < 0:
            soundDie.play()
            time.sleep(2)
            crash()

        # bird crashes when it hits any pipe
        if birdX + 34 > pipeStartX and (birdY < pipeTopY + pipe_height or birdY + 24 > pipeBottomY):
            soundDie.play()
            time.sleep(2)
            crash()

        # moving pipes accross the screen
        if pipeStartX < -50:
            pipeStartX = display_width

            # make pipes change y coordinate randomly
            pipeTopY = random.randint(-260, -40)
            pipeBottomY = pipe_height + 100 + pipeTopY

        pygame.display.update()
        clock.tick(60)

#game_intro()
game_loop()
pygame.quit()
quit()
