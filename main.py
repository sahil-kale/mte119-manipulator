import math
import matplotlib.pyplot as plt
import concurrent.futures
import numpy as np

g_x = [0.75, 0.50, 0.20]
g_y = [0.10, 0.50, 0.60]
geo_consts = [4, 2, 1]
theta = [-60 / 180 * math.pi, 0, 45 / 180 * math.pi]


def calcNewFinalPoints(a3: float, pos: int):
    xdist = math.cos(theta[pos]) * a3
    ydist = math.sin(theta[pos]) * a3

    Ex = g_x[pos] - xdist
    Ey = g_y[pos] - ydist
    return Ex, Ey


# ensure that a1 and a2 can be
def checkValid(a1: float, a2: float, Ex: float, Ey: float):
    dist = math.sqrt(Ex * Ex + Ey * Ey)
    min = abs(a1 - a2)
    max = a1 + a2
    return (dist <= max and dist >= min)


# Calculate torque on base from x coords, length, and geometry const
def calcTorque(x_1: float, x_2: float, length: float, geoConst: int):
    return (x_1 + x_2 / 2) * geoConst * length * 9.81


def calcLinkAngles(Ex: float, Ey: float, a1: float, a2: float):
    # try:
    q2 = math.acos((math.pow(Ex, 2) + math.pow(Ey, 2) - math.pow(a1, 2) - math.pow(a2, 2)) / (2 * a1 * a2))
    # except:
    #    print("Error! " + str(a1) + " " + str(a2) + " " + str(Ex) + " " + str(Ey))
    #    exit()

    q1 = math.atan(Ey / Ex) + math.atan((a2 * math.sin(q2)) / (a1 + a2 * math.cos(q2)))
    return q1, q2


def calcLinkCoords(q1: float, q2: float, a1: float, a2: float):
    a1_x = math.cos(q1) * a1
    a1_y = math.sin(q1) * a1

    a2_x = math.cos(q1 - q2) * a2 + a1_x
    a2_y = math.sin(q1 - q2) * a2 + a1_y
    return a1_x, a1_y, a2_x, a2_y


# This function will ensure that the lengts are valid.
def execute(a1: float, a2: float, a3: float):
    if (a1 + a2 + a3 <= 1):
        # Numbers are invalid if they're here
        return None

    torques = 0

    for pos in range(0, 3):

        # Calculate the new Final Point for a1 and a2 to reach
        Ex, Ey = calcNewFinalPoints(a3, pos)
        # check whether a1 and 2 can reach the new final point
        if (not checkValid(a1, a2, Ex, Ey)):
            return None
        # Numbers are valid from here on out:

        # calculating link angles for a1 and a2
        q1, q2 = calcLinkAngles(Ex, Ey, a1, a2)

        # calculate the end points of a1 and a2 links
        a1_x, a1_y, a2_x, a2_y = calcLinkCoords(q1, q2, a1, a2)

        # calculate torque
        torque = calcTorque(0, a1_x, a1, geo_consts[0])
        torque += calcTorque(a1_x, a2_x, a2, geo_consts[1])
        torque += calcTorque(a2_x, Ex, a3, geo_consts[2])
        torque += g_x[pos] * 5 * 9.81

        # add to final torque
        torques += torque * torque

    torques = math.sqrt(torques)

    # return torques, F_a1x, F_a1y, F_a2x, F_a2y, g_x[2], g_y[2]
    return torques, a1, a2, a3


def visualize(a1_x: float, a1_y: float, a2_x: float, a2_y: float, a3_x: float, a3_y: float) -> None:
    x_vals = [0, a1_x, a2_x, a3_x]
    y_vals = [0, a1_y, a2_y, a3_y]
    plt.plot(x_vals, y_vals, marker = ".")


if __name__ == '__main__':

    # a1, a2, a3 0-200, in steps of 5
    minTorque = math.inf
    a1_F = 0
    a2_F = 0
    a3_F = 0

    interval_start = 0
    interval_end = 3
    divisions = 300
    iterator = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for a1 in np.linspace(interval_start, interval_end, num = divisions):
            for a2 in np.linspace(interval_start, interval_end, num = divisions):
                for a3 in np.linspace(interval_start, interval_end, num = divisions):
                    futures.append(executor.submit(execute, a1 = a1, a2 = a2, a3 = a3))
                    iterator += 1
                    if(iterator % 10000 == 0):
                        print("iteration: " + str(iterator) + " | %" + str(iterator/divisions**3*100))
                    

        for future in concurrent.futures.as_completed(futures):
            if future.result() is not None:
                data = future.result()
                

                if data[0] < minTorque:
                    minTorque = data[0]
                    print("Current Torque:" + str(minTorque))
                    print("lengths: " + str(data[1]) + " " + str(data[2]) + " " + str(data[3]))
                    

    # for a1 in np.linspace(interval_start, interval_end, num = divisions):
    #     for a2 in np.linspace(interval_start, interval_end, num = divisions):
    #         for a3 in np.linspace(interval_start, interval_end, num = divisions):
    #
    #             torque = execute(a1, a2, a3)
    #             if torque is not None and torque < minTorque:
    #                 minTorque = torque
    #                 a1_F = a1
    #                 a2_F = a2
    #                 a3_F = a3
    #                 print("Current Torque:" + str(minTorque))
    #                 print("lengths: " + str(a1) + " " + str(a2) + " " + str(a3))
