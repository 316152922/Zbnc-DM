dit={'学号':'S1','姓名':'许文秀','性别':'女','年龄':20,'系部':'计算机系'}
print('读取字典值：')
for key in dit.keys():
        print(dit[key],end=' ')
dit['籍贯']='广西北海'
print('\n添加元素：籍贯:广西北海：')
print(dit)
del dit['性别']
print('删除元素：性别:女：')
print(dit)
dit['年龄']=22
print('修改年龄为22：')
print(dit)
