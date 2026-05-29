from abc import ABC, abstractmethod

from model.grid import Grid


class MazeGenerator(ABC):
    @abstractmethod
    def generate(self, grid: Grid) -> None:
        pass
