import pygame
import numpy as np
from ball import Ball
from bar import Bar

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,700))
screen_center = [screen.get_width() / 2,screen.get_height() / 2]
clock = pygame.time.Clock()
running = True
dt = 0

boule = Ball(screen_center.copy(), 40)
player = Bar(screen.get_height()-75, screen_center.copy())
bot = Bar(25, screen_center.copy())
score = [0,0]
my_font = pygame.font.SysFont('Comic Sans MS', 30)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("purple")

    boule.position[0] += boule.velocity[0]
    boule.position[1] += boule.velocity[1]

    if boule.position[0] >= screen.get_width() - boule.size:
        boule.position[0] = screen.get_width() - boule.size
        boule.velocity[0] *= -1  

    elif boule.position[0] <= boule.size:
        boule.position[0] = boule.size
        boule.velocity[0] *= -1
        
    if boule.position[1] <= boule.size:
        score[1]+=1
        boule.position = screen_center.copy()
        boule.velocity = [0,-5]
        player.box.center = [screen_center[0], player.box.center[1]]
        player.positions = [player.box.center]
        bot.box.center = [screen_center[0], bot.box.center[1]]
        bot.positions = [bot.box.center]

    elif boule.position[1] >= screen.get_height()-boule.size:
        score[0]+=1
        boule.position = screen_center.copy()
        boule.velocity = [0,5]
        player.box.center = [screen_center[0], player.box.center[1]]
        player.positions = [player.box.center]
        bot.box.center = [screen_center[0], bot.box.center[1]]
        bot.positions = [bot.box.center]

    if player.box.collidepoint(boule.position[0], boule.position[1]+boule.size):
        boule.position[1] = player.box.top - boule.size
        boule.velocity[1] *= -1
        boule.velocity[0] += player.get_velocity()[0]
        boule.velocity[0] = max(-20,boule.velocity[0])
        boule.velocity[0] = min(20,boule.velocity[0])

    if bot.box.collidepoint(boule.position[0], boule.position[1]-boule.size):
        boule.position[1] = bot.box.bottom + boule.size
        boule.velocity[1] *= -1
        boule.velocity[0] += player.get_velocity()[0]
        boule.velocity[0] = max(-20,boule.velocity[0])
        boule.velocity[0] = min(20,boule.velocity[0])

    # Player bzr control
    if pygame.mouse.get_pressed()[0]:
        player.box.center = (list(pygame.mouse.get_pos())[0], player.box.center[1])
        if len(player.positions) == 2:
            player.positions = [player.positions[1], player.box.center]
        else :
            player.positions.append(player.box.center)
    
    if bot.box.center[0] < boule.position[0]:
        bot.box.center = (bot.box.center[0]+10, bot.box.center[1])

        if len(bot.positions) == 2:
            bot.positions = [bot.positions[1], bot.box.center]
        else :
            bot.positions.append(bot.box.center)

    elif bot.box.center[0] > boule.position[0]:
        bot.box.center = (bot.box.center[0]-10, bot.box.center[1])
        if len(bot.positions) == 2:
            bot.positions = [bot.positions[1], bot.box.center]
        else :
            bot.positions.append(bot.box.center)


    pygame.draw.circle(screen, "red", boule.position, boule.size)

    pygame.draw.rect(screen, "white", bot.box)
    pygame.draw.rect(screen, "white", player.box)
    text_surface = my_font.render(str(score[0])+"-"+str(score[1]), False, (255, 255, 255))
    screen.blit(text_surface, (0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()
        
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

