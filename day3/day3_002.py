# _*_ coding: utf-8 _*_
"""
扔骰子 决定干什么
"""
import random

s = random.randint(1,6)
if s == 1:
    print(str(s)*10)
elif s == 2:
    print(str(s) * 10)
elif s == 3:
    print(str(s) * 10)
elif s == 4:
    print(str(s) * 10)
elif s == 5:
    print(str(s) * 10)
elif s == 6:
    print(str(s) * 10)
else:
    print("something must be wrong!!!", s)