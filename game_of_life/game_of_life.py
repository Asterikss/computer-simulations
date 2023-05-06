from numpy._typing import NDArray
import pygame
import numpy as np
import time

class Color():
    Background = (10, 10, 10)
    Grid = (40, 40, 40)
    Alive = (255, 255, 255)

rules: list[tuple[int, tuple[int, int]]] = [(3, (2,3))]


def update(screen: pygame.Surface, cells: NDArray, size: int, rules):
    update_cells = np.zeros((cells.shape[0], cells.shape[1]))
    color = Color.Background

    for row, col in np.ndindex(cells.shape):
        n_alive_around = np.sum(cells[row - 1: row +2, col -1: col +2]) - cells[row, col]

        
        if cells[row, col] == 1:
            if rules[1][0] <= n_alive_around <= rules[1][1]:
                update_cells[row, col] = 1
                color = Color.Alive

        else:
            if n_alive_around == rules[0]:
                update_cells[row, col] = 1
                color = Color.Alive


        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return update_cells


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
    screen.fill(Color.Grid)

    size = 10

    update(screen, cells, size, rules[0])

    pygame.display.flip()
    pygame.display.update()

    paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    # update(screen, cells, 10, rules)
                    pygame.display.update() #

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // size, pos[0] // size] = 1
                update(screen, cells, size, rules[0])
                pygame.display.update()

        screen.fill(Color.Grid)

        if not paused:
            cells = update(screen, cells, size, rules[0])
            pygame.display.update()


        time.sleep(0.001)



# (To be born, (x <= To stay alive <= x)
if __name__ == "__main__":
    main()
