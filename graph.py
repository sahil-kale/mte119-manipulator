import matplotlib.pyplot as plt
import math

g_x = [75, 50, 20]
g_y = [10, 50, 60]
theta = [-60 * math.pi / 180, 0, 45 * math.pi / 180]

fig, axs = plt.subplots(2, 2)

for pos in range(0, 3):

    a1 = 0.9414141414141415 * 100
    a2 = 2.475757575757576 * 100
    a3 = 2.07979797979798 * 100

    xdist = math.cos(theta[pos]) * a3
    ydist = math.sin(theta[pos]) * a3

    Ex = g_x[pos] - xdist
    Ey = g_y[pos] - ydist

    q2 = -math.acos((math.pow(Ex, 2) + math.pow(Ey, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2));
    q1 = math.atan(Ey / Ex) + math.atan((a2 * math.sin(q2)) / (a1 + a2 * math.cos(q2)))

    a1_x = math.cos(q1) * a1
    a1_y = math.sin(q1) * a1

    a2_x = math.cos(q1 - q2) * a2 + a1_x
    a2_y = math.sin(q1 - q2) * a2 + a1_y

    if pos == 0:
        axs[0, 0].plot([0, a1_x], [0, a1_y], marker = '.')
        axs[0, 0].plot([a1_x, a2_x], [a1_y, a2_y], marker = '.')
        axs[0, 0].plot([a2_x, g_x[pos]], [a2_y, g_y[pos]], marker = '.')
    elif pos == 1:
        axs[0, 1].plot([0, a1_x], [0, a1_y], marker = '.')
        axs[0, 1].plot([a1_x, a2_x], [a1_y, a2_y], marker = '.')
        axs[0, 1].plot([a2_x, g_x[pos]], [a2_y, g_y[pos]], marker = '.')
    else:
        axs[1, 0].plot([0, a1_x], [0, a1_y], marker = '.')
        axs[1, 0].plot([a1_x, a2_x], [a1_y, a2_y], marker = '.')
        axs[1, 0].plot([a2_x, g_x[pos]], [a2_y, g_y[pos]], marker = '.')
plt.show()
