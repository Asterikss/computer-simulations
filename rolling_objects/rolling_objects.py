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

    eps = acc / r
    logging.debug(eps)
    d90 = math.radians(90)  
    logging.debug(d90)

def func1():
    print("func1")

    t = 0
    s_x = 0
    s_y = Vars.r
    v = 0

    ds_x = v * Vars.dt
    dv = Vars.acc * Vars.dt

    x_r = s_x  * math.cos(-(Vars.alfa)) - s_y * math.sin(-(Vars.alfa))
    logging.debug(x_r)
    y_r = s_x  * math.sin(-(Vars.alfa)) + s_y * math.cos(-(Vars.alfa)) + Vars.h
    logging.debug(y_r)

    b = 0
    w = 0 #
    db = w * Vars.dt
    dw = Vars.eps * Vars.dt

    x = Vars.r * math.cos(Vars.d90 - b) + x_r
    y = Vars.r * math.sin(Vars.d90 - b) + y_r

    sh = 0
    sh2 = Vars.r * math.cos(sh)
    sh3 = Vars.r * math.sin(sh)


    print("  t     :    s_x     :     s_y   :    v     :     ds_x     :     dv   :   x_r    :    y_r     :     b     :     w     :      db     :      dw    :    x   :   y")
    print(f"{t:.6f} : {s_x:.6f} : {s_y:.6f}  : {v:.6f} : {ds_x:.6f} : {dv:.6f} : {x_r:.6f} : {y_r:.6f}: {b:.6f}  : {w:.6f}  : {db:.6f}  : {dw:.6f} : {x:.6f} : {y:.6f}")

    for _ in range(20):
        t += Vars.dt
        s_x += ds_x
        # v += dv * Vars.dt
        v += dv

        ds_x = v * Vars.dt

        x_r = s_x  * math.cos(-(Vars.alfa)) - s_y * math.sin(-(Vars.alfa))
        y_r = s_x  * math.sin(-(Vars.alfa)) + s_y * math.cos(-(Vars.alfa)) + Vars.h

        b += db
        w += dw
        db = w * Vars.dt
        dw = Vars.eps * Vars.dt

        x = Vars.r * math.cos(Vars.d90 - b) + x_r
        y = Vars.r * math.sin(Vars.d90 - b) + y_r

        sh += math.pi / 10
        sh2 = Vars.r * math.cos(sh)
        sh3 = Vars.r * math.sin(sh)

        print(f"{t:.6f} : {s_x:.6f} : {s_y:.6f}  : {v:.6f} : {ds_x:.6f} : {dv:.6f} : {x_r:.6f} : {y_r:.6f}: {b:.6f}  : {w:.6f}  : {db:.6f}  : {dw:.6f} : {x:.6f} : {y:.6f}")



def main():
    func1()


if __name__ == "__main__":
    main()
