import pygame, sys, mandelbrod
from pygame import gfxdraw


tamano = (960,640)
screen = pygame.display.set_mode(tamano)
display_size_X = tamano[0]
display_size_Y = tamano[1]
display = pygame.Surface((display_size_X,display_size_Y))

def draw_fractal():
    x = 0
    print("i'am working")
    while(x < display_size_X):
        y = 0
        while(y < display_size_Y):
            xmod = (x/display_size_X)*(3) - 2 #normalizo la x e y entre -2 y 2 que seria el rango que me tendria que interesar
            ymod = (y/display_size_Y)*(2) - 1 #ya que cualquier numero mas grade se va a infinito seguro
            c = complex(xmod, ymod)
            m = mandelbrod.mandel_func(c)
            color = 255 - int((m * 255) / 51)  #hace que el color tome valores del 0 al 255  
            color1 = (255 - int((m * 255) / 51))//2
            color2 = (255 - int((m * 255) / 51))//4
            colores = (color, color1, color2)
            gfxdraw.pixel(display, x, y, colores)
            y += 1
        x += 1
        
pygame.quit()
draw_fractal()


pygame.image.save(display, "imgs/fractalMandelbrod_orange.png")
print("i'm done sir")