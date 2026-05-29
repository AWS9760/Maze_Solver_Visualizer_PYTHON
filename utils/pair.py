from dataclasses import dataclass


@dataclass(frozen=True)
class Pair:
    row: int
    col: int

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def __str__(self) -> str:
        return f"({self.row}, {self.col})"
