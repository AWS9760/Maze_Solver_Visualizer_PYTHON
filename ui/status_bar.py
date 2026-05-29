import tkinter as tk


class StatusBar:
    def __init__(self, parent) -> None:
        self._container = tk.Frame(parent, bg="#2d2d2d", padx=10, pady=10)
        self._algorithm_label = tk.Label(self._container, text="Algorithm: None", fg="#e0e0e0", bg="#2d2d2d")
        self._visited_label = tk.Label(self._container, text="Nodes Visited: 0", fg="#e0e0e0", bg="#2d2d2d")
        self._path_length_label = tk.Label(self._container, text="Path Length: 0", fg="#e0e0e0", bg="#2d2d2d")
        self._path_cost_label = tk.Label(self._container, text="Path Cost: 0", fg="#e0e0e0", bg="#2d2d2d")
        self._time_label = tk.Label(self._container, text="Time: 0ms", fg="#e0e0e0", bg="#2d2d2d")
        self._status_label = tk.Label(self._container, text="Status: Ready", fg="#e0e0e0", bg="#2d2d2d")
        for widget in (
            self._algorithm_label,
            self._visited_label,
            self._path_length_label,
            self._path_cost_label,
            self._time_label,
            self._status_label,
        ):
            widget.pack(side=tk.LEFT, padx=7)

    def get_container(self):
        return self._container

    def update_algorithm(self, algorithm: str) -> None:
        self._algorithm_label.config(text=f"Algorithm: {algorithm}")

    def update_visited(self, count: int) -> None:
        self._visited_label.config(text=f"Nodes Visited: {count}")

    def update_path_length(self, length: int) -> None:
        self._path_length_label.config(text=f"Path Length: {length}")

    def update_path_cost(self, cost: int) -> None:
        self._path_cost_label.config(text=f"Path Cost: {cost}")

    def update_time(self, time_ms: int) -> None:
        self._time_label.config(text=f"Time: {time_ms}ms")

    def update_status(self, status: str) -> None:
        self._status_label.config(text=f"Status: {status}")

    def reset(self) -> None:
        self._algorithm_label.config(text="Algorithm: None")
        self._visited_label.config(text="Nodes Visited: 0")
        self._path_length_label.config(text="Path Length: 0")
        self._path_cost_label.config(text="Path Cost: 0")
        self._time_label.config(text="Time: 0ms")
        self._status_label.config(text="Status: Ready")
