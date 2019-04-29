# _*_ coding: utf-8 _*_
"""
我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""
for x in range(21):
    for y in range(33):
        for z in range(333):
            if 5*x + 3*y + z/3 == 100 and x + y + z == 100:
                print("公鸡 %d 只，母鸡 %d 只，小鸡 %d 只 满足。" %  (x,y,z))
