import tkinter as tk
from typing import Optional, Set

from model.cell_type import CellType
from model.grid import Grid
from utils.pair import Pair


class GridRenderer:
    def __init__(self, canvas: tk.Canvas, grid: Grid) -> None:
        self._canvas = canvas
        self._grid = grid
        self._cell_width = 1.0
        self._cell_height = 1.0
        self._hovered_cell: Optional[Pair] = None
        self._open_set: Optional[Set[Pair]] = None
        self._closed_set: Optional[Set[Pair]] = None
        self._dark_mode = True
        self.update_cell_size()
        self._setup_hover_handlers()

    def _setup_hover_handlers(self) -> None:
        self._canvas.bind("<Motion>", self._on_mouse_moved)
        self._canvas.bind("<Leave>", self._on_mouse_exited)

    def _on_mouse_moved(self, event) -> None:
        cell_pos = self.get_cell_from_mouse(event.x, event.y)
        if cell_pos is not None and cell_pos != self._hovered_cell:
            self._hovered_cell = cell_pos
            self.render()

    def _on_mouse_exited(self, _event) -> None:
        self._hovered_cell = None
        self.render()

    def update_cell_size(self) -> None:
        width = max(1, self._canvas.winfo_width())
        height = max(1, self._canvas.winfo_height())
        self._cell_width = width / self._grid.get_cols()
        self._cell_height = height / self._grid.get_rows()

    def set_open_set(self, open_set: Optional[Set[Pair]]) -> None:
        self._open_set = open_set

    def set_closed_set(self, closed_set: Optional[Set[Pair]]) -> None:
        self._closed_set = closed_set

    def render(self) -> None:
        self._canvas.delete("all")
        bg = "#1e1e1e" if self._dark_mode else "#ffffff"
        self._canvas.configure(bg=bg)

        for i in range(self._grid.get_rows()):
            for j in range(self._grid.get_cols()):
                cell = self._grid.get_cell(i, j)
                if cell is None:
                    continue
                pos = Pair(i, j)
                x1 = j * self._cell_width
                y1 = i * self._cell_height
                x2 = x1 + self._cell_width
                y2 = y1 + self._cell_height
                if self._open_set is not None and pos in self._open_set and cell.get_type() not in (CellType.START, CellType.END):
                    self._draw_cell_with_type(x1, y1, x2, y2, CellType.OPEN_SET)
                elif (
                    self._closed_set is not None
                    and pos in self._closed_set
                    and cell.get_type() not in (CellType.START, CellType.END, CellType.PATH)
                ):
                    self._draw_cell_with_type(x1, y1, x2, y2, CellType.CLOSED_SET)
                else:
                    self._draw_cell(x1, y1, x2, y2, cell.get_type())

        if self._hovered_cell is not None:
            x = self._hovered_cell.col * self._cell_width
            y = self._hovered_cell.row * self._cell_height
            self._canvas.create_rectangle(
                x + 1,
                y + 1,
                x + self._cell_width - 1,
                y + self._cell_height - 1,
                outline="#ffc800",
                width=3,
            )

        grid_color = "#3c3c3c" if self._dark_mode else "#d3d3d3"
        for i in range(self._grid.get_rows() + 1):
            y = i * self._cell_height
            self._canvas.create_line(0, y, self._canvas.winfo_width(), y, fill=grid_color, width=1)
        for j in range(self._grid.get_cols() + 1):
            x = j * self._cell_width
            self._canvas.create_line(x, 0, x, self._canvas.winfo_height(), fill=grid_color, width=1)

    def _draw_cell(self, x1: float, y1: float, x2: float, y2: float, cell_type: CellType) -> None:
        color = self._get_color_for_cell_type(cell_type)
        self._canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        if cell_type == CellType.PATH:
            self._canvas.create_rectangle(x1 + 1, y1 + 1, x2 - 1, y2 - 1, outline="#ffd700", width=2)

    def _draw_cell_with_type(self, x1: float, y1: float, x2: float, y2: float, override_type: CellType) -> None:
        color = self._get_color_for_cell_type(override_type)
        self._canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def _get_color_for_cell_type(self, cell_type: CellType) -> str:
        if self._dark_mode:
            return {
                CellType.EMPTY: "#d3d3d3",
                CellType.WALL: "#141414",
                CellType.START: "#4caf50",
                CellType.END: "#f44336",
                CellType.VISITED: "#2196f3",
                CellType.PATH: "#ffeb3b",
                CellType.OPEN_SET: "#81d4fa",
                CellType.CLOSED_SET: "#64b5f6",
            }.get(cell_type, "#d3d3d3")
        return {
            CellType.EMPTY: "#ffffff",
            CellType.WALL: "#000000",
            CellType.START: "#4caf50",
            CellType.END: "#f44336",
            CellType.VISITED: "#90caf9",
            CellType.PATH: "#ffeb3b",
            CellType.OPEN_SET: "#bbdefb",
            CellType.CLOSED_SET: "#90caf9",
        }.get(cell_type, "#ffffff")

    def get_cell_from_mouse(self, mouse_x: float, mouse_y: float) -> Optional[Pair]:
        col = int(mouse_x / self._cell_width)
        row = int(mouse_y / self._cell_height)
        if self._grid.is_valid(row, col):
            return Pair(row, col)
        return None

    def set_grid(self, grid: Grid) -> None:
        self._grid = grid
        self.update_cell_size()
