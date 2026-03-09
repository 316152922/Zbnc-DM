import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dt=pd.DataFrame(np.random.rand(4,4))
plt.boxplot(x=dt.values,labels=dt.columns,whis=1.5)
plt.show()
