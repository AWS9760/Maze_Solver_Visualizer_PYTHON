from typing import Callable, List, Optional

from model.cell_type import CellType
from model.grid import Grid
from utils.pair import Pair


class AnimationController:
    def __init__(self, grid: Grid, root) -> None:
        self._grid = grid
        self._root = root
        self._visited_order: List[Pair] = []
        self._path: List[Pair] = []
        self._scheduled_ids: List[str] = []
        self._on_animation_complete: Optional[Callable[[], None]] = None
        self._on_cell_update: Optional[Callable[[], None]] = None
        self._speed = 50.0

    def set_on_cell_update(self, on_cell_update: Callable[[], None]) -> None:
        self._on_cell_update = on_cell_update

    def animate(
        self,
        visited_order: List[Pair],
        path: List[Pair],
        on_complete: Optional[Callable[[], None]],
        algorithm: Optional[str],
    ) -> None:
        self._visited_order = visited_order
        self._path = path
        self._on_animation_complete = on_complete
        self.stop()

        delay = (101 - self._speed) * 2
        is_bfs_or_dfs = algorithm in ("BFS", "DFS")
        is_astar_or_dijkstra = algorithm in ("A*", "Dijkstra")
        visited_delay = delay * 2.0 if is_astar_or_dijkstra else delay
        if is_bfs_or_dfs:
            path_start_offset = len(visited_order)
        else:
            path_start_offset = min(30, len(visited_order)) if len(path) > 0 else len(visited_order)

        for i, cell in enumerate(visited_order):
            event_id = self._root.after(int(visited_delay * (i + 1)), self._visit_cell, cell)
            self._scheduled_ids.append(event_id)

        if len(path) > 0:
            path_start_time = visited_delay * path_start_offset
            for i, cell in enumerate(path):
                event_id = self._root.after(
                    int(path_start_time + delay * (i + 1)),
                    self._path_cell,
                    cell,
                )
                self._scheduled_ids.append(event_id)

        if on_complete is not None:
            if len(path) > 0:
                path_start_time = visited_delay * path_start_offset
                completion_time = path_start_time + delay * (len(path) + 1)
            else:
                completion_time = visited_delay * (len(visited_order) + 1)
            event_id = self._root.after(int(completion_time), on_complete)
            self._scheduled_ids.append(event_id)

    def _visit_cell(self, cell: Pair) -> None:
        if self._grid.is_valid(cell.row, cell.col):
            current_type = self._grid.get_cell(cell.row, cell.col).get_type()
            if current_type not in (CellType.START, CellType.END, CellType.PATH):
                self._grid.set_cell_type(cell.row, cell.col, CellType.VISITED)
                if self._on_cell_update is not None:
                    self._on_cell_update()

    def _path_cell(self, cell: Pair) -> None:
        if self._grid.is_valid(cell.row, cell.col):
            current_type = self._grid.get_cell(cell.row, cell.col).get_type()
            if current_type not in (CellType.START, CellType.END):
                self._grid.set_cell_type(cell.row, cell.col, CellType.PATH)
                if self._on_cell_update is not None:
                    self._on_cell_update()

    def stop(self) -> None:
        for event_id in self._scheduled_ids:
            try:
                self._root.after_cancel(event_id)
            except Exception:
                pass
        self._scheduled_ids.clear()

    def set_speed(self, speed: float) -> None:
        self._speed = speed
