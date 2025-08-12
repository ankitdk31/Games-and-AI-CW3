import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE

def draw_grid(surface):
    """Draw grid lines for debugging"""
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(surface, (50, 50, 50), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(surface, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))

def load_image(path, scale=1):
    """Load and scale an image"""
    image = pygame.image.load(path)
    if scale != 1:
        new_size = (int(image.get_width() * scale), 
                   int(image.get_height() * scale))
        image = pygame.transform.scale(image, new_size)
    return image