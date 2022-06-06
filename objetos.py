import pygame
import cores
import random

class Retangulo():

    def __init__(self, x, y, lar, alt):
        self.x = x
        self.y = y
        self.lar = lar 
        self.alt = alt 

    def gerar(self, janela):
        pygame.draw.rect(janela, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (self.x, self.y, self.lar, self.alt))
