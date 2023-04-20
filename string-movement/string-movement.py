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
    print("\nxi   ", end="")
    i = 0
    for _ in range(Vars.n + 1):
        i += Vars.dx
        print(f":  {i:.3f}  ", end="")
    # print("i  0   :  1  :  2   :   3  :  4   :  5   :   6   :   7   :   8   :   9   :   10")
    # print(f"i  0   :  1  :  2   :   3  :  4   :  5   :   6   :   7   :   8   :   9   :   10")


def main():
    string_movement()


if __name__ == "__main__":
    main()
