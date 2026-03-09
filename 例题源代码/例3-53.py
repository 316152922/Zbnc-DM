import matplotlib.pyplot as plt
import numpy as np
x = np.random.uniform(0,1,200)
y = np.random.uniform(0,1,200)
size =np.random.uniform(0,1,200)*30
color = np.random.uniform(0,1,200)
plt.scatter(x,y,size,color)
plt.colorbar()
plt.show()
