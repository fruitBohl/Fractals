from turtle import *


def koch_snowflake(length, iterations):
    if iterations == 0:
        forward(length)
        return
    koch_snowflake(length / 3, iterations - 1)
    left(60)
    koch_snowflake(length / 3, iterations - 1)
    right(120)
    koch_snowflake(length / 3, iterations - 1)
    left(60)
    koch_snowflake(length / 3, iterations - 1)


def draw_snowflake():
    speed(0)
    up()
    backward(200 / 2.0)
    down()
    for i in range(3):
        color("black")
        koch_snowflake(300, 4)
        left(-120)
    end_fill()
    mainloop()


def main():
    draw_snowflake()


if __name__ == "__main__":
    main()
