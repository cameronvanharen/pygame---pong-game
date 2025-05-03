import pygame
import os


WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60 #frames per second

PADDLE_WIDTH, PADDLE_HEIGHT = 60,20

pygame.display.set_caption("pongGame")

class Paddle():
    def __init__(self, dimension):
        self.rect = pygame.Rect(WIDTH/2, HEIGHT - 100, PADDLE_WIDTH, PADDLE_HEIGHT)

    def updateX(self, x_diff):
        self.rect.x += x_diff

    def updateY(self, y_diff):
        self.rect.y += y_diff


#load a new image from a file "spaceship_yellow.png" using pygame.image.load
#YELLOW_SPACESHIP_IMAGE = 

#create a new surface for this image using pygame.Surface.convert_alpha
#YELLOW_SPACESHIP = 
# rotate this image and scale it using pygame.transform 
#YELLOW_SPACESHIP = 

#define a draw_window function that displays all elements on the screen
paddle = Paddle((PADDLE_WIDTH,PADDLE_HEIGHT))
def draw_window():
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
    pygame.draw.rect(WIN, WHITE, paddle.rect)
    # Display the YELLOW_SPACESHIP surface using pygame.surface.blit
    
   
game_running = True
while game_running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    #check for all the events that can occur
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        if paddle.rect.x > 5:
            paddle.updateX(0-5)

    if keys_pressed[pygame.K_RIGHT]:
        if paddle.rect.x < WIDTH - PADDLE_WIDTH - 5:
            paddle.updateX(5)
        
    draw_window()
    pygame.display.update()
    


    
    

pygame.quit()