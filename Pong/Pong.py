import pygame
import numpy as np

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,700))
screen_center = [screen.get_width() / 2,screen.get_height() / 2]
clock = pygame.time.Clock()
running = True
dt = 0

class Ball:
    def __init__(self):
        self.position = screen_center.copy()
        self.velocity = [0.0,5.0]
        self.is_dragged = False

class Bar:
    def __init__(self):
        self.box = pygame.Rect(screen_center[0]-screen.get_width()/3/2,screen.get_height()-100,screen.get_width()/3,50)
        self.positions = [self.box.center]
    
    def get_velocity(self):
        if len(self.positions) == 2:
            return [self.positions[1][0]-self.positions[0][0],self.positions[1][1]-self.positions[0][1]]
        return [0,0]

boule = Ball()
player = Bar()

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("purple")

    boule.position[0] += boule.velocity[0]
    boule.position[1] += boule.velocity[1]

    if boule.position[0] >= screen.get_width() - 40:
        boule.position[0] = screen.get_width() - 40
        boule.velocity[0] *= -1  


    elif boule.position[0] <= 20:
        boule.position[0] = 20
        boule.velocity[0] *= -1
        
    if boule.position[1] <= 20:
        boule.position[1] = 20
        boule.velocity[1] *= -1

    if player.box.collidepoint(boule.position[0], boule.position[1]+40):
        boule.position[1] = player.box.top - 40
        boule.velocity[1] *= -1
        boule.velocity[0] += player.get_velocity()[0]
        boule.velocity[0] = max(-20,boule.velocity[0])
        boule.velocity[0] = min(20,boule.velocity[0])
    

    if pygame.mouse.get_pressed()[0]:
        player.box.center = (list(pygame.mouse.get_pos())[0], player.box.center[1])
        if len(player.positions) == 2:
            player.positions.append(player.box.center)
            player.positions.pop(0)
        else :
            player.positions.append(player.box.center)
        


    pygame.draw.circle(screen, "red", boule.position, 40)

    pygame.draw.rect(screen, "white", player.box)


    # flip() the display to put your work on screen
    pygame.display.flip()
        
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

