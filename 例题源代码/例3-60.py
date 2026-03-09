import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,11,1)
y=x**2
plt.plot(x,y)
plt.text(-3,20,'Function: y=x^2',size=15,alpha=0.2)
plt.text(-3,40,'Function:y=x^2',size=14,family='fantasy', color='b',bbox=dict(facecolor='r',alpha=0.2))
plt.show()
