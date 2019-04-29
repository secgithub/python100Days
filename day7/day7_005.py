# _*_ coding: utf-8 _*_
##tuple元组
#元组与列表类似，不同之处在于，元组的元素不能修改
def main():
     t = ('测试',100,True,'hello python')
     print(t)
     print(t[0])
     print(t[1:3])
     for v in t:
         print(v)
     #元组不能修改，修改赋值会报错
     #t[0] = 1000
     #TypeError: 'tuple' object does not support item assignment
     #将元组转换为列表
     person = list(t)
     print(person)
     person[0] = "小明"
     print(person)
     #将列表转换为元组
     fruits_list = ['apple','pear','orange']
     fruits_tuple = tuple(fruits_list)
     print(fruits_tuple)

""""
tuple的用途，因为不能修改，多线程的环境下，可以保证线程安全。
更加易于维护
占用的空间比list小，创建的时间比list快
"""



if __name__ == '__main__':
    main()