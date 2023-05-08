from numpy._typing import NDArray
import pygame
import numpy as np
import time


class Color():
    Background = (10, 10, 10)
    Grid = (40, 40, 40)
    Alive = (0, 255, 0)


def update(screen: pygame.Surface, cells: NDArray, size: int, rules, with_evolution=True):

    update_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        n_alive_around = np.sum(cells[row - 1: row +2, col -1: col +2]) - cells[row, col]
        color = Color.Background if cells[row, col] == 0 else Color.Alive

        if with_evolution:

            if cells[row, col] == 1:
                if rules[1][0] <= n_alive_around <= rules[1][1]:
                    update_cells[row, col] = 1
                    if with_evolution:
                        color = Color.Alive #

                elif n_alive_around < rules[1][0] or n_alive_around > rules[1][1]:
                    if with_evolution:
                        color = Color.Background #


            else:
                if n_alive_around == rules[0]:
                    update_cells[row, col] = 1
                    if with_evolution:
                        color = Color.Alive


        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return update_cells


def choosen_rules(rules):
    print("Available default rules:")
    for i, rule in enumerate(rules):
        print(f"nr{i + 1} - {rule[0]} neighbours to be born. {rule[1][0]} <= neighbours to stay alivea <= {rule[1][1]}")

    print("Input the index number of the rules you want to choose.")
    print("You will be able to change them later and add custom rules.")
    print("To do that, while the simulation is running, press space to stop it.")
    print("You will be prompted for an input then.")
    while True:
        chooice = int(input(": "))
        if chooice in range(0, len(rules)):
            return chooice
        print("Enter valid input")


def main():

    # (n to be born, (x <= n to stay alive <= x)
    rules: list[tuple[int, tuple[int, int]]] = [(3, (2,3)), (2, (2, 7)), (2, (3, 4))]

    choosen_rules_idx = choosen_rules(rules)

    size = 10


    pygame.init()
    screen = pygame.display.set_mode((80 * size, 60 * size))

    cells = np.zeros((6 * size, 8 * size))
    screen.fill(Color.Grid)


    update(screen, cells, size, rules[choosen_rules_idx], False)

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
                    update(screen, cells, 10, rules[choosen_rules_idx], False) # should be here
                    pygame.display.update() #

            if pygame.mouse.get_pressed()[0]:
                # maby prevent from inserting when its running
                # print("0000000000000000000000000")
                pos = pygame.mouse.get_pos()
                # print(f"1-{pos[1]}")
                # print(f"1.5-{pos[1] // size}")
                # print(f"3-{cells[pos[1] // size, pos[0] // size]}")
                cells[pos[1] // size, pos[0] // size] = 1
                # print(f"3-{cells[pos[1] // size, pos[0] // size]}")
                # print(f"2-{pos[1]}")
                # print(f"2.5-{pos[1] // size}")
                update(screen, cells, size, rules[choosen_rules_idx], False)
                pygame.display.update()

        screen.fill(Color.Grid)

        if not paused:
            cells = update(screen, cells, size, rules[choosen_rules_idx])
            pygame.display.update()


        time.sleep(0.001)

if __name__ == "__main__":
    main()
