# _*_coding : utf-8  _*_
"""
输入月收入和五险一金计算个人所得税
2019
deduction是扣除数,计算的时候，对应相应的档位然后 乘以税率 再减去扣除数

"""
salary = float(input("月收入："))
insurrance = float(input("五险一金："))
diff = salary - insurrance - 5000
if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 3000:
    rate = 0.03
    deduction = 0
elif diff < 12000:
    rate = 0.1
    deduction = 210
elif diff < 25000:
    rate = 0.2
    deduction = 1410
elif diff < 35000:
    rate = 0.25
    deduction = 2660
elif diff < 55000:
    rate = 0.3
    deduction = 4410
elif diff < 80000:
    rate = 0.35
    deduction = 7160
else:
    rate = 0.45
    deduction = 15160
tax = abs(diff*rate - deduction)
print("个人所得税是：%.2f元" % tax)
print("到手收入是：%.2f元" % (diff + 5000 - tax))