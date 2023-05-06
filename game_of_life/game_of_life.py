import pygame
import numpy as np

class Color():
    Background = (10, 10, 10)
    Grid = (40, 40, 40)
    Alive = (255, 255, 255)

rules = [(2,3)]

def update(screen, cells, size):
    updated_cells = np.empty((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        n_alive_around = np.sum(cells[row - 1: row + 2, col - 1: col + 2]) - cells[row, col]


def main():
    ...

if __name__ == "__main__":
    main()
