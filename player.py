import pygame

class Player:
    def __init__(self, image_path, x, y, width, height, speed, jump_strength, gravity):
        src = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(src, (width, height))
        self.width = width
        self.height = height
        self.start_x = x
        self.start_y = y
        self.position = [x, y]
        self.velocity = [0, 0]
        self.speed = speed
        self.jump_strength = jump_strength
        self.gravity = gravity
        self.on_ground = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity[0] = -self.speed
            elif event.key == pygame.K_RIGHT:
                self.velocity[0] = self.speed
            elif event.key == pygame.K_UP and self.on_ground:
                self.velocity[1] = self.jump_strength
                self.on_ground = False
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.velocity[0] = 0

    def update(self, walls):
        self.velocity[1] += self.gravity
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.on_ground = False
        char_rect = self.get_rect()
        for wall in walls:
            if char_rect.colliderect(wall):
                overlap = char_rect.clip(wall)
                if overlap.width < overlap.height:
                    if char_rect.centerx < wall.centerx:
                        self.position[0] -= overlap.width
                    else:
                        self.position[0] += overlap.width
                else:
                    if char_rect.centery < wall.centery:
                        self.position[1] -= overlap.height
                    else:
                        self.position[1] += overlap.height
                    if self.velocity[1] > 0:
                        self.on_ground = True
                    self.velocity[1] = 0
                char_rect.topleft = (self.position[0], self.position[1])

    def reset(self):
        self.position = [self.start_x, self.start_y]
        self.velocity = [0, 0]
        self.on_ground = False

    def get_rect(self):
        return pygame.Rect(self.position[0], self.position[1], self.width, self.height)

    def draw(self, surface):
        surface.blit(self.image, (self.position[0], self.position[1]))
