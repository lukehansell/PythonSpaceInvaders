from lib import relative_path
from game import Game
import pygame

#images
icon_file = relative_path(__file__, 'assets/ufo.png')
icon = pygame.image.load(icon_file)

HEIGHT = 600
WIDTH = 800

SCREENRECT = pygame.Rect(0, 0, WIDTH, HEIGHT)

# player
game = Game(WIDTH, HEIGHT)

# init
pygame.init()
pygame.font.init()

# create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# title and icon
pygame.display.set_caption('Space Invaders')
pygame.display.set_icon(icon)

# game loop
while game.is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.player.move_left()
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            if event.key == pygame.K_SPACE:
                game.create_bullet()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and game.player.is_moving_left():
                game.player.stop_moving()
            if event.key == pygame.K_RIGHT and game.player.is_moving_right():
                game.player.stop_moving()

    game.update()
    game.render(screen)

    # update everything displayed
    pygame.display.update()
