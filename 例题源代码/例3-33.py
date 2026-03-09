import pandas as pd
df=pd.DataFrame([[1,2.12,3.245],[3.356,4.56,2.1101]],columns=list('abc'),index=[2,3])
def f(x):
    return len(str(x))  #对每一个元素求长度，其中1按1.0计算
print(df.applymap(f))
