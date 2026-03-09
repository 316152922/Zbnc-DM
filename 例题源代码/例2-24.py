import re
str1='se234 2022-10-09 07:30:00 2022-10-10 07:25:00最新疫情'
p=r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
content=re.findall(p,str1,re.M)
print(content)
