import pygame
from lib import relative_path

class Player(pygame.sprite.Sprite):
    def __init__(self, bounding_box):
        image_file = relative_path(__file__, '../assets/player.png')
        image = pygame.image.load(image_file)

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = image
        self.rect = self.image.get_rect(midbottom=bounding_box.midbottom)
        self.dx = 0
        self.dy = 0
        self.x_inertia = 0
        self.y_inertia = 0
        self.bounding_box = bounding_box

    def move_left(self):
        self.x_inertia = -1

    def move_right(self):
        self.x_inertia = 1

    def stop_moving(self):
        self.x_inertia = 0

    def is_moving_left(self):
        return self.x_inertia == -1

    def is_moving_right(self):
        return self.x_inertia == 1

    def update(self):
        # increase speed left
        if self.x_inertia == 1 and self.dx <= 10:
            self.dx += 0.25

        # increase speed right
        if self.x_inertia == -1 and self.dx >= -10:
            self.dx -= 0.25

        # slow down to a stop
        if self.x_inertia == 0:
            if self.dx < 0:
                self.dx += 0.25

            if self.dx > 0:
                self.dx -= 0.25

            if self.dx > -1 and self.dx < 1:
                self.dx = 0

        self.rect.move_ip(self.dx, 0)
        if not self.bounding_box.contains(self.rect):
            self.dx = 0
            self.rect = self.rect.clamp(self.bounding_box)

