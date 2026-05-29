# Maze Solver Visualizer (Python)

An interactive desktop application for exploring classic pathfinding algorithms on a 2D grid. Draw walls, place start and end points, generate mazes, and watch **BFS**, **DFS**, **A\***, and **Dijkstra** search the grid step by step with live statistics and animation.

Built with **Python** and **Tkinter** — no third-party packages required.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Features

- **Four pathfinding algorithms** — compare breadth-first, depth-first, A*, and Dijkstra on the same maze
- **Step-by-step visualization** — visited cells and final path animate at an adjustable speed
- **Open / closed set display** — A* and Dijkstra highlight frontier and explored nodes after the run
- **Interactive grid editing** — paint walls and move start/end with the mouse
- **Maze generation** — random wall placement or perfect mazes via **Wilson's algorithm**
- **Configurable grid** — resize from 10×10 to 50×50
- **Live metrics** — nodes visited, path length, path cost, and search time in the status bar
- **Dark-themed UI** — responsive canvas that scales with the window

---

## Demo

> Add a screenshot or GIF here after uploading to GitHub, for example:
>
> `![Maze Solver Visualizer](docs/demo.gif)`

---

## Requirements

- **Python 3.8+** (recommended)
- **Tkinter** — included with most standard Python installs on Windows and macOS

On **Linux**, if Tkinter is missing, install it for your distribution, for example:

```bash
# Debian / Ubuntu
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/Maze_Solver_Visualizer_PYTHON.git
   cd Maze_Solver_Visualizer_PYTHON
   ```

2. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   There are no external Python packages. See `requirements.txt` for details.

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the application from the project root:

```bash
python main.py
```

### Toolbar

| Control | Description |
|--------|-------------|
| **Algorithm** | Choose BFS, DFS, A*, or Dijkstra |
| **Maze Generator** | Random (30% walls) or Wilson's Algorithm (perfect maze) |
| **Start Visualization** | Run the selected algorithm and animate the result |
| **Clear Grid** | Remove all walls and reset start/end to corners |
| **Reset Path** | Clear visited/path highlighting only |
| **Generate Maze** | Build a new maze with the selected generator |
| **Speed** | Animation speed (1 = slow, 100 = fast) |
| **Grid Size** | Change maze dimensions (10–50) |

### Mouse controls

| Action | Effect |
|--------|--------|
| **Left click** | Toggle wall on an empty cell; remove wall on a wall cell |
| **Left drag** | Draw walls while dragging |
| **Right click** | Cycle cell to **start** (green); click start again to set **end** (red); click end to clear |

Default start is the **top-left** corner; default end is the **bottom-right**.

---

## Algorithms

| Algorithm | Strategy | Notes in this app |
|-----------|----------|-------------------|
| **BFS** | Layer-by-layer expansion | Shortest path in unweighted grids; visits shown in expansion order |
| **DFS** | Depth-first stack | May not find the shortest path; useful to compare exploration shape |
| **A\*** | Best-first with heuristic | Manhattan distance heuristic; open/closed sets visualized |
| **Dijkstra** | Uniform-cost search | Treats each step with equal cost; open/closed sets visualized |

All algorithms use **4-directional** movement (up, down, left, right). Walls are impassable.

---

## Color legend

| Color | Meaning |
|-------|---------|
| Green | Start |
| Red | End |
| Dark gray / black | Wall |
| Light gray | Empty cell |
| Blue shades | Visited / open set / closed set |
| Yellow | Final path |

---

## Project structure

```
Maze_Solver_Visualizer_PYTHON/
├── main.py                      # Application entry point
├── requirements.txt
├── controller/
│   ├── maze_controller.py       # Grid input, algorithm runs, maze generation
│   └── animation_controller.py  # Step-by-step visualization timing
├── model/
│   ├── grid.py                  # Grid state and neighbors
│   ├── cell.py / cell_type.py   # Cell model and costs
│   ├── algorithms/
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   ├── astar.py
│   │   └── dijkstra.py
│   └── maze/
│       ├── maze_generator.py
│       └── wilsons_algorithm.py
├── ui/
│   ├── toolbar.py
│   ├── status_bar.py
│   └── grid_renderer.py
└── utils/
    └── pair.py                  # (row, col) coordinate helper
```

The codebase follows a simple **MVC-style** layout: `model` holds data and algorithms, `ui` handles rendering and widgets, and `controller` wires user actions to logic.

---

## How it works

1. You define the maze (walls, start, end) or generate one.
2. On **Start Visualization**, the chosen algorithm runs on a **background thread** so the UI stays responsive.
3. When the search finishes, the **AnimationController** replays visited cells, then draws the path.
4. The status bar reports **nodes visited**, **path length**, **path cost**, and **elapsed time**.

Path cost sums per-cell movement costs from `CellType` (walls use a large sentinel cost and are never traversed).

---

## Educational context

This project is suited for **AI / algorithms courses** and self-study: compare how each search strategy expands through the grid, observe trade-offs between optimality and exploration, and experiment with maze density and size.

---

## Contributing

Issues and pull requests are welcome. If you extend the project, consider:

- Additional algorithms (e.g. Greedy Best-First, Bidirectional Search)
- Diagonal movement or weighted terrain
- Export/import of maze layouts
- Screenshots in this README

---

## License

This project is open source. Add a `LICENSE` file (e.g. MIT) when publishing if you have not already.

---

## Acknowledgments

- **Wilson's algorithm** for uniform random maze generation
- Classic pathfinding references: Russell & Norvig, CLRS, and standard competitive-programming treatments of BFS/DFS/A*/Dijkstra
