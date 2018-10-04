import numpy as np
import matplotlib.pyplot as plt

t1 = np.arange(0,10,0.2)
t2 = np.arange(0,10,0.5)
plt.plot(t1,t1**2, 'r-',t2,t2**2,'bs',t2,t2**2+1,'g-')
plt.axis(xmin=0,xmax=10,ymin=0,ymax=100)
plt.ylabel('numbers')
plt.show()
