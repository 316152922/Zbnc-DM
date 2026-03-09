import pandas as pd
s1=pd.Series([12,5,7,21],index=[4,2,3,1])
s2=pd.Series([12,5,7,21],index=['a','b','c','d'])
s3=pd.Series({'a':21,'b':213,'c':309,'d':210,'e':111})
print(s1)
print(s2)
print(s3)
