import pygame
from settings import PLAYER_SPEED, GRID_SIZE, COLLISION_RADIUS, WHITE

class Player:
    def __init__(self, x, y, color, up_key, down_key, left_key, right_key):
        self.x = x
        self.y = y
        self.color = color
        self.speed = PLAYER_SPEED
        self.radius = COLLISION_RADIUS
        self.keys = {
            'up': up_key,
            'down': down_key,
            'left': left_key,
            'right': right_key
        }
        self.direction = [0, 0]  # Track current movement direction
    
    def update(self, keys, grid):
        """Update player position with improved movement and collision"""
        # Reset movement direction
        self.direction = [0, 0]
        
        # Track if a key was pressed
        moved = False
        
        # Calculate movement vector based on key presses
        if keys[self.keys['up']]:
            self.direction[1] -= 1
            moved = True
        if keys[self.keys['down']]:
            self.direction[1] += 1
            moved = True
        if keys[self.keys['left']]:
            self.direction[0] -= 1
            moved = True
        if keys[self.keys['right']]:
            self.direction[0] += 1
            moved = True
        
        # If no movement key was pressed, stop here
        if not moved:
            return
        
        # Normalize diagonal movement
        if self.direction[0] != 0 and self.direction[1] != 0:
            self.direction[0] *= 0.7071  # 1/sqrt(2)
            self.direction[1] *= 0.7071
        
        # Calculate new position
        new_x = self.x + self.direction[0] * self.speed
        new_y = self.y + self.direction[1] * self.speed
        
        # Grid-based collision checking (4-point check)
        collision = False
        
        # Check four corners of player circle
        check_positions = [
            (new_x - self.radius, new_y - self.radius),  # Top-left
            (new_x + self.radius, new_y - self.radius),  # Top-right
            (new_x - self.radius, new_y + self.radius),  # Bottom-left
            (new_x + self.radius, new_y + self.radius)   # Bottom-right
        ]
        
        for px, py in check_positions:
            gx = int(px // GRID_SIZE)
            gy = int(py // GRID_SIZE)
            if (0 <= gx < len(grid[0]) and (0 <= gy < len(grid))):
                if grid[gy][gx] == 1:  # Wall collision
                    collision = True
                    break
        
        # Update position if no collision
        if not collision:
            self.x = new_x
            self.y = new_y
            
            # Keep player within screen bounds
            self.x = max(self.radius, min(self.x, len(grid[0]) * GRID_SIZE - self.radius))
            self.y = max(self.radius, min(self.y, len(grid) * GRID_SIZE - self.radius))
    
    def draw(self, screen):
        """Draw player with directional indicator"""
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw direction indicator if moving
        if self.direction != [0, 0]:
            end_x = self.x + self.direction[0] * self.radius
            end_y = self.y + self.direction[1] * self.radius
            pygame.draw.line(
                screen, WHITE,
                (self.x, self.y),
                (end_x, end_y),
                3
            )
