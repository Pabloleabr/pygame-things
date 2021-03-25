import pygame, sys
from Data import pokemons, text_boxes 
from pygame import K_SPACE

clock = pygame.time.Clock()

pygame.init()

WINDOW_SIZE = (960,640)
screen = pygame.display.set_mode(WINDOW_SIZE)
display_size_X = 960
display_size_Y = 640
display = pygame.Surface((display_size_X,display_size_Y))

icon = pygame.image.load("Data/imgs/icon.png")

pygame.display.set_caption("pokemon test")#title
pygame.display.set_icon(icon)

moves_textbox = text_boxes.text_box(display, (255,255,255), 8, 440, display_size_X-16, 192 )

charmander = pokemons.pokemon("charmander", 80, 15, 9, 11, ["scratch", "tail atack", "fire ball", "rage"])
squiertail = pokemons.pokemon("squiertail", 86, 13, 13, 8, ["scratch", "tail atack", "epic punch", "ironskin"])

def moves_boxs(pokemon):
    """takes the pokemon has an argument and draws the boxes with the moves the pokemon has with their effects"""
    pass

while True:
    display.fill((250, 230, 230))
    moves_textbox.draw()
    for event in pygame.event.get():

        mouse = pygame.mouse.get_pressed() #devuelve tupla con valor T o F(leftclick, middleclick, rightclick)
        if mouse[0]:#checks for mouse left click and display it
            pass
        if mouse[2]:
            pass

        if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:#updates the state of the game by presing space                   
                    pass

        
        #exits the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0,0))#scales the images to the screen
    pygame.display.update()#updates display
    clock.tick(60)#makes it run at 60fps
