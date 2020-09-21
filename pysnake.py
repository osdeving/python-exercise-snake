import pygame
import time


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Pysnake')

snake = [(200, 200), (210, 200), (220,200)]
clock = pygame.time.Clock()

direction = RIGHT


# game loop
while True:
    clock.tick(10)

    go = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            go = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = UP
            if event.key == pygame.K_DOWN:
                direction = DOWN
            if event.key == pygame.K_LEFT:
                direction = LEFT
            if event.key == pygame.K_RIGHT:
                direction = RIGHT

            if event.key == pygame.K_SPACE:
                snake.append((0,0))

    
    if(not go):
        break


    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    # atualizando a tela
   


    screen.fill((0,0,0))
    for pos in snake:
        pygame.draw.rect(screen, (255,255,255), [pos[0],pos[1],10,10])

    pygame.display.update()
