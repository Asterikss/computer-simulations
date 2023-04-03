import logging
level = logging.INFO
fmt = "%(levelname)s:%(lineno)d:%(funcName)s: %(message)s"
logging.basicConfig(level = level, format = fmt)


class Vars:
    dt = 0.001 # s
    l = 1 # m
    g = -10 # m/s^2

    m = 1 # kg

    # v0_x = 10
    # v0_y = 10
    #
    # g_x = 0
    # g_y = -10
    #
    # # zakres 0-1
    # q = 0.2


def main():
    ...

if __name__ == "__main__":
    main()
