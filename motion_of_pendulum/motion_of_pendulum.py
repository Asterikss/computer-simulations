import math
import logging
# level = logging.DEBUG
level = logging.INFO
fmt = "%(levelname)s:%(lineno)d:%(funcName)s: %(message)s"
logging.basicConfig(level = level, format = fmt)


class Vars:
    dt = 0.001 # s
    l = 1 # m
    g = -10 # m/s^2

    m = 1 # kg
    
    angle = 45


def pendulum_movement_euler():
    print("pendulum_movement_euler")

    t = 0
    alfa = math.radians(Vars.angle)
    logging.debug(alfa)
    omega = 0
    eps = (Vars.g / Vars.l) * math.sin(alfa)

    d_a = omega * Vars.dt
    d_w = eps * Vars.dt
    
    x = Vars.l * math.cos(alfa - math.radians(90))
    y = Vars.l * math.sin(alfa - math.radians(90))
    h = y + Vars.l
    v = Vars.l * omega

    ep = abs(Vars.m * Vars.g * h)
    logging.debug(ep)
    ek = (Vars.m * v**2)/2 
    ec = ep + ek


    print("  t   : alfa  :  omega :   eps  :  D_a   :  D_w   :   x   :   y   :   h   :   V   :   Ep  :  Ek   :   Ec")
    print(f"{t:.3f} : {alfa:.3f} : {omega:.3f}  : {eps:.3f} : {d_a:.3f} : {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")

    for _ in range(120):
    # for _ in range(20):
        t += Vars.dt
        alfa += d_a
        omega += d_w
        eps = (Vars.g / Vars.l) * math.sin(alfa)

        d_a = omega * Vars.dt
        d_w = eps * Vars.dt

        x = Vars.l * math.cos(alfa - math.radians(90))
        y = Vars.l * math.sin(alfa - math.radians(90))
        h = y + Vars.l
        v = Vars.l * omega

        ep = abs(Vars.m * Vars.g * h)
        logging.debug(ep)
        ek = (Vars.m * v**2)/2 
        ec = ep + ek

        print(f"{t:.3f} : {alfa:.3f} : {omega:.3f} : {eps:.3f} : {d_a:.3f} : {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")
 

def pendulum_movement_imprv_euler():
    print("pendulum_movement_imprv_euler (rounded to three decimal places): ")

    t = 0
    alfa = math.radians(Vars.angle)
    logging.debug(alfa)
    omega = 0
    eps = (Vars.g / Vars.l) * math.sin(alfa)

    mid_a = 0
    mid_w = 0
    mid_e = 0

    d_a = omega * Vars.dt
    d_w = eps * Vars.dt
    
    x = Vars.l * math.cos(alfa - math.radians(90))
    y = Vars.l * math.sin(alfa - math.radians(90))
    h = y + Vars.l
    v = Vars.l * omega

    ep = abs(Vars.m * Vars.g * h)
    logging.debug(ep)
    ek = (Vars.m * v**2)/2 
    ec = ep + ek



    print("  t   :  alfa :  omega  :  eps  :  mid_a : mid_w : mid_e  :  D_a  :  D_w    :   x   :   y   :   h   :   V   :  Ep   : Ek    :  Ec   : ")
    print(f"{t:.3f} : {alfa:.3f} : {omega:.3f} : {eps:.3f} :  {mid_a:.3f} :  {mid_w:.3f} :  {mid_e:.3f} :  {d_a:.3f} :  {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")

    for _ in range(120):
    # for _ in range(20):
        t += Vars.dt
        alfa += d_a
        omega += d_w
        eps = (Vars.g / Vars.l) * math.sin(alfa)

        mid_a = alfa + omega * (Vars.dt/2) # mid_a = alfa(to + d_t/2)
        mid_w = omega + eps * (Vars.dt/2) # mid_w = omega(to + d_t/2)
        mid_e = (Vars.g/Vars.l) * math.sin(mid_a)

        d_a = mid_w * Vars.dt # omega(to + d_t/2) * dt
        d_w = mid_e * Vars.dt # epsilon(to + d_t/2) * dt

        x = Vars.l * math.cos(alfa - math.radians(90))
        y = Vars.l * math.sin(alfa - math.radians(90))
        h = y + Vars.l
        v = Vars.l * omega

        ep = abs(Vars.m * Vars.g * h)
        logging.debug(ep)
        ek = (Vars.m * v**2)/2 
        ec = ep + ek

        print(f"{t:.3f} : {alfa:.3f} : {omega:.3f} : {eps:.3f} : {mid_a:.3f} : {mid_w:.3f} : {mid_e:.3f} : {d_a:.3f} : {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")


def calc_derivative(alfa, omega) -> tuple[float, float]: #pure
    return (omega, (Vars.g/Vars.l) * math.sin(alfa)) # (kn_alfa (omega), kn_omega (Epsilon))


def solve_euler(kn_alfa, kn_omega, half_delta_t) -> tuple[float, float]: #pure
    return (kn_alfa * half_delta_t, kn_omega * half_delta_t) # (kn_alfa * dt/2, kn_omega * dt/2)


def pendulum_movement_RK4():
    print("pendulum_movement_RK4: ")

    t = 0
    alfa = math.radians(Vars.angle)
    logging.debug(alfa)
    omega = 0
    eps = (Vars.g / Vars.l) * math.sin(alfa)

    x = Vars.l * math.cos(alfa - math.radians(90))
    y = Vars.l * math.sin(alfa - math.radians(90))
    h = y + Vars.l
    v = Vars.l * omega

    ep = abs(Vars.m * Vars.g * h)
    logging.debug(ep)
    ek = (Vars.m * v**2)/2 
    ec = ep + ek

    d_alfa = 0
    d_omega = 0
    print("  t   :  alfa :  omega :  eps   :  D_a   :  D_w   :   x   :   y    :   h   :  V     :  Ep  :  Ek   :   ec")
    print(f"{t:.6f} : {alfa:.6f} : {omega:.6f}  : {eps:.6f} :  {d_alfa:.6f} :  {d_omega:.6f} : {x:.6f} : {y:.6f} : {h:.6f} :  {v:.6f} : {ep:.6f}: {ek:.6f} : {ec:.6f}")

    for _ in range(440):
    # for _ in range(20):
        t += Vars.dt
        ki_alfa = 0
        ki_omega = 0
        ki_table: list[tuple[float, float]] = []
        
        alfa_tmp = alfa
        omega_tmp = omega
        for _ in range(4):
            ki_alfa, ki_omega = calc_derivative(alfa_tmp, omega_tmp)
            ki_table.append(tuple([round(ki_alfa, 3), round(ki_omega, 3)]))
            
            d_alfa, d_omega = solve_euler(ki_alfa, ki_omega, Vars.dt/2)

            alfa_tmp += d_alfa
            omega_tmp += d_omega

        logging.debug(ki_table)

        alfa += ((ki_table[0][0] + (2 * ki_table[1][0]) + (2 * ki_table[2][0]) + ki_table[3][0]) / 6) * Vars.dt
        logging.debug(round(alfa, 3))
        omega += ((ki_table[0][1] + (2 * ki_table[1][1]) + (2 * ki_table[2][1]) + ki_table[3][1]) / 6) * Vars.dt
        logging.debug(round(omega, 3))

        eps = (Vars.g / Vars.l) * math.sin(alfa) #
        x = Vars.l * math.cos(alfa - math.radians(90))
        y = Vars.l * math.sin(alfa - math.radians(90))
        h = y + Vars.l
        v = Vars.l * omega

        ep = abs(Vars.m * Vars.g * h)
        logging.debug(ep)
        ek = (Vars.m * v**2)/2 
        ec = ep + ek

        print(f"{t:.6f} : {alfa:.6f} : {omega:.6f}  : {eps:.6f} :  {d_alfa:.6f} :  {d_omega:.6f} : {x:.6f} : {y:.6f} : {h:.6f} :  {v:.6f} : {ep:.6f}: {ek:.6f} : {ec:.6f}")


def main():
    pendulum_movement_euler()
    pendulum_movement_imprv_euler()
    pendulum_movement_RK4()


if __name__ == "__main__":
    main()
