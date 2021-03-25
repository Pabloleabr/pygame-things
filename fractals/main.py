import pygame, sys, mandelbrod
from pygame import gfxdraw
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT
clock = pygame.time.Clock()

pygame.init()

WINDOW_SIZE = (500,400)
screen = pygame.display.set_mode(WINDOW_SIZE)
display_size_X = WINDOW_SIZE[0]
display_size_Y = WINDOW_SIZE[1]
display = pygame.Surface((display_size_X,display_size_Y))

Z=0
Minx=-1
Miny=-1
Maxx=2
Maxy=1
pygame.display.set_caption("fractals")


def draw_fractal():
    x = 0
    while(x < display_size_X):
        y = 0
        while(y < display_size_Y):
            xmod = (x/display_size_X)*(Maxx - Minx) - Maxx #normalizo la x e y entre -2 y 2 que seria el rango que me tendria que interesar
            ymod = (y/display_size_Y)*(Maxy - Miny) - Maxy #ya que cualquier numero mas grade se va a infinito seguro
            c = complex(xmod, ymod)
            m = mandelbrod.mandel_func(c, Z)
            color = 255 - int((m * 255) / 51)  #hace que el color tome valores del 0 al 255  
            colores = (color, color, color)
            gfxdraw.pixel(display, x, y, colores)
            y += 1
        x += 1

while True:
    
    draw_fractal()


    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:#updates the state of the game by presing space                   
                Miny += 0.1
            if event.key == K_DOWN:                   
                Maxy -= 0.1
            if event.key == K_LEFT:                   
                Maxx += 0.1
            if event.key == K_RIGHT:                   
                Minx -= 0.1



        #exits the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0,0))#scales the images to the screen
    pygame.display.update()#updates display
    clock.tick(30)#makes it run at x fps
