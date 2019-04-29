# _*_ coding: utf-8 _*_
"""
静态方法和类方法
方法前使用@staticmethod
"""
from math import sqrt
class Triangle(object):
    __slots__ = ('__a' , '__b', '__c')
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    #静态方法 staticmethod
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b
    def perimeter(self):
        return self.__a + self.__b + self.__c
    def area(self):
        half = self.perimeter()/2
        return sqrt(half * (half - self.__a) * \
                    (half - self.__b) * (half - self.__c))
def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
        # print(Triangle.perimeter(t))
        print(t.area())
        # print(Triangle.area(t))
    else:
        print('无法构成三角形.')

if __name__ == '__main__':
    main()