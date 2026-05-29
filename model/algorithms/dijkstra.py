import heapq
from dataclasses import dataclass, field
from typing import Dict, List, Set

from model.cell_type import INT_MAX
from model.grid import Grid
from utils.pair import Pair


@dataclass(order=True)
class Node:
    distance: int
    position: Pair = field(compare=False)


class Dijkstra:
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

        pq: List[Node] = [Node(0, start)]
        distances: Dict[Pair, int] = {start: 0}
        came_from: Dict[Pair, Pair] = {}
        self._open_set.add(start)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while pq:
            current = heapq.heappop(pq)
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

                edge_cost = self._grid.get_cost(new_row, new_col)
                tentative_distance = distances.get(current_pos, INT_MAX) + edge_cost
                if tentative_distance < distances.get(neighbor, INT_MAX):
                    came_from[neighbor] = current_pos
                    distances[neighbor] = tentative_distance
                    heapq.heappush(pq, Node(tentative_distance, neighbor))
                    self._open_set.add(neighbor)

        return self._path

    def get_visited_order(self) -> List[Pair]:
        return self._visited_order

    def get_path(self) -> List[Pair]:
        return self._path

    def get_open_set(self) -> Set[Pair]:
        return self._open_set

    def get_closed_set(self) -> Set[Pair]:
        return self._closed_set
