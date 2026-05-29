import tkinter as tk
from tkinter import ttk


class Toolbar:
    def __init__(self, parent) -> None:
        self._container = tk.Frame(parent, bg="#2d2d2d", padx=10, pady=10)
        self._algorithm_var = tk.StringVar(value="BFS")
        self._maze_gen_var = tk.StringVar(value="Random")
        self._speed_var = tk.DoubleVar(value=50)
        self._grid_size_var = tk.DoubleVar(value=25)
        self._speed_label_var = tk.StringVar(value="Speed: 50")
        self._grid_size_label_var = tk.StringVar(value="Grid Size: 25x25")

        row1 = tk.Frame(self._container, bg="#2d2d2d")
        row1.pack(anchor="w", pady=2)
        tk.Label(row1, text="Algorithm:", fg="#e0e0e0", bg="#2d2d2d").pack(side=tk.LEFT, padx=(0, 10))
        self._algorithm_combobox = ttk.Combobox(
            row1,
            values=["BFS", "DFS", "A*", "Dijkstra"],
            state="readonly",
            textvariable=self._algorithm_var,
            width=18,
        )
        self._algorithm_combobox.pack(side=tk.LEFT)

        row2 = tk.Frame(self._container, bg="#2d2d2d")
        row2.pack(anchor="w", pady=2)
        tk.Label(row2, text="Maze Generator:", fg="#e0e0e0", bg="#2d2d2d").pack(side=tk.LEFT, padx=(0, 10))
        self._maze_generator_combobox = ttk.Combobox(
            row2,
            values=["Random", "Wilson's Algorithm"],
            state="readonly",
            textvariable=self._maze_gen_var,
            width=20,
        )
        self._maze_generator_combobox.pack(side=tk.LEFT)

        row3 = tk.Frame(self._container, bg="#2d2d2d")
        row3.pack(anchor="w", pady=2)
        self._start_button = tk.Button(row3, text="Start Visualization", width=16)
        self._clear_button = tk.Button(row3, text="Clear Grid", width=12)
        self._reset_path_button = tk.Button(row3, text="Reset Path", width=12)
        self._start_button.pack(side=tk.LEFT, padx=(0, 10))
        self._clear_button.pack(side=tk.LEFT, padx=(0, 10))
        self._reset_path_button.pack(side=tk.LEFT)

        row4 = tk.Frame(self._container, bg="#2d2d2d")
        row4.pack(anchor="w", pady=2)
        self._random_maze_button = tk.Button(row4, text="Generate Maze", width=16)
        self._random_maze_button.pack(side=tk.LEFT)

        row5 = tk.Frame(self._container, bg="#2d2d2d")
        row5.pack(anchor="w", pady=2)
        tk.Label(row5, textvariable=self._speed_label_var, fg="#e0e0e0", bg="#2d2d2d").pack(side=tk.LEFT, padx=(0, 10))
        self._speed_slider = tk.Scale(
            row5,
            from_=1,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self._speed_var,
            length=200,
            bg="#2d2d2d",
            fg="#e0e0e0",
            highlightthickness=0,
        )
        self._speed_slider.pack(side=tk.LEFT)

        row6 = tk.Frame(self._container, bg="#2d2d2d")
        row6.pack(anchor="w", pady=2)
        tk.Label(row6, textvariable=self._grid_size_label_var, fg="#e0e0e0", bg="#2d2d2d").pack(side=tk.LEFT, padx=(0, 10))
        self._grid_size_slider = tk.Scale(
            row6,
            from_=10,
            to=50,
            orient=tk.HORIZONTAL,
            variable=self._grid_size_var,
            length=200,
            resolution=1,
            bg="#2d2d2d",
            fg="#e0e0e0",
            highlightthickness=0,
        )
        self._grid_size_slider.pack(side=tk.LEFT)

    def get_container(self):
        return self._container

    def get_algorithm_combobox(self):
        return self._algorithm_combobox

    def get_start_button(self):
        return self._start_button

    def get_clear_button(self):
        return self._clear_button

    def get_reset_path_button(self):
        return self._reset_path_button

    def get_random_maze_button(self):
        return self._random_maze_button

    def get_speed_slider(self):
        return self._speed_slider

    def get_grid_size_slider(self):
        return self._grid_size_slider

    def update_grid_size_label(self, size: int) -> None:
        self._grid_size_label_var.set(f"Grid Size: {size}x{size}")

    def get_maze_generator_combobox(self):
        return self._maze_generator_combobox

    def update_speed_label(self, speed: float) -> None:
        self._speed_label_var.set(f"Speed: {int(speed)}")
