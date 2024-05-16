import math


def angle(loc1, loc2):
    rad = math.atan2((loc2[1] - loc1[1]), (loc2[0] - loc1[0]))
    deg = rad*180/math.pi
    if deg < 0:
        return 360 + deg
    return deg
