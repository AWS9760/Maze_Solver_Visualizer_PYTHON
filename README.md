# 🧩 Maze Solver Visualizer (Python)

An interactive **pathfinding and maze visualization tool** built with **Python** and **Tkinter**.
Create mazes, place start and end nodes, and watch popular search algorithms explore the grid step-by-step with smooth animations and live statistics.

> 🚀 Built for learning, experimentation, and visualizing how pathfinding algorithms work in real time.

---

## ✨ Features

### 🧠 Pathfinding Algorithms

Visualize and compare:

* **Breadth-First Search (BFS)**
* **Depth-First Search (DFS)**
* **A*** (A-Star Search)
* **Dijkstra’s Algorithm**

---

### 🧱 Maze Generation

Generate complex mazes instantly using:

* **Random Maze Generation**
* **Wilson’s Algorithm** (perfect maze generation)

---

### 🎮 Interactive Grid System

* Draw walls using mouse drag
* Place and move **start** / **end** nodes
* Adjustable grid size (**10×10 → 50×50**)
* Responsive dark-themed interface

---

### ⚡ Real-Time Visualization

* Step-by-step pathfinding animation
* Adjustable animation speed
* Explored nodes and final path highlighting
* Open/closed set visualization for A* and Dijkstra

---

### 📊 Live Statistics

Track algorithm performance in real time:

* Nodes visited
* Path length
* Path cost
* Execution time
* Search status

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **GUI Framework:** Tkinter
* **Architecture:** MVC-inspired structure
* **Algorithms:** BFS, DFS, A*, Dijkstra

---

## ⚙️ Requirements

* **Python 3.8+**
* **Tkinter** (included with most Python installations)

### Linux Users

Install Tkinter if it is missing:

```bash
# Debian / Ubuntu
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Maze_Solver_Visualizer_PYTHON.git
cd Maze_Solver_Visualizer_PYTHON
```

---

### 2️⃣ (Optional) Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

No external packages are required.

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the application from the project root:

```bash
python main.py
```

---

## 🎯 Usage Guide

1. Select a pathfinding algorithm
2. Create or generate a maze
3. Adjust speed and grid size (optional)
4. Click **Start Visualization**
5. Observe the algorithm exploring the grid in real time

---

### 🖱️ Mouse Controls

| Action          | Effect                      |
| --------------- | --------------------------- |
| **Left Click**  | Add/remove walls            |
| **Left Drag**   | Draw walls continuously     |
| **Right Click** | Set or move start/end nodes |

Default start node: **Top-left**
Default end node: **Bottom-right**

---

## 📘 Algorithm Summary

| Algorithm    | Description                                    |
| ------------ | ---------------------------------------------- |
| **BFS**      | Finds shortest path in unweighted grids        |
| **DFS**      | Explores deeply but may not find shortest path |
| **Dijkstra** | Computes shortest path using cumulative cost   |
| **A***       | Uses heuristics for faster optimal pathfinding |

All algorithms use **4-directional movement**:
⬆️ Up • ⬇️ Down • ⬅️ Left • ➡️ Right

---

## 🎨 Color Legend

| Color               | Meaning                   |
| ------------------- | ------------------------- |
| 🟩 Green            | Start Node                |
| 🟥 Red              | End Node                  |
| ⬛ Dark Gray / Black | Wall                      |
| ⬜ Light Gray        | Empty Cell                |
| 🔵 Blue Shades      | Explored / Frontier Nodes |
| 🟨 Yellow           | Final Path                |

---

## 📂 Project Structure

```text
Maze_Solver_Visualizer_PYTHON/
├── main.py
├── requirements.txt
├── controller/
│   ├── maze_controller.py
│   └── animation_controller.py
├── model/
│   ├── grid.py
│   ├── cell.py
│   ├── cell_type.py
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
    └── pair.py
```

---

## 🧠 Educational Purpose

This project is ideal for:

* Learning pathfinding algorithms
* Visualizing search strategies
* Understanding algorithm efficiency
* AI and Data Structures coursework
* Experimenting with maze generation techniques

---

## 💡 Future Improvements

* Additional pathfinding algorithms
* Diagonal movement support
* Weighted terrain system
* Save/load maze configurations
* Step-by-step execution mode
* Side-by-side algorithm comparison
* Export statistics and screenshots

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the project and submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Abdul Wali**
Computer Science Student | Software Developer

---

⭐ *If you find this project useful, consider giving it a star!*
