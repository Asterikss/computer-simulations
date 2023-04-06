import math
import logging
level = logging.DEBUG
# level = logging.INFO
fmt = "%(levelname)s:%(lineno)d:%(funcName)s: %(message)s"
logging.basicConfig(level = level, format = fmt)


class Vars:
    dt = 0.05 # s
    r = 2
    h = 20

    # l = 1 # m
    # g = -10 # m/s^2
    g = 10 # m/s^2

    m = 1 # kg
    
    angle = 45
    alfa = math.radians(angle)
    logging.debug(alfa)

    lk = 2/5 * m * r**2 # globe
    ls = 2/3 * m * r**2 # sphere
    logging.debug(lk)
    acc = g * math.sin(alfa) / (1 + lk / (m * r**2))
    logging.debug(acc)


def func1():
    print("func1")

    t = 0
    s_x = 0
    s_y = Vars.r
    v = 0

    ds_x = v * Vars.dt
    dv = Vars.acc * Vars.dt

    # print("  t   : alfa  :  omega :   eps  :  D_a   :  D_w   :   x   :   y   :   h   :   V   :   Ep  :  Ek   :   Ec")
    # print("  t   : s_x  :  s_y :   v  :  D_s   :  D_v   :   x   :   y   :   h   :   V   :   Ep  :  Ek   :   Ec")
    print("  t     :    s_x     :     s_y   :    v     :     ds_x     :     dv ")
    # print(f"{t:.3f} : {alfa:.3f} : {omega:.3f}  : {eps:.3f} : {d_a:.3f} : {d_w:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")
    # print(f"{t:.3f} : {s_x:.3f} : {s_y:.3f}  : {v:.3f} : {ds_x:.3f} : {dv:.3f} : {x:.3f} : {y:.3f} : {h:.3f} : {v:.3f} : {ep:.3f}: {ek:.3f} : {ec:.3f}")
    # print(f"{t:.3f} : {s_x:.3f} : {s_y:.3f}  : {v:.3f} : {ds_x:.3f} : {dv:.3f} ")
    print(f"{t:.7f} : {s_x:.7f} : {s_y:.7f}  : {v:.7f} : {ds_x:.7f} : {dv:.7f} ")

    for _ in range(20):
        t += Vars.dt
        s_x += ds_x
        # v += dv * Vars.dt
        v += dv

        ds_x = v * Vars.dt

        # print(f"{t:.3f} : {s_x:.3f} : {s_y:.3f}  : {v:.3f} : {ds_x:.3f} : {dv:.3f} ")
        print(f"{t:.7f} : {s_x:.7f} : {s_y:.7f}  : {v:.7f} : {ds_x:.7f} : {dv:.7f} ")



def main():
    func1()


if __name__ == "__main__":
    main()
