import pygame
import os
pygame.init()




WIDTH,HEIGHT = 500,300
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60



score = 0
gameOver = False


font = pygame.font.Font('freesansbold.ttf', 16)

PADDLE_WIDTH, PADDLE_HEIGHT = 60,20
BALL_RADIUS = 10

x_add = 1
y_add = 1

pygame.display.set_caption("pongGame")

class Paddle():
    def __init__(self, dimension):
        self.rect = pygame.Rect(WIDTH/2, HEIGHT - 100, PADDLE_WIDTH, PADDLE_HEIGHT)

    def updateX(self, x_diff):
        self.rect.x += x_diff

    def updateY(self, y_diff):
        self.rect.y += y_diff

    def getRect(self):
        return self.rect

class Ball():
    def __init__(self, dimension):
        self.rect = pygame.Rect(100, 30, BALL_RADIUS,BALL_RADIUS)
        self.x_vel = 2
        self.y_vel = 2
    
    def updateX(self, x_diff):
        self.rect.x += x_diff

    def invertX(self):
        if self.rect.x < 0:
            self.x_vel = 0 + abs(self.x_vel)

        if self.rect.x > WIDTH:
            self.x_vel = 0 - abs(self.x_vel)

    def updateY(self, y_diff):
        self.rect.y += y_diff

    def invertY(self):
        if self.rect.y < 0:
           self.y_vel = abs(self.y_vel)

        if self.rect.y > HEIGHT:
           self.y_vel = 0 - abs(self.y_vel)
           global gameOver
           gameOver = True
        
    def invertYPaddle(self):
        global score
        self.y_vel = 0 - abs(self.y_vel)
        score += 1

    def getRect(self):
        return self.rect

        
#define a draw_window function that displays all elements on the screen
paddle = Paddle((PADDLE_WIDTH,PADDLE_HEIGHT))
ball = Ball((BALL_RADIUS, BALL_RADIUS))


def draw_window():
    pygame.draw.rect(WIN, BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
    pygame.draw.rect(WIN, WHITE, pygame.Rect(paddle.rect.x, paddle.rect.y, PADDLE_WIDTH, PADDLE_HEIGHT))
   # print(paddle.getRect())
    #
   # print(paddle.rect.x)
    pygame.draw.circle(WIN, WHITE, (ball.rect.x, ball.rect.y), BALL_RADIUS)
    text = font.render(f'Score: {score}', True, WHITE, None)
    gameOverText = font.render(f'Your final score: {score}', True, WHITE, None)
    textRect = text.get_rect()
    gameOverTextRect = gameOverText.get_rect()
    gameOverTextRect.center = (WIDTH/2, HEIGHT/2)
    WIN.blit(text, textRect)
    if gameOver == True:
        pygame.draw.rect(WIN, BLACK, pygame.Rect(0,0,WIDTH,HEIGHT))
        WIN.blit(gameOverText, gameOverTextRect)

    
   
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

    if (ball.rect.colliderect(paddle.rect)):
        ball.invertYPaddle()
    
    if gameOver == False:

        ball.updateX(ball.x_vel)
        ball.updateY(ball.y_vel)
    
    
        
    draw_window()
    pygame.display.update()

pygame.quit()