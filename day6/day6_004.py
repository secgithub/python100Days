# _*_ coding:utf-8 _*_


from day6.day6_001 import factorial as f

def foo():
    global a
    a = 1000
    #print(a)

def notDone():
    # ToDo: add your code here
    pass

if __name__ == '__main__':
    print("*"*10)
    n = 7
    print("N的阶乘是%d" % f(n))
    a = 10
    foo()
    print(a)
    notDone()