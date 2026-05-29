import threading
import time
from typing import Optional, Set

from controller.animation_controller import AnimationController
from model.algorithms.astar import AStar
from model.algorithms.bfs import BFS
from model.algorithms.dfs import DFS
from model.algorithms.dijkstra import Dijkstra
from model.cell_type import CellType
from model.grid import Grid
from model.maze.maze_generator import MazeGenerator
from model.maze.wilsons_algorithm import WilsonsAlgorithm
from ui.grid_renderer import GridRenderer
from ui.status_bar import StatusBar
from utils.pair import Pair


class MazeController:
    def __init__(self, grid: Grid, renderer: GridRenderer, status_bar: StatusBar, canvas, root) -> None:
        self._grid = grid
        self._renderer = renderer
        self._status_bar = status_bar
        self._canvas = canvas
        self._root = root
        self._animation_controller = AnimationController(grid, root)
        self._animation_controller.set_on_cell_update(self._on_cell_update)
        self._current_algorithm = "BFS"
        self._is_visualizing = False
        self._current_open_set: Optional[Set[Pair]] = None
        self._current_closed_set: Optional[Set[Pair]] = None
        self._setup_mouse_handlers()

    def _on_cell_update(self) -> None:
        self._renderer.set_open_set(self._current_open_set)
        self._renderer.set_closed_set(self._current_closed_set)
        self._renderer.render()

    def _setup_mouse_handlers(self) -> None:
        self._canvas.bind("<Button-1>", self._handle_primary_press)
        self._canvas.bind("<Button-3>", self._handle_secondary_press)
        self._canvas.bind("<B1-Motion>", self._handle_mouse_drag)

    def _handle_primary_press(self, event) -> None:
        if self._is_visualizing:
            return
        cell_pos = self._renderer.get_cell_from_mouse(event.x, event.y)
        if cell_pos is None:
            return
        row = cell_pos.row
        col = cell_pos.col
        current_type = self._grid.get_cell(row, col).get_type()
        if current_type == CellType.WALL:
            self._grid.set_cell_type(row, col, CellType.EMPTY)
        elif current_type not in (CellType.START, CellType.END):
            self._grid.set_cell_type(row, col, CellType.WALL)
        self._renderer.render()

    def _handle_secondary_press(self, event) -> None:
        if self._is_visualizing:
            return
        cell_pos = self._renderer.get_cell_from_mouse(event.x, event.y)
        if cell_pos is None:
            return
        row = cell_pos.row
        col = cell_pos.col
        current_type = self._grid.get_cell(row, col).get_type()
        if current_type == CellType.START:
            self._grid.set_end(row, col)
        elif current_type == CellType.END:
            self._grid.set_cell_type(row, col, CellType.EMPTY)
        else:
            self._grid.set_start(row, col)
        self._renderer.render()

    def _handle_mouse_drag(self, event) -> None:
        if self._is_visualizing:
            return
        cell_pos = self._renderer.get_cell_from_mouse(event.x, event.y)
        if cell_pos is None:
            return
        row = cell_pos.row
        col = cell_pos.col
        current_type = self._grid.get_cell(row, col).get_type()
        if current_type not in (CellType.START, CellType.END, CellType.WALL):
            self._grid.set_cell_type(row, col, CellType.WALL)
            self._renderer.render()

    def start_visualization(self) -> None:
        if self._is_visualizing:
            return
        self._is_visualizing = True
        self._grid.reset_grid()
        self._renderer.set_open_set(None)
        self._renderer.set_closed_set(None)
        self._renderer.render()
        self._status_bar.update_status(f"Running {self._current_algorithm}...")
        start_time = int(time.time() * 1000)

        def worker() -> None:
            visited_order = []
            path = []
            open_set = None
            closed_set = None
            path_cost = 0
            if self._current_algorithm == "BFS":
                bfs = BFS(self._grid)
                path = bfs.find_path()
                visited_order = bfs.get_visited_order()
            elif self._current_algorithm == "DFS":
                dfs = DFS(self._grid)
                path = dfs.find_path()
                visited_order = dfs.get_visited_order()
            elif self._current_algorithm == "A*":
                a_star = AStar(self._grid)
                path = a_star.find_path()
                visited_order = a_star.get_visited_order()
                open_set = a_star.get_open_set()
                closed_set = a_star.get_closed_set()
            elif self._current_algorithm == "Dijkstra":
                dijkstra = Dijkstra(self._grid)
                path = dijkstra.find_path()
                visited_order = dijkstra.get_visited_order()
                open_set = dijkstra.get_open_set()
                closed_set = dijkstra.get_closed_set()

            if len(path) > 0:
                for p in path:
                    path_cost += self._grid.get_cost(p.row, p.col)

            end_time = int(time.time() * 1000)
            duration = end_time - start_time

            def on_ui() -> None:
                self._current_open_set = open_set
                self._current_closed_set = closed_set
                self._status_bar.update_visited(len(visited_order))
                self._status_bar.update_path_length(len(path) - 1 if len(path) > 0 else 0)
                self._status_bar.update_path_cost(path_cost)
                self._status_bar.update_time(duration)
                self._renderer.set_open_set(open_set)
                self._renderer.set_closed_set(closed_set)

                def complete() -> None:
                    self._is_visualizing = False
                    if len(path) > 0:
                        self._status_bar.update_status("Path found!")
                    else:
                        self._status_bar.update_status("No path found!")

                self._animation_controller.animate(visited_order, path, complete, self._current_algorithm)

            self._root.after(0, on_ui)

        threading.Thread(target=worker, daemon=True).start()

    def clear_grid(self) -> None:
        if self._is_visualizing:
            return
        self._animation_controller.stop()
        self._grid.clear_grid()
        self._renderer.set_open_set(None)
        self._renderer.set_closed_set(None)
        self._renderer.render()
        self._status_bar.reset()

    def reset_path(self) -> None:
        if self._is_visualizing:
            return
        self._animation_controller.stop()
        self._grid.reset_grid()
        self._renderer.set_open_set(None)
        self._renderer.set_closed_set(None)
        self._renderer.render()
        self._status_bar.update_visited(0)
        self._status_bar.update_path_length(0)
        self._status_bar.update_path_cost(0)
        self._status_bar.update_time(0)
        self._status_bar.update_status("Ready")

    def generate_maze(self, generator_type: str) -> None:
        if self._is_visualizing:
            return
        self._animation_controller.stop()

        generator: Optional[MazeGenerator] = None
        if generator_type == "Wilson's Algorithm":
            generator = WilsonsAlgorithm()
        else:
            self._grid.generate_random_maze(0.3)
            self._renderer.render()
            self._status_bar.reset()
            return

        generator.generate(self._grid)
        self._renderer.render()
        self._status_bar.reset()

    def set_algorithm(self, algorithm: str) -> None:
        self._current_algorithm = algorithm
        self._status_bar.update_algorithm(algorithm)

    def set_speed(self, speed: float) -> None:
        self._animation_controller.set_speed(speed)

    def resize_grid(self, new_size: int) -> None:
        if self._is_visualizing:
            return
        self._animation_controller.stop()
        self._grid.resize(new_size, new_size)
        self._renderer.set_grid(self._grid)
        self._renderer.render()
        self._status_bar.reset()

    def is_visualizing(self) -> bool:
        return self._is_visualizing
