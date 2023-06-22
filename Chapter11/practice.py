# 储蓄问题。已知某同学有一些零用钱，他想通过银行储蓄增值。问：
# 存多少年，才能达到预期的数额？
# 为简单起见，假设储蓄规则为： （1） 存期以一年为单位，存款以元为单位。 （2） 一年期的存款利率均为3% （不考虑利率调整）。
# 在如下程序的划线处填空。
n = 0
p = float(input("please enter origin money:"))
q = float(input("please enter target money:"))
while (p <= q):
    p = 1.03 * p
    n += 1
print(n, "年后到达预期")
