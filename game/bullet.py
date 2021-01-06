from game.game_object import GameObject
from lib import relative_path
import pygame

class Bullet(GameObject):
    def __init__(self, position_x, position_y):
        image_file = relative_path(__file__, '../assets/lazer.png')
        image = pygame.image.load(image_file)

        super().__init__(position_x, position_y, 10, 3, image)

    def update(self):
        self.position.y -= 1

    def is_off_screen(self):
        return self.position.y + self.height <= 0