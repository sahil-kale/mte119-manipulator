import matplotlib.pyplot as plt
import math

g_x = [75, 50, 20];
g_y = [10, 50, 60];
theta = [-60 * math.pi / 180, 0, 45 * math.pi / 180];

pos = 2;

a1 = 0.7221105527638191 * 100;
a2 = 1.7477386934673367 * 100;

a3 = 1.5517587939698492 * 100;

xdist = math.cos(theta[pos]) * a3;
ydist = math.sin(theta[pos]) * a3;

Ex = g_x[pos] - xdist;
Ey = g_y[pos] - ydist;

q2 = -math.acos((math.pow(Ex, 2) + math.pow(Ey, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2));
q1 = math.atan(Ey / Ex) + math.atan((a2 * math.sin(q2)) / (a1 + a2 * math.cos(q2)));

a1_x = math.cos(q1) * a1;
a1_y = math.sin(q1) * a1;

a2_x = math.cos(q1 - q2) * a2 + a1_x;
a2_y = math.sin(q1 - q2) * a2 + a1_y;

plt.plot([0, a1_x, a2_x], [0, a1_y, a2_y])
plt.plot([Ex, g_x[pos]], [Ey, g_y[pos]])
plt.show()
