import os, sys, matplotlib
import numpy as np
import matplotlib.pyplot as plt
from numpy import ones,vstack
from numpy.linalg import lstsq
import scipy

points = [(6, 2.907),(29 ,0.257)]
x_coords_steeper, y_coords_steeper = zip(*points)
A = vstack([x_coords_steeper,ones(len(x_coords_steeper))]).T
m, c = lstsq(A, y_coords_steeper)[0]
print("Line Solution is y = {m}x + {c}".format(m=m,c=c))

xpoints = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 1])
ypoints = np.array([0, 0.075, 0.132, 0.158, 0.194, 0.214, 0.464])

steeperCurvexpoints = np.array([0, 0])
steeperCurveypoints = np.array([0.989,0.464])

shallowerCurvexpoints = np.array([0, 0])
shallowerCurveypoints = np.array([1.011,0.464])

plt.plot(xpoints, ypoints, label = "Line of Best Fit (with R² = 1)")
plt.title("Absorbance dependent on coffee concentration")
plt.xlabel("concentration of caffeine ")
plt.ylabel("Absorbance (275 Au)")
plt.plot(steeperCurvexpoints, steeperCurveypoints, label = "steeper = " + "Ln(V) = -0.098T + 3.300" )
plt.plot(shallowerCurvexpoints, shallowerCurveypoints, label = "shallower = " + " Ln(V) = -0.115T + 3.598")
plt.grid()
plt.legend()

plt.errorbar(xpoints, ypoints, xerr=xpoints*0.011 , fmt='.k')

plt.show()


 
