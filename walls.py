import pygame

class Walls:
    def __init__(self, virtual_w, virtual_h, brick_path):
        self.virtual_w = virtual_w
        self.virtual_h = virtual_h
        self.brick = pygame.image.load(brick_path).convert_alpha()
        self.brick_w = self.brick.get_width()
        self.brick_h = self.brick.get_height()
        self.brick_rotated = pygame.transform.rotate(self.brick, 90)
        self.wall_thickness = self.brick_h
        self.side_thickness = self.brick_h
        self.rects = [
            pygame.Rect(0, 0, virtual_w, self.wall_thickness),
            pygame.Rect(0, virtual_h - self.wall_thickness, virtual_w, self.wall_thickness),
            pygame.Rect(0, 0, self.side_thickness, virtual_h),
            pygame.Rect(virtual_w - self.side_thickness, 0, self.side_thickness, virtual_h),
        ]

    def draw(self, surface):
        for wall_x in [0, self.virtual_w - self.side_thickness]:
            y = 0
            while y < self.virtual_h:
                surface.blit(self.brick_rotated, (wall_x, y))
                y += self.brick_rotated.get_height()

        for wall_y in [0, self.virtual_h - self.wall_thickness]:
            x = self.side_thickness
            while x < self.virtual_w - self.side_thickness:
                surface.blit(self.brick, (x, wall_y))
                x += self.brick_w
