import pygame

class Message(pygame.sprite.Sprite):
    def __init__(self, text, position):
        height = 600
        width = 800
        print('here', text, position)
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("Arial", 32)
        self.surface = self.font.render(text, 1, pygame.Color(255,255,255))
        self.image = pygame.Surface((width, height))
        W = self.surface.get_width()
        H = self.surface.get_height()
        self.image.blit(self.surface, [width/2 - W/2, height/2 - H/2])
