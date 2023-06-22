# 1. 没有return语句的函数返回值 （ ）
def void(n):
    n = 10
    print("n:", n)


print("void=", void(10))


# void= None
# 2. 以下程序实现：计算给定日期是该年的第几天。请在划线处填写合适的代码，完善程序。
# 定义函数fcount()
def fcount(year, month, day):
    sum = 0  # 判断该年是否为闰年
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month-1):
            sum = sum+lst[i]
        return sum+day
    else:
        lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(month-1):
            sum = sum+lst[i]
        return sum+day


# 输入年月日
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
# 调用函数fcount()，并输出天数
sum = fcount(2023, 6, 21)
print(year, "年", month, "月", day, "日", "是今年的第", sum, "天！")
