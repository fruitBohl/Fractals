from turtle import *
import math


def fractal1(length, iterations, sides):
    if iterations == 0:
        forward(length)
        return
    right(0)
    fractal1(length / 2, iterations - 1, sides)
    right(90)
    fractal1(length / 2, iterations - 1, sides)
    left(90)
    fractal1(length / 2, iterations - 1, sides)


def fractal2(length, iterations, sides):
    if iterations == 0:
        forward(length)
        return
    for y in range(length):
        forward(length - y)
        left(length - y)
        fractal2(length, iterations - 1, sides)


def draw_fractal(length, iterations, sides, fractal):
    speed(10)
    hideturtle()
    penup()
    goto(50, 200)
    showturtle()
    pendown()  # mr ryan moment
    for i in range(sides):
        color("black")
        fractal(length, iterations, sides)
        left(360 / sides)
    mainloop()


def main():
    draw_fractal(50, 3, 16, fractal1)


if __name__ == "__main__":
    main()
