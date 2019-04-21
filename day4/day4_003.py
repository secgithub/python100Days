#  _*_ coding :utf-8 _*_
"""
输入一个正整数判断它是不是素数（质数）
"""
number = int(input('请输入一个数字：'))
result = True
for x in range(2,number):
    if number%x == 0:
        result = False
        break
print("输入的数字是质数吗？" , result)