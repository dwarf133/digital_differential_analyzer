from math import fabs as abs
from PIL import Image, ImageDraw


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


x1, y1, x2, y2 = [int(i) for i in input("Input: x1, y1, x2, y2: ").split()]
img = Image.new('RGB', (20, 20), 'white')
idDraw = ImageDraw.Draw(img)


def dda(x1, y1, x2, y2):
    if abs(x2-x1) >= abs(y2-y1):
        length = abs(x2-x1)
    else:
        length = abs(y2-y1)
    length = int(length)
    dx = (x2 - x1) // length
    dy = (y2 - y1) // length
    x = x1 + 0.5 * sign(dx)
    y = y1 + 0.5 * sign(dy)
    for i in range(0, length):
        idDraw.point((math_round(x), math_round(y)), fill='black')
        print(math_round(x), math_round(y))
        x += dx
        y += dy


dda(x1, y1, x2, y2)
img.save("ans.png")
