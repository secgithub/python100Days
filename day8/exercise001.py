# _*_ coding: utf-8 _*_
from time import  sleep


class Clock(object):
    """
    数字时钟
    """
    def __init__(self, hour=0, minute=0, second=0):
        """
        构造方法
        :param hour:时
        :param minute: 分
        :param second: 秒
        """
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    def run(self):
        self.__second +=1
        if self.__second == 60:
            self.__second = 0
            self.__minute += 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0
    def __str__(self):
        return '%02d:%02d:%02d' % \
               (self.__hour, self.__minute, self.__second)

if __name__ == '__main__':
    clock = Clock(23,59,57)
    while True:
        print(clock)
        sleep(1)
        clock.run()