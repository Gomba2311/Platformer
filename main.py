import pygame
from settings import screen_width, screen_height, level_map
from level import Level

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

bg_surf = pygame.image.load("img/BG.png")
bg_rect = bg_surf.get_rect(bottomleft=(0, screen_height))

level = Level(level_map, screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_surf, bg_rect)
    level.run()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
