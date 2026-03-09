file='D:\\Data_Mining\poetry.txt'
f = open(file,'r+',encoding='utf-8') 
print('文件名为:', f.name)
line = f.readline()
print('读取的数据为:',line)
f.seek(0,1)  # 重新设置文件读取指针到开头
line = f.readline()
print('读取的数据为:',line)
f.close()
