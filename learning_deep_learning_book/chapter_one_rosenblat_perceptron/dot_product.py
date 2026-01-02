import matplotlib.pyplot as plt
import numpy as np


def compute_output_vector(w, x):
	z = np.dot(w,x)
	return np.sign(z)

plt.plot([-1.0, 1.0, -1.0], [1.0, -1.0, -1.0], "r+", markersize=12)
plt.plot([-2, 2, -2, 2])
plt.show()
