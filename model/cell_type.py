from enum import Enum


INT_MAX = 2**31 - 1


class CellType(Enum):
    EMPTY = ("EMPTY", 1)
    WALL = ("WALL", INT_MAX)
    START = ("START", 1)
    END = ("END", 1)
    VISITED = ("VISITED", 1)
    PATH = ("PATH", 1)
    OPEN_SET = ("OPEN_SET", 1)
    CLOSED_SET = ("CLOSED_SET", 1)

    def __init__(self, _: str, cost: int) -> None:
        self._cost = cost

    def get_cost(self) -> int:
        return self._cost

    def is_walkable(self) -> bool:
        return self != CellType.WALL
