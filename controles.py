import pygame
import sys

def controle(comando):
    if comando[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
