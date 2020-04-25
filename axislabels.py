import matplotlib.pyplot as plt 
import numpy as np
x=np.arange(0,4*np.pi-1,0.1)# start,stop,step
y=np.sin(x)
z=np.cos(x)
#krisa checking
#i am bishal checking
#i am suraj checking
#plt.plot(x,y)
#plt.plot(x,z)
plt.plot(x,y,x,z)
plt.xlabel("values of x is from 0 to 4pi")  #string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of Sin(x) and Cos(x)')
plt.legend(['sin(x)','cos(x)']) # legend entries as seperate strings in a list sorry master file
plt.show()
