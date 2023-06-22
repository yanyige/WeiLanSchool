# import
import random
import math
import move
print('result is', math.sqrt(2))

print('result is', 2 ** 0.5)

print("dir:", dir(random))
print("ramdom:", random.random())
print("randomint:", random.randint(1, 10))

# 2. 程序填空。
# 首先，为实现列表元素的循环左移，自定义函数left（），并保存到模块
# 文件move.py，如图13－7所示。
p = [1, 2, 3, 4, 5, 6]
n = 3
print("left:", move.left(p, n))
