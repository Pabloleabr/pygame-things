import pygame

class text_box():
    def __init__(self, window, color, x, y, width, height, text="",B_effect = None):
        self.window = window
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.B_effect = B_effect

    def draw(self):
        "draws the buttom when its called"
        pygame.draw.rect(self.window, (0,0,0), (self.x - 2 ,self.y - 2, self.width + 4, self.height + 4), 0)#outline
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height), 0)#square

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            self.window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    
    def mouse_over(self, pos):
        "checks if the mouse positions and the bottons aline to return true, needs the mouse possitions as an argument"
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

    def call_effect(self):
        return self.B_effect


