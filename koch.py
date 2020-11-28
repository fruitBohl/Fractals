from turtle import *


def koch_snowflake(iterations):
    if iterations == 0:
        forward(1)
        return
    koch_snowflake(iterations - 1)
    left(60)
    koch_snowflake(iterations - 1)
    right(120)
    koch_snowflake(iterations - 1)
    left(60)
    koch_snowflake(iterations - 1)


def draw_snowflake():
    speed(0)
    up()
    backward(200 / 2.0)
    down()
    fillcolor("black")
    begin_fill()
    for i in range(3):
        color("black")
        koch_snowflake(4)
        left(-120)
    end_fill()
    mainloop()
