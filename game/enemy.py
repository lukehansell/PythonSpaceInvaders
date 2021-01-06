from game.game_object import GameObject
from lib import relative_path
import pygame

class Enemy(GameObject):
    def __init__(self, position_x, position_y):

        image_file = relative_path(__file__, '../assets/alien.png')
        image = pygame.image.load(image_file)

        super().__init__(position_x, position_y, 32, 32, image)

        self.dx = 1

    def change_direction(self):
        self.dx = self.dx * -1
        self.position.y += 32

    def update(self):
        self.position.x += self.dx
