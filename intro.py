import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 10000) # start, finish, n points

y = x**2 + 2*x + 2

# equaly spread x axis points accros -10 and 10
fig, ax = plt.subplots()
ax.plot(x,y)
#plt.show()


ax.set_xlim([-2, 0])
ax.set_ylim([0, 2])
ax.plot(x,y, label='y = x^2 + 2x + 2')


ax.set_xlim([-1.5, -0.5])
ax.set_ylim([0.5, 1.5])
ax.plot(x,y, label='y = x^2 + 2x + 2')

ax.set_xlim([-1.1, -0.9])
ax.set_ylim([0.9, 1.1])
ax.plot(x,y, label='y = x^2 + 2x + 2')

ax.set_xlim([-1.01, -0.99])
ax.set_ylim([0.99, 1.01])
ax.plot(x,y, label='y = x^2 + 2x + 2')

plt.show()