from settings import GRID_SIZE

def check_collision(obj1, obj2, threshold=10):
    """Check distance-based collision between two objects"""
    dx = obj1.x - obj2.x
    dy = obj1.y - obj2.y
    distance = (dx**2 + dy**2)**0.5
    return distance < threshold

def grid_to_pixel(grid_pos):
    """Convert grid coordinates to pixel coordinates"""
    return (grid_pos[0] * GRID_SIZE + GRID_SIZE//2, 
            grid_pos[1] * GRID_SIZE + GRID_SIZE//2)