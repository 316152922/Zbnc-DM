import re
str1='hello 123456789 word_this is just a test'
parttern='^Hello\s\d{9}.*test$'
'''
“^”标识开头，这里匹配以Hello开头的字符串；“\s”匹配空白字符串；“\d{9}”匹配9位数字；“.”匹配除了换行符之外的任意字符；“*”匹配零次或多次，二者结合起来能够匹配任意字符（除换行符）；“$”标识结尾，这里匹配以test结尾的字符串
'''
result=re.match(parttern,str1,re.I)
print(result)
print(result.group())  #group()方法输出匹配到的内容
print(result.span())   #span()方法输出匹配的范围
