# _*_ coding: utf-8 _*_

def main():
    str1 = 'hello python!'
    print(len(str1))
    print(str1.capitalize())
    print(str1.upper())
    print(str1.find('lo'))
    print(str1.find('lol'))
    print(str1.startswith('hl'))
    print(str1.startswith('hel'))
    print(str1.endswith('!'))
    print(str1.center(50,'*')) #两侧填充*
    print(str1.rjust(30,'*'))
    str2 = 'abc123456'
    print(str2[2])
    print(str2[2:5])
    print(str2[2:])
    print(str2[1::2]) # 两个冒号最后一位就变成了 步长
    print(str2[::-1])
    print(str2[-3:-1])
    print(str2.isdigit())
    print(str2.isalnum())
    print(str2.isalpha())
    str3 = "   1111222@@@@33    "
    print(str3.strip()) #去掉两侧空格


if __name__ == '__main__':
        main()





