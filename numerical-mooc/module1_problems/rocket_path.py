import numpy as np
import matplotlib.pyplot as py
import sympy as sm

ms = 50 # 50kg weight of rocket shell
vg = 9.81 # m/s^2
p = 1.091 #average density of air 
r = 0.5 # 0.5m. Radius of rocket
a = np.pi * r**2 # max cross sectional area of rocket
ve = 325 # m/s. exhaust speed
cd = 0.15 # drag coefficient
mp = 100 # 100kg at time t. initial weight of the propellant.
mp_dot = 20.

# Weight of rocket a particular time.
def mp1(t0, t):
  if(t <= 5.):
    return mp_dot * t - mp_dot * t0
  elif(t > 5.):
    return 0.

m = mp - mp1(0., 3.2)
print m

#Velocity and Height
h0 = 0
v0 = 0

def f(u):
  # u is array of float containing values at time t
  h, v = u
  return np.array([v - g + (mp_dot * ve) / (ms + mp) - (0.5 * p * v * np.abs(v) * a * cd) / (ms + mp)])

def euler(u, f, dt):
  return u + (f(u) * dt)

T = 50 # final time
dt = 0.1 # given
t = np.arange(0, T + dt, dt)
N = len(t)

u = np.empty((N, 2)) #creates a matrix
u[0] = np.array([h0, v0])

#Using the method


