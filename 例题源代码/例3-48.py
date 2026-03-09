import matplotlib.pyplot as plt
import numpy as np
x=np.arange(10)
plt.plot(x,x*1.5,'g+:',x,x*2.5,'ro-.',x,x*3.5,'x--',x,x*4.5,'bd-')
plt.show()
