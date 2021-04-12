import matplotlib.pyplot as plt
from math import *

if __name__ == '__main__':
    g_x = [0.75, 0.50, 0.20]
    g_y = [0.10, 0.50, 0.60]
    theta = [-0.60 / 180 * pi, 0, 0.45 / 180 * pi]

    pos = 2

    a1 = 0.7102204408817635
    a2 = 1.6923847695390781
    a3 = 1.5064128256513027

    xdist = cos(theta[pos]) * a3
    ydist = sin(theta[pos]) * a3

    Ex = g_x[pos] - xdist
    Ey = g_y[pos] - ydist

    q2 = -acos((Ex * Ex + Ey * Ey - a1 * a1 - a2 * a2) / (2 * a1 * a2))
    q1 = atan(Ey / Ex) + atan((a2 * sin(q2)) / (a1 + a2 * cos(q2)))

    a1_x = cos(q1) * a1
    a1_y = sin(q1) * a1

    a2_x = cos(q1 - q2) * a2 + a1_x
    a2_y = sin(q1 - q2) * a2 + a1_y

    x_val = [0, a1_x, a2_x, g_x[pos]]
    y_val = [0, a1_y, a2_y, g_y[pos]]

    plt.plot(x_val, y_val, marker = '.')
    plt.show()