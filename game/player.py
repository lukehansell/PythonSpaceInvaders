from game.game_object import GameObject
from lib import relative_path
import pygame

class Player(GameObject):
    def __init__(self, position_x, position_y, x_boundary_min, x_boundary_max, height, width):
        image_file = relative_path(__file__, '../assets/player.png')
        image = pygame.image.load(image_file)

        super().__init__(position_x, position_y, height, width, image)

        self.dx = 0
        self.dy = 0
        self.x_inertia = 0
        self.y_inertia = 0
        self.x_boundary_min = x_boundary_min
        self.x_boundary_max = x_boundary_max

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
        block_left = self.position.x <= self.x_boundary_min
        block_right = self.position.x >= self.x_boundary_max


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

        # prevent player from flying off of screen
        if block_left:
            self.position.x = self.x_boundary_min

        if block_right and self.dx > 0:
            self.position.x = self.x_boundary_max

        self.position.x += self.dx
