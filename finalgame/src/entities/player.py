import pygame
from settings import PLAYER_SPEED

class Player:
    def __init__(self, x, y, color, up_key, down_key, left_key, right_key):
        self.x = x
        self.y = y
        self.color = color
        self.speed = PLAYER_SPEED
        self.keys = {
            'up': up_key,
            'down': down_key,
            'left': left_key,
            'right': right_key
        }
    
    def update(self, grid):
        keys = pygame.key.get_pressed()
        
        # Calculate potential new position
        new_x, new_y = self.x, self.y
        if keys[self.keys['up']]:
            new_y -= self.speed
        if keys[self.keys['down']]:
            new_y += self.speed
        if keys[self.keys['left']]:
            new_x -= self.speed
        if keys[self.keys['right']]:
            new_x += self.speed
        
        # Convert to grid coordinates for collision check
        grid_x, grid_y = int(new_x // 20), int(new_y // 20)
        
        # Check if new position is valid (not a wall)
        if 0 <= grid_x < len(grid[0]) and 0 <= grid_y < len(grid):
            if grid[grid_y][grid_x] != 1:  # 1 represents walls
                self.x = new_x
                self.y = new_y
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 10)