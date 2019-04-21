# _*_ coding:utf-8 _*_
"""
python 模块化，不同的python文件就是一个模块，可以通过import引入
module1.py

def foo():
    print('hello, world!')
module2.py

def foo():
    print('goodbye, world!')
test.py

from module1 import foo

# 输出hello, world!
foo()

from module2 import foo

# 输出goodbye, world!
foo()


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
"""