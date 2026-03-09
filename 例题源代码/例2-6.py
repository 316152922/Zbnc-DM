a=int(input('输入正整数a：'))
b=int(input('输入正整数b：'))
if a<b:
        a,b=b,a
r=a%b
while r!=0:
        a,b=b,r
        r=a%b
print('最大公约数：'+str(b))
