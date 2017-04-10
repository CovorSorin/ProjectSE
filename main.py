import pygame, sys
import threading
import time
from threading import Thread
from pygame.locals import *

# functions
def exit_app():
    pygame.quit()
    sys.exit(0)

def load_image(name):
    image = pygame.image.load(name)
    return image

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# circle class
# a circle represents a car
class Circle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, (BLUE), (25, 25), 25, 0)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
def car():
        circle = Circle()
        circle.update()
            
# set up pygame
pygame.init()
clock = pygame.time.Clock()

# set up the app window
HEIGHT = 600
WIDTH = 600

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Traffic Simulation')
DISPLAYSURF.fill((255, 255, 255))

# draw on the screen
pygame.draw.circle(DISPLAYSURF, BLUE, (20, 310), 20, 0)

x = 0
c1 = Thread(target = car())
c1.start()
# run the app loop
while True:
    
    # exit app
    for event in pygame.event.get():
        if event.type == QUIT:
            exit_app()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_app()

