#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt

zeroes = [0.5,0,0,1.63] #initial x velocity; initial y velocity, initial x accel, initial y accel

e = 0.001

steps = 10000

x, y  =  [0.0]*steps, [0.0]*steps
vx, vy = [0.0]*steps, [0.0]*steps
ax, ay = [0.0]*steps, [0.0]*steps


def getOrbitPositions():

    def getRadius(x,y,i):
        return math.sqrt(math.pow(x[i],2) + math.pow(y[i],2))

    def getAccel(pos,r3,i):
        return -pos[i]/r3

    def getPos(xy,vxy,i):
        return xy[i - 1] + e*vxy[i-1]

    def getVel(vxy,axy,i):
        return vxy[i - 1] + e * axy[i]

    x[0] = zeroes[0]
    y[0] = zeroes[1]

    r3 = math.pow(getRadius(x,y,0), 3)

    ax[0] = getAccel(x,r3,0)
    ay[0] = getAccel(y,r3,0)

    vx[0] = zeroes[2] + (e/2.0)*ax[0]
    vy[0] = zeroes[3] + (e/2.0)*ay[0]

    for i in range(1, steps):

        x[i] = getPos(x,vx,i)
        y[i] = getPos(y,vy,i)

        r3 = math.pow(getRadius(x,y,i),3)

        ax[i] = getAccel(x,r3,i)
        ay[i] = getAccel(y,r3,i)

        vx[i] = getVel(vx,ax,i)
        vy[i] = getVel(vy,ay,i)

    return x, y

table = getOrbitPositions()

plt.figure(figsize=(7,7))

plt.plot(table[0], table[1]) # ASPECT RATIO 

ax = plt.gca()
ax.set_aspect(1)

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5,1.5)
plt.show()
