
import pygame, sys
from data import game_rules

from pygame.constants import K_SPACE, K_f

clock = pygame.time.Clock()

pygame.init()

pygame.key.set_repeat(1,100) 

WINDOW_SIZE = (960,640)
screen = pygame.display.set_mode(WINDOW_SIZE)
display_size_X = 960
display_size_Y = 640
display = pygame.Surface((display_size_X,display_size_Y))

dead_cell = pygame.image.load("data\images\dead_cell.png")
life_cell = pygame.image.load("data\images\life_cell.png")
TILE_SIZE = 16

pygame.display.set_caption("Conway's Game of life")#title
pygame.display.set_icon(dead_cell)

map = {}

def clear_map(map):
    """utilizada para crear un mapa en blanco, sirviendo para lipiarlo tambien
    toma como argumento un diccionario"""
    y = 0
    for y in range(display_size_Y//TILE_SIZE):
        x=0
        for x in range(display_size_X//TILE_SIZE):
            display.blit(dead_cell,(x * TILE_SIZE, y * TILE_SIZE))
            map[str(x * TILE_SIZE) + "_" + str(y * TILE_SIZE)] = 0
    return map

def conways_visuals():
    """used to display the updated state of the map"""
    global map
    map = game_rules.conways_game(map,display_size_X, display_size_Y, TILE_SIZE)
    y = 0
    for y in range(display_size_Y//TILE_SIZE):
        x = 0
        for x in range(display_size_X//TILE_SIZE):
            if map[str(x * TILE_SIZE) + "_" + str(y * TILE_SIZE)] == 0:
                display.blit(dead_cell,(x * TILE_SIZE, y * TILE_SIZE))
            if map[str(x * TILE_SIZE) + "_" + str(y * TILE_SIZE)] == 1:
                display.blit(life_cell,(x * TILE_SIZE, y * TILE_SIZE))

def mouse_lock_pos():
    """used for locking in the popsition where you draw the square, so it fits perfecly"""
    pos = pygame.mouse.get_pos()
    posX, posY = pos[0], pos[1] 
    #locks in the cells
    if pos[0]%TILE_SIZE != 0:
        posX = pos[0] - pos[0]%TILE_SIZE
    if pos[1]%TILE_SIZE != 0:
        posY = pos[1] - pos[1]%TILE_SIZE
    return (posX, posY)

def display_cell(n):
    """arguments must be 0 or 1 depending on the state of the cell you want to display"""
    if n == 1:
        cell = life_cell
    else:
        cell = dead_cell
    sqpos = mouse_lock_pos()
    posX, posY = sqpos[0], sqpos[1]
    display.blit(cell,(posX , posY ))
    map[str(posX)+ "_" + str(posY)] = n


map = clear_map(map)
while True:
    for event in pygame.event.get():

        mouse = pygame.mouse.get_pressed() #devuelve tupla con valor T o F(leftclick, middleclick, rightclick)
        if mouse[0]:#checks for mouse left click and display it
            display_cell(1)
        if mouse[2]:
            display_cell(0)

        if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:#updates the state of the game by presing space                   
                    conways_visuals()
                if event.key == K_f:                   
                    clear_map(map)

        
        #exits the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0,0))#scales the images to the screen
    pygame.display.update()#updates display
    clock.tick(60)#makes it run at 60fps
