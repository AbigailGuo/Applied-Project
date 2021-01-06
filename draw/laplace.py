from matplotlib import pyplot as plt
import math
import numpy as np



t = [0.05*i for i in range(0, 100)]
result = [math.sin(i) for i in t]
perturb = []
for i in range(0, len(t)):
    noise = np.random.laplace(loc=0, scale=1/2)
    perturb.append(result[i]+noise)
plt.axis([0, 5, -5, 3])
plt.legend("epsilon = 3")
plt.plot(t, result)
plt.scatter(t, perturb, )
plt.plot(t, perturb)
plt.show()
# plt.plot(t, result)
plt.cla()
plt.axis([0, 5, -5, 3])
plt.scatter(t, perturb)
plt.show()
