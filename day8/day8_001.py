# _*_ coding: utf-8 _*_

class student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,cource_name):
        print ('%s正在学习%s' % (self.name,cource_name))


if __name__ == '__main__':
    xiaoming = student("小明",12);
    xiaoming.study("英语")
