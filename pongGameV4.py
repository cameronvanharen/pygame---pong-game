import pygame
import os


WIDTH,HEIGHT = 500,300
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60

PADDLE_WIDTH, PADDLE_HEIGHT = 60,20
BALL_RADIUS = 10

add_x_vel = 0
add_y_vel = 0

pygame.display.set_caption("pongGame")

class Paddle():
    def __init__(self, dimension):
        self.rect = pygame.Rect(WIDTH/2, HEIGHT - 100, PADDLE_WIDTH, PADDLE_HEIGHT)

    def updateX(self, x_diff):
        self.rect.x += x_diff

    def updateY(self, y_diff):
        self.rect.y += y_diff


class Ball():
    def __init__(self, dimension):
        self.rect = pygame.Rect(100, 30, 10,10)
        self.x_vel = 5
        self.y_vel = 5
    
    def updateX(self, x_diff):
        self.rect.x += x_diff

    def invertX(self):
        if self.rect.x < 0:
            self.x_vel = 2 + add_x_vel

        if self.rect.x > WIDTH*2:
            self.x_vel = -2 - add_y_vel

    def updateY(self, y_diff):
        self.rect.y += y_diff

    def invertY(self):
        if self.rect.y < 0:
            self.y_vel = 2 + add_y_vel

        if self.rect.y > HEIGHT*2:
            self.y_vel = -2 - add_y_vel

        
#define a draw_window function that displays all elements on the screen
paddle = Paddle((PADDLE_WIDTH,PADDLE_HEIGHT))
ball = Ball((BALL_RADIUS, BALL_RADIUS))
def draw_window():
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
    pygame.draw.rect(WIN, WHITE, paddle.rect)
    pygame.draw.circle(WIN, WHITE, (ball.rect.x/2, ball.rect.y/2), BALL_RADIUS)
    
   
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
    
    
    ball.invertX()
    ball.invertY()
    ball.updateX(ball.x_vel)
    ball.updateY(ball.y_vel)
    
        
    draw_window()
    pygame.display.update()

pygame.quit()