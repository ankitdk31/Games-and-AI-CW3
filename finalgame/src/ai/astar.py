import heapq
from collections import defaultdict

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

class AStarPathfinder:
    def __init__(self, grid):
        self.grid = grid
    
    def get_neighbors(self, node):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            x, y = node[0] + dx, node[1] + dy
            if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
                if self.grid[x][y] != 1:  # Not a wall
                    neighbors.append((x, y))
        return neighbors
        
    def find_path(self, start, target):
        # Early return if start or target is invalid
        if (not (0 <= start[0] < len(self.grid))) or \
        (not (0 <= start[1] < len(self.grid[0]))) or \
        self.grid[start[0]][start[1]] == 1:
            print(f"Invalid start position: {start}")
            return None
        
        if (not (0 <= target[0] < len(self.grid))) or \
        (not (0 <= target[1] < len(self.grid[0]))) or \
        self.grid[target[0]][target[1]] == 1:
            print(f"Invalid target position: {target}")
            return None
        
        # Rest of A* implementation...
        open_set = PriorityQueue()
        open_set.put(start, 0)
        came_from = {}
        g_score = defaultdict(lambda: float('inf'))
        g_score[start] = 0
        f_score = defaultdict(lambda: float('inf'))
        f_score[start] = manhattan_distance(start, target)
        
        while not open_set.empty():
            current = open_set.get()[1]
            
            if current == target:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.reverse()
                return path
            
            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1
                
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + manhattan_distance(neighbor, target)
                    open_set.put(neighbor, f_score[neighbor])
        
        return None  # No path found