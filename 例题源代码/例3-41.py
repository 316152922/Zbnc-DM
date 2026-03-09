import csv
import os
os.chdir('D:\\Data_mining') #改变当前路径
head=['学号','姓名','性别','年龄','系部']  #写定义文件头
lst=[['S1','许文秀','女',20,'计算机系'],
      ['S2','刘德峰','男',21,'电信系'],
      ['S3','刘世元','男',22,'管理系'],
      ['S4','于金凤','女',21,'计算机系']]
with open ('test.csv', 'a', newline='') as f :  #追加方式打开或创建
    f_csv=csv.writer(f)  
    f_csv.writerow(head)  #写入文件头
    for i in range(4):  #按行写入文件  
       f_csv.writerow(lst[i])
