import numpy as np
import matplotlib.pyplot as plt
data=np.random.normal(0,1,10000)
n,bins,patches=plt.hist(data,50)
plt.show()
