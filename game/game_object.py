from game.point import Point
from lib import collision_detected

class GameObject:
    def __init__(self, x, y, height, width, image):
        self.position = Point(x, y)
        self.height = height
        self.width = width
        self.image = image
        self.is_active = True

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, (self.position.x, self.position.y))

    def get_bottom_right_point(self):
        return Point(self.position.x + self.width, self.position.y + self.height)

    def is_colliding(self, other_object):
        return collision_detected(
            self.position,
            self.get_bottom_right_point(),
            other_object.position,
            other_object.get_bottom_right_point()
        )

    def is_colliding_with_any(self, other_objects):
        for other in other_objects:
            if self.is_colliding(other):
                return True
        return False
