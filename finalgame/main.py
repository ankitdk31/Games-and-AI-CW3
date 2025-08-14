import pygame
import sys
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE,
    BLACK, WHITE, BLUE, RED, GREEN, YELLOW,
    PELLET_SCORE, PELLET_RADIUS, COLLISION_RADIUS, FPS
)
from src.entities.player import Player
from src.entities.ghost import Ghost
from src.world.maze import generate_maze

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pacman with A* Pathfinding - Multiplayer")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Arial', 32)
    
    # Generate game world
    grid = generate_maze(20, 20)
    pellets = [
        (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2)
        for row in range(len(grid))
        for col in range(len(grid[0]))
        if grid[row][col] == 2
    ]
    
    # Create players
    player1 = Player(
        GRID_SIZE * 1 + GRID_SIZE // 2,
        GRID_SIZE * 1 + GRID_SIZE // 2,
        BLUE,
        pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d
    )
    player2 = Player(
        GRID_SIZE * (len(grid[0]) - 2) + GRID_SIZE // 2,
        GRID_SIZE * (len(grid) - 2) + GRID_SIZE // 2,
        GREEN,
        pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT
    )
    
    # Create ghosts
    ghosts = [
        Ghost(GRID_SIZE * 5 + GRID_SIZE // 2, GRID_SIZE * 5 + GRID_SIZE // 2, RED, grid),
        Ghost(
            GRID_SIZE * (len(grid[0]) - 6) + GRID_SIZE // 2,
            GRID_SIZE * (len(grid) - 6) + GRID_SIZE // 2,
            YELLOW,
            grid
        )
    ]
    
    # Game state
    scores = {1: 0, 2: 0}
    game_over = False
    running = True
    game_started = False  # Track game start state
    
    while running:
        keys = pygame.key.get_pressed()  # Get current key states
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Start game on any key press
            if not game_started and event.type == pygame.KEYDOWN:
                game_started = True
            
            if game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart
                    return main()
                if event.key == pygame.K_q:  # Quit
                    running = False
        
        # Draw background
        screen.fill(BLACK)
        
        # Draw maze walls
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    pygame.draw.rect(
                        screen, BLUE,
                        (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                    )
        
        # Draw pellets
        for px, py in pellets:
            pygame.draw.circle(screen, WHITE, (int(px), int(py)), PELLET_RADIUS)
        
        if not game_started:
            # Show start screen
            start_text = font.render("Press ANY KEY to Start", True, WHITE)
            controls_text = font.render(
                "Player 1: WASD  |  Player 2: Arrow Keys", 
                True, WHITE
            )
            screen.blit(
                start_text,
                (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50)
            )
            screen.blit(
                controls_text,
                (SCREEN_WIDTH // 2 - controls_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20)
            )
        else:
            if not game_over:
                # Update players (move only if keys are pressed)
                player1.update(keys, grid)
                player2.update(keys, grid)
                
                # Update ghosts
                for ghost in ghosts:
                    dist_to_p1 = ((ghost.x - player1.x) ** 2 + (ghost.y - player1.y) ** 2) ** 0.5
                    dist_to_p2 = ((ghost.x - player2.x) ** 2 + (ghost.y - player2.y) ** 2) ** 0.5
                    target = player1 if dist_to_p1 < dist_to_p2 else player2
                    ghost.update((target.x, target.y), grid)
                
                # Check pellet collisions
                pellets_to_remove = []
                for i, (px, py) in enumerate(pellets):
                    for player in [player1, player2]:
                        if ((player.x - px) ** 2 + (player.y - py) ** 2) ** 0.5 < PELLET_RADIUS * 2:
                            pellets_to_remove.append(i)
                            if player == player1:
                                scores[1] += PELLET_SCORE
                            else:
                                scores[2] += PELLET_SCORE
                            break
                
                # Remove collected pellets
                for i in sorted(pellets_to_remove, reverse=True):
                    if i < len(pellets):
                        pellets.pop(i)
                
                # Check ghost collisions
                for ghost in ghosts:
                    for player in [player1, player2]:
                        if ((ghost.x - player.x) ** 2 + (ghost.y - player.y) ** 2) ** 0.5 < COLLISION_RADIUS:
                            game_over = True
            
            # Draw players and ghosts
            player1.draw(screen)
            player2.draw(screen)
            for ghost in ghosts:
                ghost.draw(screen)
            
            # Draw scores
            score_text = font.render(
                f"Player 1: {scores[1]}  Player 2: {scores[2]}",
                True, WHITE
            )
            screen.blit(score_text, (10, 10))
            
            # Game over message
            if game_over:
                game_over_text = font.render(
                    "GAME OVER - Press R to restart, Q to quit",
                    True, RED
                )
                screen.blit(
                    game_over_text,
                    (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2)
                )
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
