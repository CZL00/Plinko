import pygame
import pymunk
import random

pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plinko")

space = pymunk.Space()
space.gravity = (0, 1000)  

# Color
cyan = (180, 220, 220)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Basic Setting
ball_radius = 10
obstacle_radius = 10
rows = 20
spacing = obstacle_radius * 3
gap_factor = 2

# Obstacle
def create_obstacles():
    obstacles = []
    for row in range(rows):
        for col in range(row + 1):
            if row == 0 and col == 0:
                continue

            x = WIDTH / 2 + (col - row / 2) * spacing * gap_factor
            y = 100 + row * (spacing * (3 ** 0.5) / 1.5)
            body = pymunk.Body(0, 0, pymunk.Body.STATIC)
            body.position = x, y
            shape = pymunk.Circle(body, obstacle_radius)
            shape.elasticity = 1
            space.add(body, shape)
            obstacles.append(shape)
    return obstacles

# Ball
def create_ball():
    body = pymunk.Body(1, 100)

    x = WIDTH // 2 + random.randint(-50, 50)
    body.position = x, 10
    
    shape = pymunk.Circle(body, ball_radius)
    shape.elasticity = 0.5
    space.add(body, shape)
    return shape

obstacles = create_obstacles()

running = True
balls = []

#Main Loop
while running:
    screen.fill(cyan)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(create_ball())

    space.step(1 / 60.0)

    for obstacle in obstacles:
        position = int(obstacle.body.position.x), int(obstacle.body.position.y)
        pygame.draw.circle(screen, RED, position, obstacle_radius)

    for ball in balls:
        position = int(ball.body.position.x), int(ball.body.position.y)
        pygame.draw.circle(screen, BLACK, position, ball_radius)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
