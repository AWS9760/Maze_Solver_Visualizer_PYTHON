from collections import deque
from typing import Dict, List, Set

from model.grid import Grid
from utils.pair import Pair


class BFS:
    def __init__(self, grid: Grid) -> None:
        self._grid = grid
        self._visited_order: List[Pair] = []
        self._path: List[Pair] = []

    def find_path(self) -> List[Pair]:
        self._visited_order.clear()
        self._path.clear()

        start = self._grid.get_start()
        end = self._grid.get_end()
        if start is None or end is None:
            return self._path

        queue = deque([start])
        parent: Dict[Pair, Pair] = {}
        visited: Set[Pair] = {start}

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while queue:
            current = queue.popleft()
            self._visited_order.append(current)
            if current == end:
                node = end
                while node is not None:
                    self._path.insert(0, node)
                    node = parent.get(node)
                return self._path

            for i in range(4):
                new_row = current.row + dr[i]
                new_col = current.col + dc[i]
                neighbor = Pair(new_row, new_col)
                if (
                    self._grid.is_valid(new_row, new_col)
                    and self._grid.get_cell(new_row, new_col).is_walkable()
                    and neighbor not in visited
                ):
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)

        return self._path

    def get_visited_order(self) -> List[Pair]:
        return self._visited_order

    def get_path(self) -> List[Pair]:
        return self._path
