file='D:\\DATA_Mining\poetry.txt'
f = open(file,'a+',encoding='utf-8') #打开文件
str1='《春夜喜雨》是唐诗名篇之一，是杜甫上元二年（761年）在成都草堂居住时所作。'
f.write('\n')
f.write(str1)
f.close() 
f = open(file,'r',encoding='utf-8') 
data = f.read()
print(data) 
f.close() 
