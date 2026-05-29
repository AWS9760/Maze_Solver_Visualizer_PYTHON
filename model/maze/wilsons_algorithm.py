import random
from typing import List, Optional

from model.cell_type import CellType, INT_MAX
from model.grid import Grid
from model.maze.maze_generator import MazeGenerator
from utils.pair import Pair


class WilsonsAlgorithm(MazeGenerator):
    def __init__(self) -> None:
        self._random = random.Random()

    def generate(self, grid: Grid) -> None:
        actual_start = grid.get_start()
        actual_end = grid.get_end()
        start_row = actual_start.row
        start_col = actual_start.col
        end_row = actual_end.row
        end_col = actual_end.col

        for i in range(grid.get_rows()):
            for j in range(grid.get_cols()):
                if (i == start_row and j == start_col) or (i == end_row and j == end_col):
                    grid.set_cell_type(i, j, CellType.EMPTY)
                else:
                    grid.set_cell_type(i, j, CellType.WALL)

        unvisited: List[Pair] = []
        for i in range(1, grid.get_rows() - 1, 2):
            for j in range(1, grid.get_cols() - 1, 2):
                unvisited.append(Pair(i, j))

        maze_start = unvisited.pop(self._random.randrange(len(unvisited)))
        grid.set_cell_type(maze_start.row, maze_start.col, CellType.EMPTY)

        dr = [-2, 2, 0, 0]
        dc = [0, 0, -2, 2]

        while unvisited:
            current = unvisited[self._random.randrange(len(unvisited))]
            path = [current]

            while grid.get_cell(current.row, current.col).get_type() == CellType.WALL:
                neighbors = []
                for i in range(4):
                    new_row = current.row + dr[i]
                    new_col = current.col + dc[i]
                    if grid.is_valid(new_row, new_col):
                        neighbors.append(Pair(new_row, new_col))
                if neighbors:
                    current = neighbors[self._random.randrange(len(neighbors))]
                    if current in path:
                        idx = path.index(current)
                        path = path[: idx + 1]
                    else:
                        path.append(current)

            for i in range(len(path) - 1):
                cell = path[i]
                nxt = path[i + 1]
                grid.set_cell_type(cell.row, cell.col, CellType.EMPTY)
                wall_row = (cell.row + nxt.row) // 2
                wall_col = (cell.col + nxt.col) // 2
                grid.set_cell_type(wall_row, wall_col, CellType.EMPTY)
                if cell in unvisited:
                    unvisited.remove(cell)

            last = path[-1]
            grid.set_cell_type(last.row, last.col, CellType.EMPTY)
            if last in unvisited:
                unvisited.remove(last)

        self._connect_to_maze(grid, start_row, start_col)
        self._connect_to_maze(grid, end_row, end_col)
        grid.set_start(start_row, start_col)
        grid.set_end(end_row, end_col)

    def _connect_to_maze(self, grid: Grid, row: int, col: int) -> None:
        nearest_empty = self._find_nearest_empty(grid, row, col, row, col)
        if nearest_empty is not None:
            current_row = row
            current_col = col
            target_row = nearest_empty.row
            target_col = nearest_empty.col

            while current_row != target_row or current_col != target_col:
                if current_col != target_col:
                    step = 1 if target_col > current_col else -1
                    current_col += step
                elif current_row != target_row:
                    step = 1 if target_row > current_row else -1
                    current_row += step
                if grid.is_valid(current_row, current_col):
                    grid.set_cell_type(current_row, current_col, CellType.EMPTY)
                else:
                    break
        else:
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            for i in range(4):
                new_row = row + dr[i]
                new_col = col + dc[i]
                if grid.is_valid(new_row, new_col):
                    grid.set_cell_type(new_row, new_col, CellType.EMPTY)
                    if grid.is_valid(new_row + dr[i], new_col + dc[i]):
                        grid.set_cell_type(new_row + dr[i], new_col + dc[i], CellType.EMPTY)

    def _find_nearest_empty(
        self, grid: Grid, row: int, col: int, exclude_row: int, exclude_col: int
    ) -> Optional[Pair]:
        nearest = None
        min_manhattan_dist = INT_MAX
        max_radius = max(grid.get_rows(), grid.get_cols())
        for radius in range(1, max_radius + 1):
            for d_row in range(-radius, radius + 1):
                for d_col in range(-radius, radius + 1):
                    if abs(d_row) + abs(d_col) == radius:
                        new_row = row + d_row
                        new_col = col + d_col
                        if new_row == exclude_row and new_col == exclude_col:
                            continue
                        if grid.is_valid(new_row, new_col):
                            cell_type = grid.get_cell(new_row, new_col).get_type()
                            if cell_type == CellType.EMPTY:
                                manhattan_dist = abs(d_row) + abs(d_col)
                                if manhattan_dist < min_manhattan_dist:
                                    min_manhattan_dist = manhattan_dist
                                    nearest = Pair(new_row, new_col)
            if nearest is not None and min_manhattan_dist <= 10:
                return nearest
        return nearest
