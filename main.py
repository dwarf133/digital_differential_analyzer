from math import fabs as abs
from PIL import Image, ImageDraw


WIDTH = 81
HEIGHT = 81


def math_round(number):
    if number - int(number) > 0.5:
        return int(number + 1)
    else: return int(number)


def sign(number):
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


def to_normal_view(x, y):
    return x + WIDTH // 2, -1 * (y - HEIGHT // 2)


def wright_axes():
    dda(-1 * WIDTH // 2, 0, WIDTH // 2 + 1, 0, 'red')
    dda(0, -1 * HEIGHT // 2, 0, HEIGHT // 2 + 1, 'red')


x1, y1, x2, y2 = [int(i) for i in input("Input: x1, y1, x2, y2: ").split()]
img = Image.new('RGB', (HEIGHT, WIDTH), 'white')
idDraw = ImageDraw.Draw(img)


def dda(x1, y1, x2, y2, color = 'black'):
    if abs(x2-x1) >= abs(y2-y1):
        length = abs(x2-x1)
    else:
        length = abs(y2-y1)
    length = int(length)
    dx = (x2 - x1) / length
    dy = (y2 - y1) / length
    x = x1 + 0.5 * sign(dx)
    y = y1 + 0.5 * sign(dy)
    for i in range(0, length):
        idDraw.point(to_normal_view(math_round(x), math_round(y)), fill=color)
        #print(math_round(x), math_round(y))
        print(x, y)
        x += dx
        y += dy


wright_axes()
dda(x1, y1, x2, y2)

img.save("ans.png")
