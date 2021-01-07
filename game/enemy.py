import pygame
from lib import relative_path

CHANGE_DIRECTION_EVENT = pygame.event.custom_type()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, starting_position, bounding_box):

        image_file = relative_path(__file__, '../assets/alien.png')

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image_file)
        self.dx = 2
        self.rect = self.image.get_rect(topleft=starting_position)
        self.bounding_box = bounding_box

    def change_direction(self):
        self.dx = self.dx * -1
        self.rect.top += 32

    def update(self):
        self.rect.move_ip(self.dx, 0)

        if not self.bounding_box.contains(self.rect):
            if not pygame.event.peek(CHANGE_DIRECTION_EVENT):
                pygame.event.post(pygame.event.Event(CHANGE_DIRECTION_EVENT))
