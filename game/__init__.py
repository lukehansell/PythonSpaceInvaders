import pygame
from lib import relative_path, collision_detected
from game.player import Player
from game.enemy import Enemy
from game.bullet import Bullet
from game.point import Point

class Game:
    def __init__(self, width, height):
        background_file = relative_path(__file__, '../assets/background.jpg')
        self.background = pygame.image.load(background_file)

        self.is_running = True
        self.finished = False
        self.player_wins = False
        self.player = self.init_player(width, height)
        self.width = width
        self.height = height
        self.enemies = self.init_enemies()
        self.bullets = []

    def init_enemies(self):
        enemies = []
        for y_offset in range(3):
            for x_offset in range(10):
                enemies.append(Enemy(42 * x_offset, 42 * y_offset))

        return enemies

    def init_player(self, width, height):
        player_width = 64
        player_height = 64
        position_x = (width/2) - (player_width/2)
        position_y = height - (player_height * 1.5)
        return Player(position_x, position_y, 0, width-player_width, player_height, player_width)

    def create_bullet(self):
        if len(self.bullets) == 10:
            return
        bullet_x = self.player.position.x + (self.player.width / 2)
        self.bullets.append(Bullet(bullet_x, self.player.position.y))

    def update(self):

        # "end of game" logic
        if self.player.is_colliding_with_any(self.enemies):
            self.finished = True
            return

        if len(self.enemies) == 0:
            self.finished = True
            self.player_wins = True
            return

        # enemy movement logic
        enemies_should_change_direction = next((x for x in self.enemies if x.position.x + 32 >= 800 or x.position.x < 0 ), None)

        # cleaning up old objects
        self.bullets = list(filter(lambda bullet: not bullet.is_off_screen(), self.bullets))

        # collision detection (need to create new lists and reassign to check collisions in multiple directions)
        filtered_bullets = list(filter(lambda bullet: not bullet.is_colliding_with_any(self.enemies), self.bullets))
        filtered_enemies = list(filter(lambda enemy: not enemy.is_colliding_with_any(self.bullets), self.enemies))
        self.enemies = filtered_enemies
        self.bullets = filtered_bullets

        # updating game objects
        for enemy in self.enemies:
            if enemies_should_change_direction is not None:
                enemy.change_direction()
            enemy.update()

        for bullet in self.bullets:
            bullet.update()

        self.player.update()

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.background, (0, 0))

        for enemy in self.enemies:
            enemy.render(screen)

        for bullet in self.bullets:
            bullet.render(screen)

        self.player.render(screen)

        if self.finished and self.player_wins:
            font = pygame.font.SysFont('Arial', 30)
            text_surface = font.render('You Win!', False, (255, 255, 255))
            screen.blit(text_surface, (self.width / 2, self.height / 2))

        if self.finished and not self.player_wins:
            font = pygame.font.SysFont('Arial', 30)
            text_surface = font.render('You Lose!', False, (150, 0, 0))
            screen.blit(text_surface, (self.width / 2, self.height / 2))

    def quit(self):
        self.is_running = False