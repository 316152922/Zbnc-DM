lst1=['This','is','a','apple']
print(' '.join(lst1))
#如果列表中包含数字类型元素时，需要先转换为字符串
lst2=['S6','许文秀','女',21,'计算机系']
print(' '.join([str(x) for x in lst2]))
