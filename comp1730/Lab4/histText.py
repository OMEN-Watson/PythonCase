import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(19680801)

xdata = np.array([1.2, 2.3, 3.3, 3.1, 1.7, 3.4, 2.1, 1.25, 1.3])
xbins = np.array([1, 2, 3, 4])

# changing the style of the histogram bars just to make it
# very clear where the boundaries of the bins are:
style = {'facecolor': 'none', 'edgecolor': 'C0', 'linewidth': 3}

fig, ax = plt.subplots()
ax.hist(xdata, xbins, **style)

# plot the xdata locations on the x axis:
# ax.plot(xdata, 0*xdata, 'd')
ax.plot(xdata, 0*xdata,'d')
# ax.set_ylabel('Number per bin')
# ax.set_xlabel('x bins (dx=1.0)')
plt.show()