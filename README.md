# Pacman AI with A* Pathfinding


## Project Statement
This project implements a multiplayer Pacman game featuring intelligent ghost AI using A* pathfinding. The implementation demonstrates core AI techniques for real-time game environments, focusing on optimal pathfinding in dynamic scenarios with multiple players.

## AI Implementation Details

### 1. [A* Pathfinding Algorithm](/src/ai/astar.py)
- **Purpose**: Optimal ghost navigation through maze
- **Key Features**:
  - Manhattan distance heuristic for grid-based movement
  - Priority queue for efficient node exploration
  - Dynamic path recalculation
- **Adapted From**: Core algorithm structure based on [Red Blob Games' A* Guide](https://www.redblobgames.com/pathfinding/a-star/)
  ```python
  # Adapted from Red Blob Games' A* implementation
  def find_path():
      """Pathfinding implementation based on public tutorial"""
  ```

### 2. [Ghost Behavior System](/src/entities/ghost.py)
- **Purpose**: Intelligent target selection and movement
- **Key Features**:
  - Nearest-player targeting using distance calculations
  - Smooth path following with collision avoidance
  - Visual path debugging
- **Original Work**: Custom implementation specific to this project

## Development Process

### Version Control
- **Commit Strategy**:
  - Daily commits with descriptive messages
  - Atomic commits focusing on single features/fixes
  - Meaningful commit comments (e.g., "feat: implement ghost targeting logic")
  
- **Major Milestones**:
  - `v0.1` - Basic A* implementation (tag: 2023-11-01)
  - `v0.5` - Functional multiplayer system (tag: 2023-11-15)
  - `v1.0` - Final release with all features (tag: 2023-12-01)


## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Start the game:
```bash
python main.py
```

**Controls**:
- Player 1: WASD keys
- Player 2: Arrow keys

## Project Structure
```
GAMES AND AI-CW3/
├── finalgame/                  # Complete game package
│   ├── assets/                 # Game assets (sprites, sounds)
│   │   ├── sprites/            # Visual assets
│   │   └── sounds/             # Audio files
│   │
│   └── src/                    # Source code
│       ├── ai/                 # AI implementations
│       │   ├── __init__.py
│       │   └── astar.py        # A* pathfinding algorithm
│       │
│       ├── entities/           # Game entities
│       │   ├── __init__.py
│       │   ├── ghost.py        # Ghost AI behavior
│       │   └── player.py       # Player controls
│       │
│       ├── utils/              # Helper functions
│       │   ├── __init__.py
│       │   ├── collision.py    # Collision detection
│       │   └── helpers.py      # Utility functions
│       │
│       ├── world/              # Game environment
│       │   ├── __init__.py
│       │   └── maze.py         # Maze generation
│       │
│       ├── main.py             # Game entry point
│       ├── requirements.txt    # Python dependencies
│       └── settings.py         # Game configuration
│
├── video/                      # Demonstration videos
│   └── gameplay.mp4            # Gameplay recording
│
├── .gitignore                  # Git exclusion rules
├── README.md                   # Project documentation

```


**Academic Integrity Notice**:  
This repository will remain private until evaluation is complete as per academic requirements. All adapted code is properly attributed both in comments and in this documentation.
