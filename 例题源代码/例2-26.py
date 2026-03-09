import re
def Find(string):
        url_pattern=r'[]a-zA-Z.)+://[^\s]*'
        url=re.findall(url_pattern,string)
        return url
str_url='我们常用网站很多，下面列出两个，如Runoob 的网页地址为：https://wwww.runoob.com,Goog的网址为：https://www.google.com'
str1=Find(str_url)
for ch in str1:
        if ch!='': print(ch,end=' ')

