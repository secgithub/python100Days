# _*_ coding: utf-8 _*_
"""
__slots__魔法
限定自定义类型的对象,只能绑定某些属性
限定之后，对象就不能创建其他的属性了
"""

class Person(object):
    # 限定Person的对象只能绑定下面几个属性
    __slots__ = ('__name', '__age__', '__gender__')

    def __init__(self, name, age):
        self.__name = name
        self.__age__ = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age__

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age__ = age

    def play(self):
        if self.__age__ <= 18:
            print('%s正在玩泥巴' % self.__name)
        else:
            print('%s正在玩电脑' % self.__name)


if __name__ == '__main__':
    person = Person('小明', 19)
    person.play()
    person.name = '王重阳'
    person.age = 10
    person.play()
    person.__gender__ = '1111'
    person.__wtf = '2222'# AttributeError: 'Person' object has no attribute '__wtf'

