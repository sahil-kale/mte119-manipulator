import matplotlib.pyplot as plt
import math

g_x = [75, 50, 20]
g_y = [10, 50, 60]
theta = [-60 * math.pi / 180, 0, 45 * math.pi / 180]

fig, axs = plt.subplots(2, 2)

for pos in range(0, 3):

    a1 = 0.9303030303030303 * 100
    a2 = 2.4843434343434345 * 100
    a3 = 2.1 * 100

    xdist = math.cos(theta[pos]) * a3
    ydist = math.sin(theta[pos]) * a3

    Ex = g_x[pos] - xdist
    Ey = g_y[pos] - ydist

    q2_p = math.acos((math.pow(Ex, 2) + math.pow(Ey, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2));
    q1_p = math.atan(Ey / Ex) + math.atan((a2 * math.sin(q2_p)) / (math.sqrt(math.pow(Ex, 2) + math.pow(Ey, 2))))

    a1_x_p = math.cos(q1_p) * a1
    a1_y_p = math.sin(q1_p) * a1

    if pos == 0:
        axs[0, 0].plot([0, a1_x_p], [0, a1_y_p], marker = '.')
        axs[0, 0].plot([a1_x_p, Ex], [a1_y_p, Ey], marker = '.')
        axs[0, 0].plot([Ex, g_x[pos]], [Ey, g_y[pos]], marker = '.')
    elif pos == 1:
        axs[0, 1].plot([0, a1_x_p], [0, a1_y_p], marker = '.')
        axs[0, 1].plot([a1_x_p, Ex], [a1_y_p, Ey], marker = '.')
        axs[0, 1].plot([Ex, g_x[pos]], [Ey, g_y[pos]], marker = '.')
    else:
        axs[1, 0].plot([0, a1_x_p], [0, a1_y_p], marker = '.')
        axs[1, 0].plot([a1_x_p, Ex], [a1_y_p, Ey], marker = '.')
        axs[1, 0].plot([Ex, g_x[pos]], [Ey, g_y[pos]], marker = '.')
plt.show()
