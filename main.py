import pygame
from pygame.locals import *
import sys
import random

import cores
import controles
import objetos

FPS = 60

def main():
    pygame.init()
    clock = pygame.time.Clock()

    ALTURA = 600
    LARGURA = 400

    # RESOLUÇÃO
    DISPLAYSURF = pygame.display.set_mode((ALTURA, LARGURA))

    # TITULO DA JANELA
    pygame.display.set_caption('TEST PCG')

    # CONDIÇÂO
    v = 0

    # ITERAÇÕES FOR
    xfor = 0
    yfor = 0

    countx = 0
    county = 0

    # DIMENSÕES DO RETANGULO
    x = 0
    y = 0
    lar = 100
    alt = 100

    # INICIAR OBJETOS
    ret = objetos.Retangulo(x, y, lar, alt)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # RENDERIZA RENTANGULO        
        if v == 0:
            for yfor in range (4):
                for xfor in range (6):
                    objetos.Retangulo.gerar(ret, DISPLAYSURF)
                    ret.x += 100
                
                ret.x = 0
                ret.y += 100    

            v = 1

        pygame.display.update()

        # COMANDO DE SAIR
        comando = pygame.key.get_pressed()
        controles.controle(comando)

        
if __name__ == '__main__':
    main()
