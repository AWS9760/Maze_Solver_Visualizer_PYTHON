from model.cell_type import CellType


class Cell:
    def __init__(self, row: int, col: int, cell_type: CellType) -> None:
        self._row = row
        self._col = col
        self._type = cell_type

    def get_row(self) -> int:
        return self._row

    def get_col(self) -> int:
        return self._col

    def get_type(self) -> CellType:
        return self._type

    def set_type(self, cell_type: CellType) -> None:
        self._type = cell_type

    def is_walkable(self) -> bool:
        return self._type.is_walkable()

    def get_cost(self) -> int:
        return self._type.get_cost()

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Cell) and self._row == other._row and self._col == other._col

    def __hash__(self) -> int:
        return 31 * self._row + self._col

    def __str__(self) -> str:
        return f"Cell({self._row}, {self._col}, {self._type.name})"
