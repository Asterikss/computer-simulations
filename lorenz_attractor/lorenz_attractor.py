import logging


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

    d_x = (a * y - a * x) * dt
    d_y = (-1 * x * z + b * x - y) * dt
    d_z = (x * y - c * z) * dt
    print(f"  t   :   x   :   y   :   z   :   d_x   :   d_y  :  d_z")
    print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : {d_x:.3f} : {d_y:.3f} : {d_z:.3f}")

    for _ in range(20):
        t += dt

        x += d_x
        y += d_y
        z += d_z

        d_x = (a * y - a * x) * dt
        d_y = (-1 * x * z + b * x - y) * dt
        d_z = (x * y - c * z) * dt

        print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : {d_x:.3f} : {d_y:.3f} : {d_z:.3f}")



def lorenz_imprv_euler():
    print("improved euler")
    t = 0
    x = Vars.x
    y = Vars.y
    z = Vars.z

    a = Vars.a
    b = Vars.b
    c = Vars.c

    dt = Vars.dt

    

    d_x = (a * y - a * x) * dt
    d_y = (-1 * x * z + b * x - y) * dt
    d_z = (x * y - c * z) * dt
    print(f"  t   :   x   :   y   :   z   :   d_x   :   d_y  :  d_z")
    print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : {d_x:.3f} : {d_y:.3f} : {d_z:.3f}")

    for _ in range(40):
        t += dt

        x += d_x
        y += d_y
        z += d_z
        
        # mid_x = x + ((a * y - a * x) * dt/2)
        # mid_y = y + ((-1 * x * z + b * x - y) * dt/2)
        # mid_z = z + ((x * y - c * z) * dt/2)
        mid_x = x + ((a * y - a * x) * dt/2)
        mid_y = y + ((-1 * x * z + b * x - y) * dt/2)
        mid_z = z + ((x * y - c * z) * dt/2)

        # d_x = (a * y - a * x) * dt
        # d_y = (-1 * x * z + b * x - y) * dt
        # d_z = (x * y - c * z) * dt
        d_x = mid_x * dt
        d_y = mid_y * dt
        d_z = mid_z * dt

        print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : {d_x:.3f} : {d_y:.3f} : {d_z:.3f}")


def lorenz_improved_euler2():
    print("improved euler2")
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

    for _ in range(120):
        t += dt

        # Calculate intermediate values using Euler method
        x_i = x + (a * y - a * x) * dt
        y_i = y + (-1 * x * z + b * x - y) * dt
        z_i = z + (x * y - c * z) * dt

        # Calculate new values using intermediate values and Euler method
        d_x = (a * y_i - a * x_i) * dt
        d_y = (-1 * x_i * z_i + b * x_i - y_i) * dt
        d_z = (x_i * y_i - c * z_i) * dt

        x += 0.5 * (d_x + (a * y - a * x) * dt)
        y += 0.5 * (d_y + (-1 * x * z + b * x - y) * dt)
        z += 0.5 * (d_z + (x * y - c * z) * dt)

        print(f"{t:.3f} : {x:.3f} : {y:.3f} : {z:.3f} : {d_x:.3f} : {d_y:.3f} : {d_z:.3f}")


def main():
    # lorenz_euler()
    # lorenz_imprv_euler()
    lorenz_improved_euler2()


if __name__ == "__main__":
    main()
