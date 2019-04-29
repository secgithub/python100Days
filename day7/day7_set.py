# _*_coding: utf-8 _*_

#集合是一致的，不允许有重复的元素,可以计算交集、并集，差集等运算

def main():
    set1 = { 1,2,3,4,5,6,3,2}
    print(set1)
    print('length=',len(set1))
    set2 = set(range(1,10))
    print(set2)
    set1.add(8)
    set1.add(7) #添加一个元素
    print(set1)
    set2.update([11,12])#添加多个元素
    print(set2)
    set2.discard(5)#r如果remove的元素不存在，会报错
    print(set2)
    if 4 in set2:
        set2.remove(4)
    print(set2)
    for x in set2:
        print(x**2, end=' ')
    print()
    #将元组转换成集合
    set3 = set((1,2,3,4,56))
    print(set3.pop())#pop出第一个元素
    print(set3)
    #j集合的交集、并集、差集、对称差运算
    print(set1,set2)
    print(set1 & set2) #交集
    print(set1 | set2) #并集
    print(set1 - set2) # 差集
    print(set1 ^ set2)
    #判断子集和超级,返回True or False
    print(set2 <= set1)
    print(set3 <= set1)
    print(set1 >= set2)
    print(set1 >= set3)







if __name__ =='__main__':
    main()