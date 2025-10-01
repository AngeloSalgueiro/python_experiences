import pygame
import numpy as np
import math

pygame.init()
screen = pygame.display.set_mode((1280,600))
screen_center = [screen.get_width() / 2,screen.get_height() / 2]
clock = pygame.time.Clock()
running = True
dt = 0

class ball:
    def __init__(self, size):
        self.position = screen_center.copy()
        self.velocity = [0.0,0.0]
        self.size = size
        self.is_dragged = False

crazyball = ball(40)

def get_distance():
    x = abs(pygame.mouse.get_pos()[0]-crazyball.position[0])
    y = abs(pygame.mouse.get_pos()[1]-crazyball.position[1])
    z = x**2+y**2
    return math.sqrt(z)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    if not crazyball.is_dragged:
        if get_distance() <= crazyball.size and pygame.mouse.get_pressed()[0]:
            crazyball.is_dragged = True

        else :
            crazyball.velocity[1] += 0.3
            crazyball.position[0] += crazyball.velocity[0]
            crazyball.position[1] += crazyball.velocity[1]

            if crazyball.position[1] + crazyball.size >= screen.get_height():
                crazyball.position[1] = screen.get_height()-crazyball.size
                crazyball.velocity[1] *= -1 * 0.80
                crazyball.velocity[0] *= 0.95

            elif crazyball.position[1] - crazyball.size < 0:
                crazyball.position[1] = crazyball.size
                crazyball.velocity[1] *= -1 * 0.80
                crazyball.velocity[0] *= 0.95

            if crazyball.position[0] + crazyball.size >= screen.get_width():
                crazyball.position[0] = screen.get_width()-crazyball.size
                crazyball.velocity[0] *= -1 * 0.80
                crazyball.velocity[1] *= 0.95

            elif crazyball.position[0] - crazyball.size < 0:
                crazyball.position[0] = crazyball.size
                crazyball.velocity[0] *= -1 * 0.80
                crazyball.velocity[1] *= 0.95
        
    else :
        crazyball.position = list(pygame.mouse.get_pos())
        crazyball.velocity = list(pygame.mouse.get_rel())

        if not pygame.mouse.get_pressed()[0]:
            crazyball.is_dragged = False
        
        

    pygame.draw.circle(screen,"red",crazyball.position,crazyball.size)

    pygame.display.flip()
        
    dt = clock.tick(60) / 1000

pygame.quit()
