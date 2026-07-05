import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ALIEN_START_Y_MIN = 50
ALIEN_START_Y_MAX = 150
ALIEN_X_SPEED = 4
ALIEN_Y_SPEED = 40
BULLET_SPEED = 10
COLLISION = 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load('bg.png')
alien = pygame.image.load('Alien.png')
icon = pygame.image.load('logo.jpg')

# player
player = pygame.image.load('player.png')
player_x = PLAYER_START_X
player_y = PLAYER_START_Y
player_x_change = 0

# enemy

alien = []