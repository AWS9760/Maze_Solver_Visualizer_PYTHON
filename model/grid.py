import random
from typing import List, Optional

from model.cell import Cell
from model.cell_type import CellType, INT_MAX
from utils.pair import Pair


class Grid:
    def __init__(self, rows: int, cols: int) -> None:
        self._rows = rows
        self._cols = cols
        self._grid: List[List[Cell]] = [[None for _ in range(cols)] for _ in range(rows)]
        self._start: Optional[Pair] = None
        self._end: Optional[Pair] = None
        self._random = random.Random()
        self._initialize_grid()

    def _initialize_grid(self) -> None:
        for i in range(self._rows):
            for j in range(self._cols):
                self._grid[i][j] = Cell(i, j, CellType.EMPTY)
        self._start = Pair(0, 0)
        self._end = Pair(self._rows - 1, self._cols - 1)
        self._grid[self._start.row][self._start.col].set_type(CellType.START)
        self._grid[self._end.row][self._end.col].set_type(CellType.END)

    def reset_grid(self) -> None:
        for i in range(self._rows):
            for j in range(self._cols):
                cell = self._grid[i][j]
                cell_type = cell.get_type()
                if cell_type in (CellType.VISITED, CellType.PATH, CellType.OPEN_SET, CellType.CLOSED_SET):
                    cell.set_type(CellType.EMPTY)
        if self._start is not None:
            self._grid[self._start.row][self._start.col].set_type(CellType.START)
        if self._end is not None:
            self._grid[self._end.row][self._end.col].set_type(CellType.END)

    def clear_grid(self) -> None:
        for i in range(self._rows):
            for j in range(self._cols):
                self._grid[i][j].set_type(CellType.EMPTY)
        self._start = Pair(0, 0)
        self._end = Pair(self._rows - 1, self._cols - 1)
        self._grid[self._start.row][self._start.col].set_type(CellType.START)
        self._grid[self._end.row][self._end.col].set_type(CellType.END)

    def generate_random_maze(self, wall_probability: float) -> None:
        self.clear_grid()
        for i in range(self._rows):
            for j in range(self._cols):
                current = Pair(i, j)
                if current != self._start and current != self._end:
                    if self._random.random() < wall_probability:
                        self._grid[i][j].set_type(CellType.WALL)

    def get_neighbors(self, row: int, col: int) -> List[Pair]:
        neighbors: List[Pair] = []
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]
            if self.is_valid(new_row, new_col) and self._grid[new_row][new_col].is_walkable():
                neighbors.append(Pair(new_row, new_col))
        return neighbors

    def get_cost(self, row: int, col: int) -> int:
        if self.is_valid(row, col):
            return self._grid[row][col].get_cost()
        return INT_MAX

    def is_valid(self, row: int, col: int) -> bool:
        return 0 <= row < self._rows and 0 <= col < self._cols

    def get_cell(self, row: int, col: int) -> Optional[Cell]:
        if self.is_valid(row, col):
            return self._grid[row][col]
        return None

    def set_cell_type(self, row: int, col: int, cell_type: CellType) -> None:
        if self.is_valid(row, col):
            self._grid[row][col].set_type(cell_type)

    def get_start(self) -> Optional[Pair]:
        return self._start

    def get_end(self) -> Optional[Pair]:
        return self._end

    def set_start(self, row: int, col: int) -> None:
        if self._start is not None and self.is_valid(self._start.row, self._start.col):
            self._grid[self._start.row][self._start.col].set_type(CellType.EMPTY)
        self._start = Pair(row, col)
        if self.is_valid(row, col):
            self._grid[row][col].set_type(CellType.START)

    def set_end(self, row: int, col: int) -> None:
        if self._end is not None and self.is_valid(self._end.row, self._end.col):
            self._grid[self._end.row][self._end.col].set_type(CellType.EMPTY)
        self._end = Pair(row, col)
        if self.is_valid(row, col):
            self._grid[row][col].set_type(CellType.END)

    def get_rows(self) -> int:
        return self._rows

    def get_cols(self) -> int:
        return self._cols

    def resize(self, new_rows: int, new_cols: int) -> None:
        self._rows = new_rows
        self._cols = new_cols
        self._grid = [[None for _ in range(new_cols)] for _ in range(new_rows)]
        self._initialize_grid()
