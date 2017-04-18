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

def car():
    for delta in range(0, 300, 10):
        x = 20 + delta
        y = 20
        position = (x, y)
        
        # this erases the old sreen with black
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, position, radius, 0)
        
        # update screen
        pygame.display.flip()
        
        # small time delay
        milliseconds = 50
        pygame.time.delay(milliseconds)
        
c1 = Thread(target = car())
c1.start()

# app loop
running = True
while running:

    # exit app
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            exit_app()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                exit_app()
