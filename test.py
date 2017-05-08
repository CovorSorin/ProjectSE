import pygame,sys
import threading
import time
from threading import Thread
from pygame.locals import *

def exit_app():
    pygame.quit()
    sys.exit(0)
    
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# window/screen width and height
WIDTH = 600
HEIGHT = 600

# default background is black
screen = pygame.display.set_mode((WIDTH, HEIGHT))

radius = 15

# semaphore rules
isRed = False

def car(startPos, endPos, speed):

    for delta in range(startPos, endPos, speed):
        x = speed + delta
        y = 305
        position = (x, y)

        
        if isRed:
            endPos = 280
            print "changed"
            
        # this erases the old sreen with black
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, position, radius, 0)
        
        # update screen
        pygame.display.flip()
        
        # small time delay
        milliseconds = 50
        pygame.time.delay(milliseconds)
        
c1 = Thread(target = car, args = (0, 620, 5))
c1.start()

# app loop
running = True
while running:

    # change semaphore
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == pygame.K_k:
                isRed = not isRed
                print "Is red" , str(isRed)
            
    # exit app
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            exit_app()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                exit_app()
