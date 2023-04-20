import math
import logging
# level = logging.DEBUG
level = logging.INFO
fmt = "%(levelname)s:%(lineno)d:%(funcName)s: %(message)s"
logging.basicConfig(level = level, format = fmt)


class Vars:
    l = math.pi # length
    n = 10
    dx = l / n
    dt = 0.3
    mi = l / n


def string_movement():
    print("i    ", end="")
    for i in range(Vars.n + 1):
        print(f":    {i}    ", end="")

    xi_table = [0 for _ in range(Vars.n + 1)]
    print("\nxi   ", end="")
    j = 0
    for i in range(Vars.n + 1):
        xi_table[i] = j
        print(f":  {j:.2E}  ", end="")
        j += Vars.dx


    f_table = [0 for _ in range(Vars.n + 1)]
    print("\nf t0 ", end="")
    for i in range(len(f_table)):
        f_table[i] = math.sin(xi_table[i])/1000000
        print(f":  {f_table[i]:.2E}  ", end="")


    print("\nv t0 ", end="")
    v_table = [0 for _ in range(Vars.n + 1)]
    for value in v_table:
        print(f":  {value}.000000  ", end="")


    a_table = [0 for _ in range(Vars.n + 1)]
    print("\na t0 ", end="")
    for i in range(1, len(a_table) - 1):
        a_table[i] = f_table[i+1] - 2 * f_table[i] + f_table[i-1]
    for value in a_table:
        print(f":  {value:.2E}  ", end="")


    # print("i  0   :  1  :  2   :   3  :  4   :  5   :   6   :   7   :   8   :   9   :   10")
    # print(f"i  0   :  1  :  2   :   3  :  4   :  5   :   6   :   7   :   8   :   9   :   10")


def main():
    string_movement()


if __name__ == "__main__":
    main()
