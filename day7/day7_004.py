# _*_ coding: utf-8
#复习list列表生成器
def reviewList():
    list1 = [x + y for x in range(2, 11, 2) for y in range(1, 10, 2)]
    print(list1)
    list2 = (x + y for x in range(10) for y in range(5))
    for val in list2:
        print(val)
def fibYield(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
        yield a

if __name__ == '__main__':
    reviewList()
    for  val in fibYield(10):
        print(val)
