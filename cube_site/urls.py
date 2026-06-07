from django.urls import path
from django.shortcuts import render
import math


def cube_frame(angle):
    width = 120
    height = 45
    scale = 42
    screen = [[' ' for x in range(width)] for y in range(height)]

    dots = [
        (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
        (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)
    ]

    lines = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    new_dots = []

    for x, y, z in dots:
        x2 = x * math.cos(angle) - z * math.sin(angle)
        z2 = x * math.sin(angle) + z * math.cos(angle)

        y3 = y * math.cos(angle * 0.8) - z2 * math.sin(angle * 0.8)
        z3 = y * math.sin(angle * 0.8) + z2 * math.cos(angle * 0.8)

        k = scale / (z3 + 4)
        px = int(x2 * k * 2 + width / 2)
        py = int(y3 * k + height / 2)

        new_dots.append((px, py))

    def draw(a, b):
        x1, y1 = new_dots[a]
        x2, y2 = new_dots[b]
        steps = max(abs(x2 - x1), abs(y2 - y1))

        if steps == 0:
            return

        for i in range(steps + 1):
            x = int(x1 + (x2 - x1) * i / steps)
            y = int(y1 + (y2 - y1) * i / steps)

            if 0 <= x < width and 0 <= y < height:
                screen[y][x] = '#'

    for line in lines:
        draw(line[0], line[1])

    return '\n'.join(''.join(row) for row in screen)


def index(request):
    frames = []

    for i in range(40):
        frames.append(cube_frame(i * 0.16))

    return render(request, 'index.html', {'frames': frames})


urlpatterns = [
    path('', index),
]
