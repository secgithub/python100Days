# _*_ coding: utf-8 _*_

class Student(object):

    def __init__(self, name, age):
        """
        __init__是一个特殊方法用于在创建对象时进行初始化操作
        通过这个方法我们可以为学生对象初始化name和age属性
        :param name:学生的名字
        :param age:年龄
        """
        self.name = name
        self.age = age
    def study(self,course_name):
        print("%s正在学习%s" % (self.name,course_name))
    def watch_tv(self):
        if self.age < 18:
            print("%s只能看动画片" % self.name)
        else:
            print("%s可以看很多影片" % self.name)



if __name__ == '__main__':
    s = Student('tom',22)
    s.study("英语")
    s.watch_tv()
