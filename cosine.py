import matplotlib.pyplot as plt 
import numpy as np
x=np.arange(0,4*np.pi,0.1)# start,stop,step
y=np.cos(x)
plt.plot(x,y)
plt.show()