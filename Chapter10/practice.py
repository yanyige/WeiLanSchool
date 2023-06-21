# 1. 阅读如下程序，当循环结束后，x的值是 （ ）。
x = 0
while x < 50:
    x = (x+2)*(x+3)
print(x)
# 72
# 2. 阅读如下程序，观察输出结果。
x = 0
while x < 10:
    x = x + 1
    if x % 2 == 0:
        continue
    print(x)
# 1 3 5 7 9