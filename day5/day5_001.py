# _*_ coding: utf-8 _*_
"""
，水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
"""

import math
# x,y,z 分别代表百位，十位，个位
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            if math.pow(x,3) + math.pow(y,3) + math.pow(z,3) == 100*x + 10*y + z:
                print("%d是一个水仙花数" % (100*x + 10*y + z))