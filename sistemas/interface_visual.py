import os
import sys
import pygame

pygame.init()
pygame.font.init()


# Dimensões da janela HD
LARGURA, ALTURA = 1280, 720
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cronicas do Reino - RPG")

# Cores do Tema
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AMARELO_OURO = (240, 190, 40)
CINZA_ESCURO = (25, 25, 35)

# Fontes
FONTE_TITULO = pygame.font.SysFont
