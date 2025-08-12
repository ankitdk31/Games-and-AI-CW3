import pygame
from settings import GHOST_SPEED
from src.ai.astar import AStarPathfinder

class Ghost:
    def __init__(self, x, y, color, grid):
        self.x = x
        self.y = y
        self.color = color
        self.speed = GHOST_SPEED
        self.path = []
        self.pathfinder = AStarPathfinder(grid)
    
    def update(self, target, grid):
        # Convert positions to grid coordinates
        grid_x, grid_y = int(self.x // 20), int(self.y // 20)
        target_x, target_y = int(target[0] // 20), int(target[1] // 20)
            
        # Find new path if needed
        if not self.path or (grid_x, grid_y) == self.path[0]:
            found_path = self.pathfinder.find_path((grid_x, grid_y), (target_x, target_y))
            self.path = found_path if found_path else []  # Default to empty list
        
        # Follow path
        if self.path:
            next_x, next_y = self.path[0]
            target_pixel_x = next_x * 20 + 10
            target_pixel_y = next_y * 20 + 10
            
            # Move toward next path node
            dx = target_pixel_x - self.x
            dy = target_pixel_y - self.y
            dist = (dx**2 + dy**2)**0.5
            
            if dist < 2:  # Reached node
                self.path.pop(0)
            else:
                self.x += dx / dist * self.speed
                self.y += dy / dist * self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 10)
        # Draw path visualization if path exists
        if self.path:  # Add this check
            for node in self.path:
                pygame.draw.rect(screen, (255, 0, 0, 100), (node[0]*20, node[1]*20, 20, 20), 1)