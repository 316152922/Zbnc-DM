def is_prime(n):
    mark=True
    for i in range(2,n//2 + 1):
        if n%i==0: mark=False
    return mark
num=0
for k in range(100,201):
    if is_prime(k):num=num+1
print('100~200之间素数个数为'+str(num))
