import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,2*np.pi,1000)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x, y1, ls="-", lw=2, label="sin(x) figure") 
plt.plot(x, y2, ls="-", lw=2, label="cos(x) figure")
plt.legend() #给图加上图例
plt.show()
