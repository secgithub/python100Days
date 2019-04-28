# _*_ coding: utf-8 _*_
"""
另一种实现的方法，从后往前遍历字符串，找到第一个”.”的下标，
文件后缀就是[下标:]
"""
def exercise(file_name):
    """
    设计一个函数返回给定文件名的后缀名
    :param file_name:给定的文件名
    :return: 返回后缀
    """
    list1 = file_name.split('.')
    # print(list1)
    return list1[-1]

if __name__ == '__main__':
    suffix = exercise("xxxx.0000")
    print(suffix)