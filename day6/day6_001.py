# _*_ coding:utf-8 _*_
def factorial(num):
    """
    求阶乘
    :param num:非负整数
    :return: num的阶乘
    """
    result = 1
    for x in range(1,num + 1):
        result *= x
    return result

n = int(input("请输入N："))
print("N的阶乘是%d" % factorial(n))