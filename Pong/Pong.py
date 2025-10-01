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
        self.box = pygame.Rect(screen_center[0]-screen.get_width()/3/2,screen.get_height()-screen.get_height()/8/2-50,screen.get_width()/3,screen.get_height()/10)
        self.positions = [self.box.center]
    
    def get_velocity(self):
        if len(self.positions) == 2:
            return [self.positions[1][0]-self.positions[0][0],self.positions[1][1]-self.positions[0][1]]
        return [0,0]

boule = Ball()

player = Bar()

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # boule.is_dragged = pygame.mouse.get_pressed()[0] and pygame.mouse.get_focused()

    if not boule.is_dragged:
        #boule.velocity[1]+=0.3
        boule.position[0] += boule.velocity[0]
        boule.position[1] += boule.velocity[1]

        
        if boule.position[0] >= screen.get_width() - 40:
            boule.position[0] = screen.get_width() - 40
            boule.velocity[0] *= -1  
            #boule.velocity[1] *= 0.80
            #boule.velocity[0] *= 0.80
        elif boule.position[0] <= 20:
            boule.position[0] = 20
            boule.velocity[0] *= -1
            #boule.velocity[1] *= 0.80
            #boule.velocity[0] *= 0.80


        # if boule.position[1] >= screen.get_height() - 40:
        #     boule.position[1] = screen.get_height() - 40
        #     boule.velocity[1] *= -1  
        #     boule.velocity[1] *= 0.80
        #     boule.velocity[0] *= 0.80
        

        
        if boule.position[1] <= 20:
            boule.position[1] = 20
            boule.velocity[1] *= -1
            #boule.velocity[1] *= 0.80
            #boule.velocity[0] *= 0.80

        if player.box.collidepoint(boule.position[0], boule.position[1]+40):
            boule.position[1] = player.box.top - 40
            print(player.get_velocity())
            boule.velocity[1] *= -1
            boule.velocity[0] += player.get_velocity()[0]
            boule.velocity[0] = max(-20,boule.velocity[0])
            boule.velocity[0] = min(20,boule.velocity[0])
            
            #boule.velocity[1] *= 0.80
            #boule.velocity[0] *= 0.80
        
    #else :
        #boule.position = list(pygame.mouse.get_pos())
        #boule.velocity = list(pygame.mouse.get_rel())
    
    

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

