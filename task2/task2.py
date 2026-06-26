"""
Напишите программу, которая рассчитывает положение точек относительно эллипса.
Координаты центра эллипса и его радиусы считываются из файла 1.
Пример:
0 0 – координаты центра
5 3 – координаты радиуса

Координаты точек считываются из файла 2.
Пример:
0 3
0 0
6 0

Вывод для данных примеров файлов:
0
1
2

Пути к файлам передаются программе в качестве аргументов!
● файл с координатами и радиусом эллипса - 1 аргумент;
● файл с координатами точек - 2 аргумент;
● координаты - рациональные числа в диапазоне от 10**-38 до 10**38;
● количество точек от 1 до 100;
● вывод каждого положения точки заканчивается символом новой строки;
● соответствия ответов:
○ 0 - точка лежит на окружности
○ 1 - точка внутри
○ 2 - точка снаружи.
Вывод программы в консоль!
"""

import sys
from math import isclose

def check_dot(ellipse_center: tuple[float, float], ellipse_radius: tuple[float, float], dot: tuple[float, float]):
    value = ((dot[0] - ellipse_center[0])**2 / (ellipse_radius[0])**2 +
               (dot[1] - ellipse_center[1])**2 / (ellipse_radius[1])**2)
    if isclose(value, 1):
        print(0)
    elif value < 1:
        print(1)
    else:
        print(2)

with open(sys.argv[1]) as c:
    lines = c.readlines()
    ellipse_center = tuple(map(float, lines[0].split()))
    ellipse_radius = tuple(map(float, lines[1].split()))

dots = []
with open(sys.argv[2]) as d:
    count = 0
    for line in d:
        count += 1
        if count > 100:
            break
        line = line.replace("\n", "")
        line = tuple(map(float, line.split()))
        dots.append(line)

for dot in dots:
    check_dot(ellipse_center, ellipse_radius, dot)