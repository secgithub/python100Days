# _*_ coding: utf-8 _*_

def exercise(list):
    """
    函数返回传入列表中最大和第二大的元素的值
    :param list: 传入的列表
    :return:返回最大和第二大的元素的tuple
    """
    list.sort()
    return (list[-1],list[-2])

if __name__ == '__main__':
    list = [1,2222,3,77,0,10,99,3]
    t = exercise(list)
    print(t)