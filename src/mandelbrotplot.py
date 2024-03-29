from mandelbrot import *
from PIL import Image, ImageDraw

# Image size (pixels)
WIDTH = 1920
HEIGHT = 1080

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1


def drawmandelbrotset():
    im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(im)

    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
            # Compute the number of iterations
            m = mandelbrot(c)
            # The color depends on the number of iterations
            color = 255 - int(m * 255 / 80)
            # Plot the point
            draw.point([x, y], (color, color, color))

    im.save('output.png', 'PNG')


def main():
    drawmandelbrotset()


if __name__ == "__main__":
    main()
