from math import floor

from PIL import Image, ImageDraw

gridcolor = (76, 45, 28)
offcolor = (173, 101, 62)
oncolor = (242, 201, 159)


def create_pixels(size):
    (sx, sy) = size
    im = Image.new("RGB", (sx * 10, sy * 10), color=gridcolor)
    for x in range(0, sx):
        for y in range(0, sy):
            draw_pixel(im, (x, y), False)
    return im


def draw_pixel(im, pixel, on=True):
    (x, y) = pixel
    draw = ImageDraw.Draw(im)
    draw.rectangle((x * 10, y * 10, x * 10 + 8, y * 10 + 8), oncolor if on else offcolor)

def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0

def draw_line(im, x1, y1, x2, y2):
    # Initialization, create constants
    A = 2 * (y2 - y1)
    E = A - (x2 - x1)
    B = A - (2 * (x2 - x1))
    x, y = x1, y1

    # Pixel loop
    while x <= x2:
        draw_pixel(im, (x, y))

        x = x + 1

        E1 = E + A
        E2 = E + B

        if E1 >= 0:
            y = y + 1
            E = E2
        else:
            E = E1

    return im










def better_draw_line(im, x1, y1, x2, y2):
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    s1 = sign(x2 - x1)
    s2 = sign(y2 - y1)

    if dy > dx:
        t = dx
        dx = dy
        dy = t
        interchange = True
    else:
        interchange = False

    # Error = dy - (floor(dx / 2))
    Error = 2*dy - dx
    A = 2*dy
    B = 2*dy - 2*dx

    draw_pixel(im, (x, y))

    for i in range(0, dx): # dx times
        if Error < 0:
            if interchange:
                y += s2
            else:
                x += s1
            Error += A
        else:
            y += s2
            x += s1
            Error += B
        draw_pixel(im, (x, y))

    return im

def main():
    im = create_pixels((64, 64))

    im = better_draw_line(im, 2, 2, 55, 40)





    im = im.transpose(method=Image.Transpose.FLIP_TOP_BOTTOM)
    im.show()

if __name__ == '__main__':
    main()