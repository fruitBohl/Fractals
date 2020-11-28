from turtle import *


def fractal(length, iterations):
    if iterations == 0:
        forward(length)
        return
    right(0)
    fractal(length / 3, iterations - 1)
    right(90)
    fractal(length / 3, iterations - 1)
    left(90)
    fractal(length / 3, iterations - 1)


def draw_fractal(length, iterations):
    hideturtle()
    penup()
    goto(-length / 3, (2 * length) / 3)
    pendown()  # mr ryan moment
    for i in range(4):
        color("black")
        fractal(length, iterations)
        left(-90)
    mainloop()


def main():
    draw_fractal(400, 4)


if __name__ == "__main__":
    main()
