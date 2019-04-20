# _*_ coding: utf-8 _*_
"""
判读输入的年份是不是闰年

"""
year = int(input('请输入年份：'))
if (year % 100 == 0 and year % 400 ==0):
    print(True)
elif(year % 100 !=0 and year % 4 ==0):
    print(True)
else:
    print(False)