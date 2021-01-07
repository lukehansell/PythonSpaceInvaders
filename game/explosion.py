from math import floor
import pygame
from lib import relative_path

class Explosion(pygame.sprite.Sprite):
    frames = 16
    animcycle = 3

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self, self.containers)
        image_file = relative_path(__file__, '../assets/explosion.png')
        self.spritesheet = pygame.image.load(image_file).convert_alpha()

        self.frame = 0
        self.image = self.get_image(self.frame)

        self.rect = self.image.get_rect(center=position)

    def get_image(self, index):
        x_offset = (index % 4) * 64
        y_offset = floor(index / 4) * 64
        print(index, (floor(index / 4),index % 4))
        image = pygame.Surface((64, 64)).convert_alpha()

        image.blit(self.spritesheet, (0, 0), (x_offset, y_offset, x_offset+64, y_offset+64))

        return image

    def update(self):
        self.image = self.get_image(self.frame)

        self.frame += 1
        if (self.frame >= self.frames):
            self.kill()
