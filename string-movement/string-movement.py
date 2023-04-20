import math
import logging
# level = logging.DEBUG
level = logging.INFO
fmt = "%(levelname)s:%(lineno)d:%(funcName)s: %(message)s"
# logging.basicConfig(level = level, format = fmt, filename="log.log", filemode="w")
logging.basicConfig(level = level, format = fmt)


class Vars:
    l = math.pi # length
    n = 10
    dx = l / n
    dt = 0.3
    mi = l / n


def string_movement_euler():
    print("------string movement - euler-------")

    print("i    ", end="")
    for i in range(Vars.n + 1):
        print(f":    {i}    ", end="")

    xi_table = [0.0 for _ in range(Vars.n + 1)]
    print("\nxi   ", end="")
    j = 0
    for i in range(Vars.n + 1):
        xi_table[i] = j
        print(f":  {j:.2E}  ", end="")
        j += Vars.dx


    f_table = [0.0 for _ in range(Vars.n + 1)]
    print("\nf t0 ", end="")
    for i in range(len(f_table) - 1):
        f_table[i] = math.sin(xi_table[i])/1000000
        print(f":  {f_table[i]:.2E}  ", end="")
    print(f":  {f_table[-1]:.2E}  ", end="")


    print("\nv t0 ", end="")
    v_table = [0.0 for _ in range(Vars.n + 1)]
    for value in v_table:
        print(f":  {value}00000  ", end="")


    a_table = [0.0 for _ in range(Vars.n + 1)]
    print("\na t0  ", end="")
    for i in range(1, len(a_table) - 1):
        a_table[i] = (f_table[i+1] - (2 * f_table[i]) + f_table[i-1]) / (Vars.dx**2)
    for value in a_table:
        print(f": {value:.2E}  ", end="")


    potential_energy: list[float] = [0.0 for _ in range(Vars.n + 1)]
    sum = 0.0
    for i in range(1, Vars.n + 1):
        sum += math.pow((f_table[i] - f_table[i-1]), 2)
    sum *= (1 /(2*Vars.dx))
    potential_energy[0] = sum


    kinetic_energy: list[float] = [0.0 for _ in range(Vars.n + 1)]
    sum = 0.0
    for i in range(1, Vars.n):
        sum += math.pow(v_table[i], 2)
    sum *= (Vars.mi / 2)
    kinetic_energy[0] = sum


    print(f"\nPotential energy: {potential_energy[0]:.2E}  Kinetic energy: {kinetic_energy[0]:.2E}  "+
          f"Total energy: {potential_energy[0] + kinetic_energy[0]}")


    for j in range(1, 11):
        print(f"\nf t{j} ", end="")
        for i in range(len(f_table)):
            f_table[i] += v_table[i] * Vars.dt
            print(f":  {f_table[i]:.2E}  ", end="")


        print(f"\nv t{j} ", end="")
        for i in range(len(v_table)):
            v_table[i] += a_table[i] * Vars.dt
            print(f":  {v_table[i]:.2E} ", end="")


        print(f"\na t{j}  ", end="")
        for i in range(1, len(a_table) - 1):
            a_table[i] = (f_table[i+1] - (2 * f_table[i]) + f_table[i-1]) / (Vars.dx**2)
        for value in a_table:
            print(f":  {value:.2E} ", end="")


        sum = 0.0
        for i in range(1, Vars.n + 1):
            sum += math.pow((f_table[i] - f_table[i-1]), 2)
        sum *= (1 /(2*Vars.dx))
        potential_energy[j] = sum


        sum = 0.0
        for i in range(1, Vars.n):
            sum += math.pow(v_table[i], 2)
        sum *= (Vars.mi / 2)
        kinetic_energy[j] = sum


        print(f"\nPotential energy: {potential_energy[j]:.2E}  Kinetic energy: {kinetic_energy[j]:.2E}  "+
              f"Total energy: {potential_energy[j] + kinetic_energy[j]}")


def string_movement_imprv_euler():
    print("------string movement - improved euler-------")

    print("i    ", end="")
    for i in range(Vars.n + 1):
        print(f":    {i}    ", end="")

    xi_table = [0.0 for _ in range(Vars.n + 1)]
    print("\nxi   ", end="")
    j = 0
    for i in range(Vars.n + 1):
        xi_table[i] = j
        print(f":  {j:.2E}  ", end="")
        j += Vars.dx


    f_table = [0.0 for _ in range(Vars.n + 1)]
    print("\nf t0 ", end="")
    for i in range(len(f_table) - 1):
        f_table[i] = math.sin(xi_table[i])/1000000
        print(f":  {f_table[i]:.2E}  ", end="")
    print(f":  {f_table[-1]:.2E}  ", end="")


    print("\nv t0 ", end="")
    v_table = [0.0 for _ in range(Vars.n + 1)]
    for value in v_table:
        print(f":  {value}00000  ", end="")


    a_table = [0.0 for _ in range(Vars.n + 1)]
    print("\na t0  ", end="")
    for i in range(1, len(a_table) - 1):
        a_table[i] = (f_table[i+1] - (2 * f_table[i]) + f_table[i-1]) / (Vars.dx**2)
    for value in a_table:
        print(f": {value:.2E}  ", end="")


    potential_energy: list[float] = [0.0 for _ in range(Vars.n + 1)]
    sum = 0.0
    for i in range(1, Vars.n + 1):
        sum += math.pow((f_table[i] - f_table[i-1]), 2)
    sum *= (1 /(2*Vars.dx))
    potential_energy[0] = sum


    kinetic_energy: list[float] = [0.0 for _ in range(Vars.n + 1)]
    sum = 0.0
    for i in range(1, Vars.n):
        sum += math.pow(v_table[i], 2)
    sum *= (Vars.mi / 2)
    kinetic_energy[0] = sum


    print(f"\nPotential energy: {potential_energy[0]:.2E}  Kinetic energy: {kinetic_energy[0]:.2E}  "+
          f"Total energy: {potential_energy[0] + kinetic_energy[0]}")


    for j in range(1, 11):
        v_mid_table = [0.0 for _ in range(Vars.n + 1)]
        for i in range(len(v_mid_table)):
            v_mid_table[i] += v_table[i] + a_table[i] * (Vars.dt/2)


        f_mid_table = [0.0 for _ in range(Vars.n + 1)]
        for i in range(len(f_mid_table)):
            f_mid_table[i] = f_table[i] + v_table[i] * (Vars.dt/2)


        a_mid_table = [0.0 for _ in range(Vars.n + 1)]
        for i in range(1, len(a_mid_table) - 1):
            a_mid_table[i] = (f_mid_table[i+1] - (2 * f_mid_table[i]) + f_mid_table[i-1]) / (Vars.dx**2)


        print(f"\nf t{j} ", end="")
        for i in range(len(f_table)):
            f_table[i] += v_mid_table[i] * Vars.dt
            print(f":  {f_table[i]:.2E}  ", end="")


        print(f"\nv t{j} ", end="")
        for i in range(len(v_table)):
            v_table[i] += a_mid_table[i] * Vars.dt
            print(f":  {v_table[i]:.2E} ", end="")


        print(f"\na t{j}  ", end="")
        for i in range(1, len(a_table) - 1):
            a_table[i] = (f_mid_table[i+1] - (2 * f_mid_table[i]) + f_mid_table[i-1]) / (Vars.dx**2) #
        for value in a_table:
            print(f":  {value:.2E} ", end="")


        sum = 0.0
        for i in range(1, Vars.n + 1):
            sum += math.pow((f_table[i] - f_table[i-1]), 2)
        sum *= (1 /(2*Vars.dx))
        potential_energy[j] = sum


        sum = 0.0
        for i in range(1, Vars.n):
            sum += math.pow(v_table[i], 2)
        sum *= (Vars.mi / 2)
        kinetic_energy[j] = sum


        print(f"\nPotential energy: {potential_energy[j]:.2E}  Kinetic energy: {kinetic_energy[j]:.2E}  "+
              f"Total energy: {potential_energy[j] + kinetic_energy[j]}")


def main():
    string_movement_euler()
    string_movement_imprv_euler()


if __name__ == "__main__":
    main()
