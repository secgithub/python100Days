# _*_ coding: utf-8 _*_

def is_leap_year(year):
    """
    判断是否是闰年
    :param year: 年饭
    :return: True 闰年，False是平年
    """
    return year % 4==0 and year %100 !=0 or year % 400 ==0
def which_day(year,month,date):
    """
    计算传入的日期是这一年的第几天
    :param year:年
    :param month:月
    :param date:日
    :return:第几天
   """
    #后面的[is_leap_year(year)]是判断条件，来生成days_of_month
    days_of_month =[
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ][is_leap_year(year)]

    total = 0
    for index in range(month-1):
        print(days_of_month[index])
        total += days_of_month[index]
    return total+date


if __name__ == '__main__':
   the_day = which_day(1982,5,20)
   print(the_day)