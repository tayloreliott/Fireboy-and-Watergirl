import pygame

class Platform:
    def __init__(self, x, y, num_bricks, brick_path):
        self.brick = pygame.image.load(brick_path).convert_alpha()
        self.brick_w = self.brick.get_width()
        self.brick_h = self.brick.get_height()
        self.x = x
        self.y = y
        self.num_bricks = num_bricks
        self.rect = pygame.Rect(x, y, self.brick_w * num_bricks, self.brick_h)

    def draw(self, surface):
        for i in range(self.num_bricks):
            surface.blit(self.brick, (self.x + i * self.brick_w, self.y))
