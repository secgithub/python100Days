# _*_ coding : utf-8 _*_
"""
循环
range(101)可以产生一个0到100的整数序列
range(1,100) 可以产生一个1到99的整数序列
range(1,100,2)可以产生一个1 到99的奇数序列,2是步长
"""
sum = 0
for x in range(2,101,2):
    sum += x
    print(sum)
