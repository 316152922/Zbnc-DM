file='D:\\Data_Mining\poetry.txt'
f=open(file,'r',encoding='utf-8') #存储txt文件时，“编码”必须选“UTF-8”
for i in range(2):
    first_line = f.readline() #读第1行
    print(first_line) #输出第1行
data = f.read()# 读取剩下的所有内容，文件大时不要用
print(data) #输出读取内容
f.close() #关闭文件
