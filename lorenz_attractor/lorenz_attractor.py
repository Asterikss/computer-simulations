class Vars():
    x = 1
    y = 1
    z = 1

    a = 10
    b = 25
    c = 8/3

    dt = 0.03


def lorenz_euler():
    print("euler")
    t = 0
    x = Vars.x
    y = Vars.y
    z = Vars.z

    a = Vars.a
    b = Vars.b
    c = Vars.c

    dt = Vars.dt

    # d_x = (a * y - a * x) * dt
    # d_y = (-1 * x * z + b * x - y) * dt
    # d_z = (x * y - c * z) * dt
    print(f"  t   :   x   :   y   :   z   :   d_x   :   d_y  :  d_z")
    # print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : {d_x:.3f} : {d_y:.3f} : {d_z:.3f}")

    for _ in range(20):
        t += dt

        d_x = (a * y - a * x) * dt
        d_y = (-1 * x * z + b * x - y) * dt
        d_z = (x * y - c * z) * dt

        x += d_x
        y += d_y
        z += d_z

        # d_x = (a * y - a * x) * dt
        # d_y = (-1 * x * z + b * x - y) * dt
        # d_z = (x * y - c * z) * dt

        print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : {d_x:.3f} : {d_y:.3f} : {d_z:.3f}")


def lorenz_improved_euler():
    print("improved euler")
    t = 0
    x = Vars.x
    y = Vars.y
    z = Vars.z

    a = Vars.a
    b = Vars.b
    c = Vars.c

    dt = Vars.dt

    print(f"  t   :   x   :   y   :   z   :   d_x   :   d_y  :  d_z")
    print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : 0.000 : 0.000 : 0.000")

    # for _ in range(220):
    for _ in range(20):
        t += dt

        x_i = x + ((a * y - a * x) * dt/2)
        y_i = y + ((-1 * x * z + b * x - y) * dt/2)
        z_i = z + ((x * y - c * z) * dt/2)

        d_x = (a * y_i - a * x_i)
        d_y = (-1 * x_i * z_i + b * x_i - y_i)
        d_z = (x_i * y_i - c * z_i)

        x += d_x * dt
        y += d_y * dt
        z += d_z * dt

        print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : {d_x:.3f} : {d_y:.3f} : {d_z:.3f}")


def lorenz_rk4():
    print("RK4")
    t = 0
    x = Vars.x
    y = Vars.y
    z = Vars.z

    a = Vars.a
    b = Vars.b
    c = Vars.c

    dt = Vars.dt

    print(f"  t   :   x   :   y   :   z")
    print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f}")

    # for _ in range(1000):
    for _ in range(20):
        t += dt

        k1_x = (a * y - a * x)
        k1_y = (-1 * x * z + b * x - y)
        k1_z = (x * y - c * z)

        k2_x = (a * (y + k1_y*dt/2) - a * (x + k1_x*dt/2))
        k2_y = (-1 * (x + k1_x*dt/2) * (z + k1_z*dt/2) + b * (x + k1_x*dt/2) - (y + k1_y*dt/2))
        k2_z = ((x + k1_x*dt/2) * (y + k1_y*dt/2) - c * (z + k1_z*dt/2))

        k3_x = (a * (y + k2_y*dt/2) - a * (x + k2_x*dt/2))
        k3_y = (-1 * (x + k2_x*dt/2) * (z + k2_z*dt/2) + b * (x + k2_x*dt/2) - (y + k2_y*dt/2))
        k3_z = ((x + k2_x*dt/2) * (y + k2_y*dt/2) - c * (z + k2_z*dt/2))

        k4_x = (a * (y + k3_y*dt) - a * (x + k3_x*dt))
        k4_y = (-1 * (x + k3_x*dt) * (z + k3_z*dt) + b * (x + k3_x*dt) - (y + k3_y*dt))
        k4_z = ((x + k3_x*dt) * (y + k3_y*dt) - c * (z + k3_z*dt))

        x += dt/6 * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        y += dt/6 * (k1_y + 2*k2_y + 2*k3_y + k4_y)
        z += dt/6 * (k1_z + 2*k2_z + 2*k3_z + k4_z)

        print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f}")


def main():
    lorenz_euler()
    lorenz_improved_euler()
    lorenz_rk4()


if __name__ == "__main__":
    main()
