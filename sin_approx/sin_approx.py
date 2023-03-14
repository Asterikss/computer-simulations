import math

class Variables:
    radian: float = 0
    orig_angle: float = 0

def unser_input():
    print("sin(x) approximation using Taylor");

    tmp: float = float(input("Enter an angle or a radian: "))
    tmp2: int = int(input("If the input is an angle type 1. Otherwise type 2: "))
    not_finished :bool = True

    while (not_finished):
        if (tmp2 == 1):
            Variables.orig_angle = tmp
            Variables.radian = convert_to_radian(tmp);
            not_finished = False

        elif (tmp2 == 2):
            Variables.radian = tmp
            Variables.orig_angle = (Variables.radian * 180) / math.pi
            not_finished = False

        else:
            tmp2: int = int(input("If the input is an angle type 1. Otherwise type 2: "))


def sin_x_approx(radian: float, precision: int):

    result: float = radian
    next_expression: float = 0
    power: int = 1

    for i in range(precision):
        result -= next_expression
        
        power += 2

        next_expression = math.pow(radian, power)/factorial(power)

        next_expression = next_expression* (-1)**i

    from_lib = math.sin(math.radians(Variables.orig_angle))

    print(f"   {precision}   |   {result:.7f}    |    {from_lib:.7f}    |  {calc_err(result, from_lib):.7f}  |")
    return result


def calc_err(result: float, from_lib: float):
    return abs(result - from_lib)


def convert_to_radian(angle: float):
    tmp :float = angle
    if (angle > 90 and angle <= 180):
        tmp = -angle + 180
    elif (angle > 180 and angle <= 270):
        tmp = -(angle - 180)
    elif (angle > 270 and angle <= 360):
        tmp = -(360 - angle)


    return tmp * (math.pi/180)


def factorial(x: int):
    if (x <= 2): 
        return x;
    return x * factorial(x - 1);


def full_sin_x_approx(radian: float):
    print(f"\nFor sin({radian}) (8 digits)")
    print("| prec |     approx     |     from_lib    |    error    |")
    print("---------------------------------------------------------")

    for i in range(1, 10):
        sin_x_approx(radian, i)



if __name__ == "__main__":
    unser_input()
    full_sin_x_approx(Variables.radian)


