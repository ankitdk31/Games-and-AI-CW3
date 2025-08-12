import random
from settings import GRID_SIZE

def generate_maze(width, height, wall_density=0.2):
    """Generate a random maze grid"""
    grid = [[2 for _ in range(width)] for _ in range(height)]  # 2 = pellets
    
    # Add walls (1) with some density
    for row in range(height):
        for col in range(width):
            if random.random() < wall_density:
                grid[row][col] = 1  # Wall
    
    # Ensure start and end positions are clear
    grid[1][1] = 2  # Player 1 start
    grid[height-2][width-2] = 2  # Player 2 start
    
    return grid