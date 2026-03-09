score=input('请输入成绩：') #手动输入成绩
score=int(score) #将输入的字符串转换为数值
if score>=90 and score<=100:print('优')
elif score>=80: print('良')
elif score>=70: print('中')
elif score>=60: print('及格')
elif score>=0 and score<60:print('不及格')
else: #输入>100或<0的分数时报错
        print('成绩输入错误！')
