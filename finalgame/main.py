import pygame
import sys
from settings import *
from src.entities.player import Player
from src.entities.ghost import Ghost
from src.world.maze import generate_maze

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pacman with A* Pathfinding")
    clock = pygame.time.Clock()
    
    # Generate game world
    grid = generate_maze(20, 20)
    pellets = [(col * 20 + 10, row * 20 + 10) 
              for row in range(len(grid)) 
              for col in range(len(grid[0])) 
              if grid[row][col] == 2]
    
    # Create players
    player1 = Player(50, 50, BLUE, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    player2 = Player(SCREEN_WIDTH-50, SCREEN_HEIGHT-50, GREEN, 
                    pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    
    # Create ghosts
    ghosts = [
        Ghost(200, 200, RED, grid),
        Ghost(600, 400, YELLOW, grid)
    ]
    
    # Game state
    scores = {1: 0, 2: 0}
    running = True
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update players
        player1.update(grid)
        player2.update(grid)
        
        # Update ghosts (chase closest player)
        for ghost in ghosts:
            # Find closest player
            dist1 = ((ghost.x - player1.x)**2 + (ghost.y - player1.y)**2)**0.5
            dist2 = ((ghost.x - player2.x)**2 + (ghost.y - player2.y)**2)**0.5
            target = player1 if dist1 < dist2 else player2
            ghost.update((target.x, target.y), grid)

        # Check pellet collisions
        pellets_to_remove = []
        for i, (pellet_x, pellet_y) in enumerate(pellets):
            for player in [player1, player2]:
                if ((player.x - pellet_x)**2 + (player.y - pellet_y)**2)**0.5 < 10:  # Collision radius
                    pellets_to_remove.append(i)
                    if player == player1:
                        scores[1] += PELLET_SCORE
                    else:
                        scores[2] += PELLET_SCORE
                    break
        
        # Remove collected pellets (reverse order to avoid index issues)
        for i in sorted(pellets_to_remove, reverse=True):
            if i < len(pellets):
                pellets.pop(i)

        # Check ghost collisions
        game_over = False
        for ghost in ghosts:
            for player_num, player in enumerate([player1, player2], start=1):
                if ((ghost.x - player.x)**2 + (ghost.y - player.y)**2)**0.5 < 15:  # Collision radius
                    print(f"Player {player_num} caught by ghost!")
                    game_over = True
        
        if game_over:
            print("Game Over! Final Scores:")
            print(f"Player 1: {scores[1]}")
            print(f"Player 2: {scores[2]}")
            running = False

        # Draw everything
        screen.fill(BLACK)
        
        # Draw maze
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:  # Wall
                    pygame.draw.rect(screen, BLUE, 
                                   (col*GRID_SIZE, row*GRID_SIZE, 
                                    GRID_SIZE, GRID_SIZE))
        
        # Draw pellets
        for pellet_x, pellet_y in pellets:
            pygame.draw.circle(screen, WHITE, (pellet_x, pellet_y), 3)


        # Draw players and ghosts
        player1.draw(screen)
        player2.draw(screen)
        for ghost in ghosts:
            ghost.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()