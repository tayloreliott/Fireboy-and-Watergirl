import pygame

class Hazards:
    def __init__(self, virtual_w, virtual_h, wall_thickness, lava_path, water_path):
        self.lava = pygame.image.load(lava_path).convert_alpha()
        self.water = pygame.image.load(water_path).convert_alpha()
        self.lava_x = virtual_w // 4 - self.lava.get_width() // 2
        self.water_x = virtual_w // 2 - self.water.get_width() // 2
        self.pool_y = virtual_h - wall_thickness - self.lava.get_height() // 2
        self.water_rect = pygame.Rect(self.water_x, self.pool_y, self.water.get_width(), self.water.get_height())

    def check(self, player):
        if player.get_rect().colliderect(self.water_rect):
            player.reset()

    def draw(self, surface):
        surface.blit(self.lava, (self.lava_x, self.pool_y))
        surface.blit(self.water, (self.water_x, self.pool_y))
