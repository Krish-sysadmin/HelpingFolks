from cProfile import label
import os
import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from numpy import ones, vstack
from numpy.linalg import lstsq
import scipy
from scipy.optimize import curve_fit


def func(x, a):
    return a * x


xpoints = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 1])
ypoints = np.array([0, 0.075, 0.132, 0.158, 0.194, 0.214, 0.464])

xpointsWithoutNumpy = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 1)
yPointsWithoutNumpy = (0, 0.075, 0.132, 0.158, 0.194, 0.214, 0.464)

popt, pcov = curve_fit(func, xpointsWithoutNumpy, yPointsWithoutNumpy)


# FOR STEEPER AND SHALLOWER CURVES
steeperCurvexpoints = np.array([0, 0.989])
steeperCurveypoints = np.array([0, 0.464])

shallowerCurvexpoints = np.array([0, 1.011])
shallowerCurveypoints = np.array([0, 0.464])


# plt.scatter(xpointsWithoutNumpy, yPointsWithoutNumpy, label="Calibration curve")
plt.plot(xpointsWithoutNumpy, func(xpointsWithoutNumpy, popt),
         "r--", label="Calibration curve y = 0.4709X")


plt.title("Absorbance dependent on coffee concentration")
plt.xlabel("concentration of caffeine ")
plt.ylabel("Absorbance (275 Au)")
plt.plot(steeperCurvexpoints, steeperCurveypoints,
         label="steeper = y=0.4691607684529828x")
plt.plot(shallowerCurvexpoints, shallowerCurveypoints,
         label="shallower = y=0.45895153313550946x")
plt.grid()
plt.legend()

plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])

plt.errorbar(xpoints, ypoints, xerr=xpoints*0.011, fmt='.k')

plt.show()
