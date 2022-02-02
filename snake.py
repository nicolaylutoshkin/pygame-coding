import pygame
import random

WIDTH = 1280
HEIGHT = 720
FPS = 30
SPEED = 5
GREEN = (3, 160, 98)
WHITE = (255, 255, 255)
RED = (170, 1, 20)
flag = False

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randrange(1, 1280), random.randrange(1, 720))



class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        global flag
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flag = 'left'
            elif event.key == pygame.K_RIGHT:
                flag = 'right'
            elif event.key == pygame.K_UP:
                flag = 'up'
            elif event.key == pygame.K_DOWN:
                flag = 'down'

        if flag != False:
            if flag == 'left':
                self.rect.x -= SPEED
            elif flag == 'right':
                self.rect.x += SPEED
            elif flag == 'up':
                self.rect.y -= SPEED
            elif flag == 'down':
                self.rect.y += SPEED



clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 





all_sprites = pygame.sprite.Group()
snake = Snake()
all_sprites.add(snake)
apple = Apple()
all_sprites.add(apple)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE GAME")
clock = pygame.time.Clock()

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(GREEN)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()