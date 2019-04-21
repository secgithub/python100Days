# _*_ coding : utf-8 _*_
"""
英寸和厘米转换
in 和 cm
1 in = 2.54cm1
"""
l = float(input("请输入长度："))
unit = str(input("请输入单位："))
if unit == 'in' or unit =='英寸':
    print("转换结果为：%.2f厘米" % ((l * 2.54)))
elif unit == 'cm' or unit == '厘米':
    print("转换结果为：%.2f英寸" %  (l/2.54))
else:
    print("输入有误！！")