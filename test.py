import matplotlib.pyplot as plot
import numpy as np  
x=np.arange(0,4*np.pi,0.01)
y=np.sin(x)
plot.plot(x,y)
plot.grid()
plot.show()