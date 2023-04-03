import math
import logging
level = logging.DEBUG
fmt = "%(levelname)s:%(lineno)d:%(funcName)s: %(message)s"
logging.basicConfig(level = level, format = fmt)


class Vars:
    dt = 0.001 # s
    l = 1 # m
    g = -10 # m/s^2

    m = 1 # kg
    
    angle = 45
    # v0_x = 10
    # v0_y = 10
    #
    # g_x = 0
    # g_y = -10
    #
    # # zakres 0-1
    # q = 0.2

def pendulum_movement_euler():
    logging.info("pendulum_movement_euler")

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


    print("  t   :   alfa  :   omega  :  eps   :  D_a   :  D_w   :   x   :   y   :   h   :  V   :  Ep : Ek  :  ec  : ")
    print(f"{t:.3f} : {alfa:.3f} : {omega:.3f} : {eps:.3f} : {d_a:.3f} : {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")
    i = 0
    while True:
        # if i == 0:
        #     print(f"{t:.2f} : {alfa:.2f} : {omega:.2f} : {eps:.2f} : {d_a:.2f} : {d_w:.2f} : {x:.2f} : {y:.2f} : {h:.2f} : {v:.2f}")

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

        # print(f"{t:.4f} : {alfa:.4f} : {omega:.4f} : {eps:.4f} : {d_a:.4f} : {d_w:.4f} : {x:.4f} : {y:.4f} : {h:.4f} : {v:.4f}")
        # print(f"{t:.3f} : {alfa:.3f} : {omega:.3f} : {eps:.3f} : {d_a:.3f} : {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")
        print(f"{t:.3f} : {alfa:.3f} : {omega:.3f} : {eps:.3f} : {d_a:.3f} : {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")



        i+=1
        if i > 20:
            break
 

def pendulum_movement_imprv_euler():
    logging.info("pendulum_movement_imprv_euler")

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
    i = 0
    while True:
        # if i == 0:
        #     print(f"{t:.2f} : {alfa:.2f} : {omega:.2f} : {eps:.2f} : {d_a:.2f} : {d_w:.2f} : {x:.2f} : {y:.2f} : {h:.2f} : {v:.2f}")

        t += Vars.dt
        alfa += d_a
        omega += d_w
        eps = (Vars.g / Vars.l) * math.sin(alfa)

        mid_a = alfa + omega * (Vars.dt/2) # mid_a = alfa(to + d_t/2)
        mid_w = omega + eps * (Vars.dt/2) # mid_w = omega(to + d_t/2)
        mid_e = (Vars.g/Vars.l) * math.sin(mid_a)

        # d_a = omega * Vars.dt
        d_a = mid_w * Vars.dt # omega(to + d_t/2) * dt
        # d_w = eps * Vars.dt 
        d_w = mid_e * Vars.dt # epsilon(to + d_t/2) * dt

        x = Vars.l * math.cos(alfa - math.radians(90))
        y = Vars.l * math.sin(alfa - math.radians(90))
        h = y + Vars.l
        v = Vars.l * omega

        print(f"{t:.3f} : {alfa:.3f} : {omega:.3f} : {eps:.3f} : {mid_a:.3f} : {mid_w:.3f} : {mid_e:.3f} : {d_a:.3f} : {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")



        i+=1
        if i > 20:
            break




def main():
    # pendulum_movement_euler()
    pendulum_movement_imprv_euler()


if __name__ == "__main__":
    main()
