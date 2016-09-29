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

# Weight of rocket a particular time.
def mp1(t0, t):
  if(t <= 5.):
    return 20. * t - 20 * t0
  elif(t > 5.):
    return 0.

m = mp - mp1(0., 3.2)
print m

#Maximum Velocity
