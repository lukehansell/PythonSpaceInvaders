from lib import relative_path
import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        image_file = relative_path(__file__, '../assets/lazer.png')
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, -3)
        if self.rect.bottom <= 0:
            self.kill()
