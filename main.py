import pygame
from player import Player
from walls import Walls
from hazards import Hazards
from platforms import Platform

def main():
    pygame.init()
    virtual_w, virtual_h = 1536, 1024
    display_w, display_h = 1152, 768
    screen = pygame.display.set_mode((display_w, display_h))
    virtual_surface = pygame.Surface((virtual_w, virtual_h))
    background = pygame.image.load("background.png").convert()

    walls = Walls(virtual_w, virtual_h, "brick.png")
    hazards = Hazards(virtual_w, virtual_h, walls.wall_thickness, "lava.png", "water.png")

    start_x = walls.side_thickness
    start_y = virtual_h - walls.wall_thickness - 192
    player = Player("fireboy.png", start_x, start_y, 99, 192, speed=5, jump_strength=-18, gravity=0.5)

    num_bricks = 2
    platform_w = 125 * num_bricks
    platform = Platform(
        x=virtual_w - walls.side_thickness - platform_w,
        y=virtual_h - walls.wall_thickness - 150,
        num_bricks=num_bricks,
        brick_path="brick.png"
    )

    gameClock = pygame.time.Clock()
    RUNNING = True
    while RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            player.handle_event(event)

        player.update(walls.rects + [platform.rect])
        hazards.check(player)

        virtual_surface.blit(background, (0, 0))
        walls.draw(virtual_surface)
        hazards.draw(virtual_surface)
        platform.draw(virtual_surface)
        player.draw(virtual_surface)

        scaled = pygame.transform.scale(virtual_surface, (display_w, display_h))
        screen.blit(scaled, (0, 0))
        pygame.display.flip()
        gameClock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
