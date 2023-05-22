import turtle
from collections import deque


def l_system_plant():
    turtle.bgcolor('black')
    t = turtle.Turtle()
    t.color('green')
    t.left(90)

    stack = deque()

    w = "X"
    for _ in range(2):
        tmp_w = ""
        for char in w:
            if char == "F":
                tmp_w += "FF"
            elif char == "X":
                tmp_w += "F+[[X]-X]-F[-FX]+X"
            else:
                tmp_w += char

        w = tmp_w

    for char in w:
        if char == "F":
            t.forward(10)
        elif char == "+":
            t.right(25)
        elif char == "-":
            t.left(25)
        elif char == "[":
            stack.append((t.pos(), t.heading()))
        elif char == "]":
            t.penup()
            pos, heading = stack.pop()
            t.setpos(pos)
            t.setheading(heading)
            t.pendown()

    turtle.done()


def main():
    l_system_plant()


if __name__ == "__main__":
    main()
