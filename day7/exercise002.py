# _*_ coding: utf-8 _*_
"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random
def main(code_len=4):
    """
    :param code_len:指定生成的验证码的长度
    :return:随机生成的验证码
    """
    seed = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # x  = random.choice(seed)
    chap = ''
    for v in range(0,code_len):
        chap += random.choice(seed)
    return chap
if __name__ == '__main__':
    cod = main()
    print(cod)