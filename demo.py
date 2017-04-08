import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

def exit_app():
    pygame.quit()
    sys.exit(0)
    
class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('1.png'))
        self.images.append(load_image('2.png'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 64, 64)

    def update(self, ind):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        # if self.index >= len(self.images):
        #   self.index = 0
        # self.image = self.images[self.index]
        self.image = self.images[ind]

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)

    isRed = True
    
    while True:
        event = pygame.event.poll()
   
        if event.type == pygame.QUIT:
            exit_app()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_app()
                
            # determine if a letter key was pressed 
            if event.key == pygame.K_SPACE:
                isRed = not isRed
            elif event.key == pygame.K_s:
                isRed = not isRed
            elif event.key == pygame.K_d:
                isRed = not isRed

        # Calling the 'my_group.update' function calls the 'update' function of all 
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        
        my_group.draw(screen)
        if not isRed:
            my_group.update(0)
            pygame.display.flip()
        else:
            my_group.update(1)
            pygame.display.flip()

if __name__ == '__main__':
    main()
