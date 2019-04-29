# _*_ coding: utf-8 _*_
"""
可见性问题，和java中的访问控制符类似，比java的简单
只有两种：公开的和私有的，私有的不能被外部访问
私有的属性或方法命名以两个下划线开头，典型的是：__init__方法

"""
class Test:
    def __init__(self, foo):
        self.__foo = foo
    def __bar(self):
        print(self.__foo)
        print('__bar')

if __name__ == '__main__':
    test = Test('hello python')
    #test.__bar()

    #   AttributeError: 'Test' object has no attribute '__bar'
    #print(test.__foo)
    #   AttributeError: 'Test' object has no attribute '__foo'
