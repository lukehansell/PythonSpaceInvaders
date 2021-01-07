import pygame
from lib import relative_path
from game.player import Player
from game.enemy import Enemy, CHANGE_DIRECTION_EVENT
from game.bullet import Bullet
from game.message import Message
from game.explosion import Explosion

HEIGHT = 600
WIDTH = 800

SCREENRECT = pygame.Rect(0, 0, WIDTH, HEIGHT)

def main():
    # init
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()

    #images
    icon_file = relative_path(__file__, 'assets/ufo.png')
    background_file = relative_path(__file__, 'assets/background.jpg')

    icon_image = pygame.image.load(icon_file)
    background_image = pygame.image.load(background_file)

    # create screen
    screen = pygame.display.set_mode(SCREENRECT.size)

    # title and icon
    pygame.display.set_caption('Space Invaders')
    pygame.display.set_icon(icon_image)

    background = pygame.Surface(screen.get_size()).convert()
    background.fill((0,0,0))
    background.blit(background_image, (0, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    # set up containers for collision detection etc
    Player.containers = all
    Enemy.containers = enemies, all
    Bullet.containers = bullets, all
    Message.containers = all
    Explosion.containers = all

    # generate starting game objects
    player = Player(SCREENRECT)

    for x in range(10):
        for y in range(3):
            Enemy((42*x, 42*y), SCREENRECT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_SPACE:
                    if len(bullets) < 10:
                        Bullet(player.rect.midtop)
                if event.key == pygame.K_e:
                    Explosion(SCREENRECT.center)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.is_moving_left():
                    player.stop_moving()
                if event.key == pygame.K_RIGHT and player.is_moving_right():
                    player.stop_moving()
            if event.type == CHANGE_DIRECTION_EVENT:
                for enemy in enemies:
                    enemy.change_direction()

        if player.alive() and len(enemies) > 0:
            # collision detection
            for alien in pygame.sprite.spritecollide(player, enemies, True):
                Explosion(alien.rect.center)
                Explosion(player.rect.center)
                player.kill()

            for enemy in pygame.sprite.groupcollide(bullets, enemies, True, True):
                Explosion(enemy.rect.center)

            # updating game objects

            all.clear(screen, background)
            all.update()

        elif player.alive() and len(enemies) == 0:
            Message("You win", SCREENRECT.center)
        elif not player.alive():
            Message("You lose", SCREENRECT.center)

        dirty = all.draw(screen)
        pygame.display.update(dirty)

        clock.tick(40)

if __name__ == "__main__":
    main()
