import heapq
from dataclasses import dataclass, field
from typing import Dict, List, Set

from model.cell_type import INT_MAX
from model.grid import Grid
from utils.pair import Pair


@dataclass(order=True)
class Node:
    f: int
    position: Pair = field(compare=False)
    g: int = field(compare=False)
    h: int = field(compare=False)


class AStar:
    def __init__(self, grid: Grid) -> None:
        self._grid = grid
        self._visited_order: List[Pair] = []
        self._path: List[Pair] = []
        self._open_set: Set[Pair] = set()
        self._closed_set: Set[Pair] = set()

    def find_path(self) -> List[Pair]:
        self._visited_order.clear()
        self._path.clear()
        self._open_set.clear()
        self._closed_set.clear()

        start = self._grid.get_start()
        end = self._grid.get_end()
        if start is None or end is None:
            return self._path

        open_set_pq: List[Node] = []
        g_score: Dict[Pair, int] = {start: 0}
        came_from: Dict[Pair, Pair] = {}

        h0 = self.manhattan_distance(start.row, start.col, end.row, end.col)
        heapq.heappush(open_set_pq, Node(h0, start, 0, h0))
        self._open_set.add(start)

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while open_set_pq:
            current = heapq.heappop(open_set_pq)
            current_pos = current.position
            if current_pos in self._closed_set:
                continue

            self._closed_set.add(current_pos)
            self._open_set.discard(current_pos)
            self._visited_order.append(current_pos)

            if current_pos == end:
                node = end
                while node is not None:
                    self._path.insert(0, node)
                    node = came_from.get(node)
                return self._path

            for i in range(4):
                new_row = current_pos.row + dr[i]
                new_col = current_pos.col + dc[i]
                neighbor = Pair(new_row, new_col)
                if (
                    not self._grid.is_valid(new_row, new_col)
                    or not self._grid.get_cell(new_row, new_col).is_walkable()
                    or neighbor in self._closed_set
                ):
                    continue

                cost = self._grid.get_cost(new_row, new_col)
                tentative_g = g_score.get(current_pos, INT_MAX) + cost
                if tentative_g < g_score.get(neighbor, INT_MAX):
                    came_from[neighbor] = current_pos
                    g_score[neighbor] = tentative_g
                    h = self.manhattan_distance(new_row, new_col, end.row, end.col)
                    f = tentative_g + h
                    heapq.heappush(open_set_pq, Node(f, neighbor, tentative_g, h))
                    self._open_set.add(neighbor)

        return self._path

    def manhattan_distance(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return abs(row1 - row2) + abs(col1 - col2)

    def get_visited_order(self) -> List[Pair]:
        return self._visited_order

    def get_path(self) -> List[Pair]:
        return self._path

    def get_open_set(self) -> Set[Pair]:
        return self._open_set

    def get_closed_set(self) -> Set[Pair]:
        return self._closed_set
