# _*_ coding: utf-8 _*_
"""
华氏温度转换为摄氏温度
公式：F =1.8C + 32
"""
f = float(input('F = '))
c = (f-32)/1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

"""
%.1f float型小数点后1位保留
"""
