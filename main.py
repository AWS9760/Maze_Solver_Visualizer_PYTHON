import tkinter as tk

from controller.maze_controller import MazeController
from model.grid import Grid
from ui.grid_renderer import GridRenderer
from ui.status_bar import StatusBar
from ui.toolbar import Toolbar


DEFAULT_GRID_SIZE = 25
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800


def main() -> None:
    root = tk.Tk()
    root.title("Maze Solver Visualizer")
    root.configure(bg="#1e1e1e")
    root.minsize(800, 600)
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    grid = Grid(DEFAULT_GRID_SIZE, DEFAULT_GRID_SIZE)
    toolbar = Toolbar(root)
    status_bar = StatusBar(root)
    toolbar.get_container().pack(side=tk.TOP, fill=tk.X)
    status_bar.get_container().pack(side=tk.BOTTOM, fill=tk.X)

    canvas = tk.Canvas(root, bg="#1e1e1e", highlightthickness=0)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
    renderer = GridRenderer(canvas, grid)
    controller = MazeController(grid, renderer, status_bar, canvas, root)

    def on_algorithm_change(_event) -> None:
        controller.set_algorithm(toolbar.get_algorithm_combobox().get())

    def on_generator_change(_event) -> None:
        controller.generate_maze(toolbar.get_maze_generator_combobox().get())

    toolbar.get_algorithm_combobox().bind("<<ComboboxSelected>>", on_algorithm_change)
    toolbar.get_maze_generator_combobox().bind("<<ComboboxSelected>>", on_generator_change)
    toolbar.get_start_button().config(command=controller.start_visualization)
    toolbar.get_clear_button().config(command=controller.clear_grid)
    toolbar.get_reset_path_button().config(command=controller.reset_path)
    toolbar.get_random_maze_button().config(
        command=lambda: controller.generate_maze(toolbar.get_maze_generator_combobox().get())
    )

    def on_speed_change(value: str) -> None:
        speed = float(value)
        toolbar.update_speed_label(speed)
        controller.set_speed(speed)

    def on_grid_size_change(value: str) -> None:
        size = int(float(value))
        toolbar.update_grid_size_label(size)
        controller.resize_grid(size)

    toolbar.get_speed_slider().config(command=on_speed_change)
    toolbar.get_grid_size_slider().config(command=on_grid_size_change)
    toolbar.update_grid_size_label(DEFAULT_GRID_SIZE)
    toolbar.update_speed_label(50)

    def on_resize(_event) -> None:
        if canvas.winfo_width() > 0 and canvas.winfo_height() > 0:
            renderer.update_cell_size()
            renderer.render()

    canvas.bind("<Configure>", on_resize)
    renderer.render()
    root.mainloop()


if __name__ == "__main__":
    main()
