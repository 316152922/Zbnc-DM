from urllib.request import urlopen # urllib.request.urlopen()函数用于实现对目标url的访问
import re
text = urlopen('https://www.cnblogs.com').read().decode()
#正则表达式提取网页中的网址
s='https://www.baidu.com/message.asp?id=35'
ret= re.sub(r'(https://.+?)/.*',lambda x:x.group(1),s)
print('在网页数据中提取的网址：\n',ret)
str1=re.findall(u'[\u4e00-\u9fa5]+',text)
print('在网页数据中提取汉字信息：\n',str1)
