from numpy._typing import NDArray
import pygame
import numpy as np
import time


class Color():
    Background = (30, 30, 30)
    Grid = (60, 60, 60)
    Alive = (0, 255, 0)


def update(screen: pygame.Surface, cells: NDArray, size: int, rules, with_evolution=True):

    update_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):

        # n_alive_around = np.sum(cells[row - 1: row +2, col -1: col +2]) - cells[row, col]
        # v - for torus
        n_alive_around = int((cells[row, (col-1)%cells.shape[1]] + cells[row, (col+1)%cells.shape[1]] +
                         cells[(row-1)%cells.shape[0], col] + cells[(row+1)%cells.shape[0], col] +
                         cells[(row-1)%cells.shape[0], (col-1)%cells.shape[1]] + cells[(row-1)%cells.shape[0], (col+1)%cells.shape[1]] +
                         cells[(row+1)%cells.shape[0], (col-1)%cells.shape[1]] + cells[(row+1)%cells.shape[0], (col+1)%cells.shape[1]])) # /255

        color = Color.Background if cells[row, col] == 0 else Color.Alive

        if cells[row, col] == 1:
            if rules[1][0] <= n_alive_around <= rules[1][1]:
                update_cells[row, col] = 1
                if with_evolution:
                    color = Color.Alive

            elif n_alive_around < rules[1][0] or n_alive_around > rules[1][1]:
                if with_evolution:
                    color = Color.Background


        else:
            if n_alive_around == rules[0]:
                update_cells[row, col] = 1
                if with_evolution:
                    color = Color.Alive


        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return update_cells


def choose_rules(rules, first_time=False):
    if first_time:
        print("\nInput the index number of the rules you want to choose.")
        print("You will be able to change them later and add custom rules.")
        print("To do that, while the simulation is running, press r.")
        print("You will be prompted for an input then.\n")

    if not first_time:
        print("If you want to add custom rules input 'r'. To just change them hit enter")

        if str(input(": ")).lower() == "r":
            n_be_born = int(input("Enter n of neighbours to be born: "))
            n_to_live1 =  int(input("Enter minimal number of neighbours to survive: "))
            n_to_live2 = int(input("Enter maximal number of neighbours to survive: "))

            rules.append((n_be_born, (n_to_live1, n_to_live2)))


    print("Available rules:")
    for i, rule in enumerate(rules):
        print(f"nr{i + 1} - {rule[0]} neighbours to be born. {rule[1][0]} <= neighbours to stay alivea <= {rule[1][1]}")

    while True:
        chooice = int(input("Input the index of the choosen rules: "))
        if chooice in range(0, len(rules) + 1):
            print("Input cells / hit space to start the simulation")
            return chooice - 1, rules
        print("Enter valid input")


def ask_for_the_layout(cells):
    print("If you want a blank starting screen where you can place cells press enter.\nOtherwise input 'c'")
    user_input = str(input(": "))
    if user_input == "c":
        print("1 - lotos layout")
        print("2 - glider layout")
        user_input = str(input(": "))
        if user_input == "1":
            cells[30, 30] = 1
            cells[31, 31] = 1
            cells[32, 31] = 1
            cells[31, 30] = 1
            cells[31, 29] = 1
        elif user_input == "2":
            cells[30, 30] = 1
            cells[31, 31] = 1
            cells[29, 30] = 1
            cells[29, 31] = 1
            cells[29, 32] = 1
        else:
            print("Enter valid input")
        print("Press space to start or add more cells")
        return cells

    return cells
            




def main():
    # (n to be born, (x <= n to stay alive <= x)
    rules: list[tuple[int, tuple[int, int]]] = [(3, (2,3)), (2, (2, 7)), (2, (3, 4))]

    choosen_rules_idx, rules = choose_rules(rules, first_time=True)

    size = 10

    cells = np.zeros((6 * size, 8 * size))
    cells = ask_for_the_layout(cells)

    pygame.init()
    screen = pygame.display.set_mode((80 * size, 60 * size))

    screen.fill(Color.Grid)


    update(screen, cells, size, rules[choosen_rules_idx], False)

    pygame.display.flip()
    pygame.display.update()

    paused = True


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

                    if paused:
                        print("~~~Game paused. Hit space to unpause or input cells")
                    else:
                        print("+++Game running. Hit space to pause")

                    update(screen, cells, 10, rules[choosen_rules_idx], False) #
                    pygame.display.update() #

                if event.key == pygame.K_r:
                        paused = not paused
                        choosen_rules_idx, rules = choose_rules(rules)

            if pygame.mouse.get_pressed()[0]:
                if paused:
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
                else:
                    print("You can only input cells when the simulation is paused")

        screen.fill(Color.Grid)

        if not paused:
            cells = update(screen, cells, size, rules[choosen_rules_idx])
            pygame.display.update()

        time.sleep(0.001)


if __name__ == "__main__":
    main()
