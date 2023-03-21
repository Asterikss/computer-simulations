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

def euler():
    print("euler")
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
    i = 0
    while True:
        t += Vars.dt
        ds_x = v_x * Vars.dt
        ds_y = v_y * Vars.dt
        dv_y = Vars.g_y * Vars.dt

        if i == 0:
            print(f"{t:.2f} : {s_x:.2f} : {s_y:.2f} : {v_x:.2f} : {v_y:.2f} : {ds_x:.2f} : {ds_y:.2f} : {dv_x:.2f} : {dv_y:.2f}")

        s_x += ds_x
        s_y += ds_y

        v_x += dv_x
        v_y += dv_y

        print(f"{t:.2f} : {s_x:.2f} : {s_y:.2f} : {v_x:.2f} : {v_y:.2f} : {ds_x:.2f} : {ds_y:.2f} : {dv_x:.2f} : {dv_y:.2f}")
        i = 1
        if s_y <= 0.001:
            break


def improved_euler():
    print("improved euler")
    t = 0
    s_x = 0
    s_y = 0
    v_x = Vars.v0_x
    v_y = Vars.v0_y

    #v_x(t+dt/2)
    mid_point_x  = 0
    mid_point_y  = 0

    ds_x = 0
    ds_y = 0

    dv_x = 0
    dv_y = 0

    # not_end: bool = True


    print(f"  t  :  s_x :  s_y :  v_x  : v_y  : mid_x : mid_y: ds_x : ds_y : dv_x : dv_y")
    i = 0
    while True:

        mid_point_x = v_x + (Vars.g_x * (Vars.dt/2))
        mid_point_y = v_y + (Vars.g_y * (Vars.dt/2))

        ds_x = mid_point_x * Vars.dt
        ds_y = mid_point_y * Vars.dt
        dv_y = Vars.g_y * Vars.dt

        if i == 0:
            print(f"{t:.2f} : {s_x:.2f} : {s_y:.2f} : {v_x:.2f} : {v_y:.2f} : {mid_point_x:.2f} : {mid_point_y:.2f} : {ds_x:.2f} : {ds_y:.2f} : {dv_x:.2f} : {dv_y:.2f}")
        s_x += ds_x
        s_y += ds_y

        v_x += dv_x
        v_y += dv_y

        # print(f" t : s_x : s_y : v_x : v_y : ds_x : ds_y : dv_x : dv_y")
        t += Vars.dt
        print(f"{t:.2f} : {s_x:.2f} : {s_y:.2f} : {v_x:.2f} : {v_y:.2f} : {mid_point_x:.2f} : {mid_point_y:.2f} : {ds_x:.2f} : {ds_y:.2f} : {dv_x:.2f} : {dv_y:.2f}")
        i = 1
        if s_y <= 0.001:
            break


def main():
    # euler()
    improved_euler()


if __name__ == "__main__":
    main()
