# _*_ coding: utf-8 _*_
"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
import random

answer = int(random.randint(1,10))
#print(answer)

while True:
    key = int(input('请输入key：'))
    if key == answer:
        print("恭喜你猜对了")
        break