import matplotlib.pyplot as plt
fracs = [15, 30.6, 44.4, 10]
A=[0,0.1,0,0]
labe=['A','B','C','D']
plt.pie(x=fracs,autopct='%3.1f%%',explode=A,labels=labe, shadow=True)
plt.show()
