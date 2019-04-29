# _*_ coding: utf-8 _*_
"""
装饰器/修改器(getter)， @property
                def age(self):
setter 方法：在@property之后，使用@name.setter
                                    def age(self):

"""

class Person(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    #访问器，相当于getter 方法
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    #修改器 - setter方法
    @age.setter
    def age(self, age):
        self.__age = age
    def play(self):
        if self.__age <= 18:
            print('%s正在玩泥巴' % self.__name)
        else:
            print('%s正在玩斗地主' % self.__name)

if __name__ == '__main__':
    person = Person("李雷",22)
    person.play()
    person.age = 17
    person.play()
    #person.name = '小明'
    #AttributeError: can't set attribute
    print(person.name,person.age)

