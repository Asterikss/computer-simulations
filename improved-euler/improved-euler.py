import logging
level = logging.INFO
fmt = "%(levelname)s:%(lineno)d:%(funcName)s: %(message)s"
logging.basicConfig(level = level, format = fmt)

class Vars:
    dt = 0.05
    approx_range = 2
    # starting points
    x0 = 1
    y0 = 1

    s0_x = 0
    s0_y = 0

    v0_x = 10
    v0_y = 10

    g_x = 0
    g_y = -10

    m = 0
    q = 0 # zakres 0-1


def calcS(dt: float, s: float, v: float):
    return s + v * dt;


def calcV(dt: float, v: float, a: float):
    return v + a * dt


def calcFg(m: float, g: float):
    return m * g


def calcFo(q: float, v: float):
    return -q * v


def calcF(m: float, g: float, q: float, v: float):
    return calcFg(m, g) + calcFo(q, v)


def calcA(m: float, g: float, q: float, v: float):
    return calcF(m, g, q, v) / m


def main():
    t = 0
    s_x = 0
    s_y = 0
    v_x = Vars.v0_x
    v_y = Vars.v0_y

    ds_x = 0
    ds_y = 0

    dv_x = 0
    dv_y = 0

    # not_end: bool = True


    print(f"  t  :  s_x :  s_y :  v_x  : v_y  : ds_x : ds_y : dv_x : dv_y")
    while True:
        t += Vars.dt
        ds_x = v_x * Vars.dt
        ds_y = v_y * Vars.dt
        dv_y = Vars.g_y * Vars.dt

        s_x += ds_x
        s_y += ds_y

        v_x += dv_x
        v_y += dv_y

        # print(f" t : s_x : s_y : v_x : v_y : ds_x : ds_y : dv_x : dv_y")
        print(f"{t:.2f} : {s_x:.2f} : {s_y:.2f} : {v_x:.2f} : {v_y:.2f} : {ds_x:.2f} : {ds_y:.2f} : {dv_x:.2f} : {dv_y:.2f}")
        if s_y <= 0:
            break


if __name__ == "__main__":
    main()
