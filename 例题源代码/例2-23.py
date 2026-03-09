import re
phone ='0517-3214-7231  # 这是一个公司的电话号码'
num = re.sub(r'#.*$', '', phone) # 删除注释
print ('电话号码 : ', num)
num = re.sub(r'\D', '', phone) # 移除非数字的内容
print ('电话号码: ', num)
