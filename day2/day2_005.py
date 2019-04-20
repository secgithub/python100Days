# _*_ coding: utf-8 _*_
"""
输入园的半径，计算园的周长
用π，在math.pi

"""
import math
radius = float(input("请输入半径："))
l = 2 * math.pi * radius
print('半径%.1f，周长是：%.1f' % (radius, l))
