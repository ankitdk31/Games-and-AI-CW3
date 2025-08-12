Here's a comprehensive `README.md` file for your `finalgame` package:

# Pacman AI with A* Pathfinding

![Gameplay Screenshot](assets/screenshot.png)

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Controls](#controls)
- [Project Structure](#project-structure)
- [AI Implementation](#ai-implementation)
- [Development Notes](#development-notes)

## Requirements

### Python Packages
Listed in `requirements.txt`:
```
pygame==2.6.1
numpy==1.26.4
```

### System Requirements
- Python 3.10 or higher
- 500MB disk space
- Graphics card supporting OpenGL 2.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ankitdk31/Games-and-AI-CW3.git
cd GAMES-AND-AI-CW3/finalgame
```

2. Create and activate virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run

Start the game:
```bash
python -m src.main
```

Or alternatively:
```bash
cd src
python main.py
```

## Controls

| Player | Movement Keys |
|--------|---------------|
| Player 1 | W, A, S, D |
| Player 2 | Arrow Keys |

## Project Structure

```
finalgame/
├── assets/          # Game resources
│   ├── sprites/     # Image files
│   └── sounds/      # Audio files
│
├── src/             # Source code
│   ├── ai/          # Pathfinding algorithms
│   ├── entities/    # Game objects
│   ├── utils/       # Helper functions
│   └── world/       # Maze generation
│
├── main.py      # Entry point
├── requirements.txt # Dependencies
└── settings.py      # Configuration
```

## AI Implementation

### Key AI Files:
1. [`src/ai/astar.py`](src/ai/astar.py) - A* pathfinding implementation
2. [`src/entities/ghost.py`](src/entities/ghost.py) - Ghost behavior and movement

### Features:
- Optimal pathfinding using Manhattan distance heuristic
- Dynamic target selection
- Smooth path following

## Development Notes

### Version Control
- Commit daily with descriptive messages
- Tag major milestones:
  ```bash
  git tag -a v1.0 -m "Stable release"
  ```