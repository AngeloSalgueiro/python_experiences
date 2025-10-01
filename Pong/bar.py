import pygame

class Bar:
    def __init__(self, height, center):
        self.box = pygame.Rect(center[0]-250/2,height,250,30)
        self.positions = [self.box.center]
    
    def get_velocity(self):
        if len(self.positions) == 2:
            return [self.positions[1][0]-self.positions[0][0],self.positions[1][1]-self.positions[0][1]]
        return [0,0]