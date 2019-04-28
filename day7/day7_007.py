# _*_ coding: utf-8 _*_

"""
字典: key ,value 键值对

"""
def main():
    scores = {'小明':100,'小李':45,'TOM':66}
    print(scores)
    print(scores['小明'])
    for elem in scores:
        print('%s\t--->\t%s' % (elem,scores[elem]))
    #修改
    scores['小明'] = 98
    scores.update(小李=88,TOM = 58)
    print(scores)
    if '李清照' in scores:
        print(scores['李清照'])
    print(scores.get('小明'))
    print(scores.get('天才',66))#获取不到时，返回后面的默认值 66
    #删除元素,字典是pop出最后一个元素,集合是pop出第一个元素0
    print(scores.popitem())
    #清空字典
    scores.clear()
    print(scores)




if __name__ == '__main__':
    main()
