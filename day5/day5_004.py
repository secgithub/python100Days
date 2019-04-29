# _*_ coding: utf-8 _*_
"""斐波那切数列
F[n]=F[n-1]+F[n-2](n>=3,F[1]=1,F[2]=1)

"""
f = []
# fn
f.append(1) #f[0]就是数列中的第 1 个
f.append(1) #f[1]就是数列中的第 2 个
n = int(input('请输入N：'))
for x in range (2,n):
    f.append(f[x-1]+f[x-2])

print(f)