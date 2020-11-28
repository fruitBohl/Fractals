ITERATIONS = 80


def mandelbrot(c):
    z = 0
    n = 0

    while n < ITERATIONS and abs(z) <= 2:
        z = z * z + c
        n += 1
    return n


def main():
    for a in range(-10, 10, 5):
        for b in range(-10, 10, 5):
            c = complex(a / 10, b / 10)
            print(c, mandelbrot(c))


if __name__ == "__main__":
    main()
