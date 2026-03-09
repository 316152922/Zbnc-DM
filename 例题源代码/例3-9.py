import random
#从一个字符串中随机生成若干个字符
def gen_code(n):
    s='er0dfsdfxcvbn7f989fd'
    code=''
    for i in range(n):
        r = random.randint(0,len(s)-1)
        code+=s[r]
    return code
username=input("输入用户名：")
passwd=input("输入密码:")
code=gen_code(5)
print("验证码是：",code)
code1=input("输入验证码：")
if code.lower() == code1.lower():
    if username=='knn' and passwd=='abc':
        print("Login success!")
    else:
        print("username or password error！")
else:
    print("check code error!")
