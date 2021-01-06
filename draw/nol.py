import numpy as np
from matplotlib import pyplot as plt
import math


t1 = np.arange(0.0, 5.0, 0.1)
points = [5*math.sin(1.5*t) for t in t1]
points1 = [10*math.sin(1.5*t) for t in t1]
mean_v = np.mean(points)
std_v = np.std(points)
mean_v1 = np.mean(points1)
std_v1 = np.std(points1)
nol_v = [(p-mean_v)/std_v for p in points]
nol_v1 = [(p-mean_v1)/std_v1 for p in points1]
plt.figure()
plt.axis([0,5,-11,11])
plt.plot(t1, points, 'bo')
plt.plot(t1, points)
plt.plot(t1, points1, 'bo', c="green")
plt.plot(t1, points1, c="green")
plt.scatter(t1, nol_v, c="orange")
plt.scatter(t1, nol_v1, c="red")
plt.plot(t1, nol_v)
plt.show()
