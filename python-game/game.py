
import numpy as np 
import pygame 
from pygame.locals import * 
from sys import exit


pygame.init()
screen = pygame.display.set_mode((500,500), 0 ,32)
pygame.display.set_caption("Hello World!")

background = pygame.image.load('Planets.png').convert()
mouse_cursor = pygame.image.load('Rockets.png').convert_alpha()

class Tank(object): 
    def __init__(self,name):
        self.name = name 
        self.armor = 100
        self.alive = True
        self.ammo = 10
    def __str__(self):
        if self.alive: 
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else: 
            return "%s (DEAD)" % self.name
    def move(self):
        pass
    def turn(self): 
        pass
    def fire(self): 
        pass 
    def hit(self): 
        pass
    def explode(self): 
        pass 


def main():
    running = True
    while running is True: 

        for event in pygame.event.get():
            if event.type == QUIT: 
                running = False 
                exit

    screen.blit(background,(0,0))
    x,y = pygame.mouse.get_pos() 
    x -=mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor,(x,y))



if __name__ == "__main__": 
    main()