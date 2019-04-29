# _*_ coding: utf-8 _*_
"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""
import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and c + a > b :
    print("周长是：%.2f" % (a + b + c) )
    p = ( a + b + c )/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("面积是：%.2f" % (area))
else:
    print("输入的三边不能构成三角形")


