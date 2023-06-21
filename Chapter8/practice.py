# 1. 阅读以下程序，写出运行结果。
# 通过成员资格运算符输出列表元素
program = ["Java", "Python", "Visual Basic"]
for w in program:
    print(w, len(w))
# Java 4 Python 6 Visual Basic 12
print(1)
print(2)
# 通过索引遍历输出列表元素
program = ["Java", "Python", "Visual Basic"]
n = len(program)
for i in range(n):
    print(i, program[i])
# 0 Java 1 Python 2 Visual Basic
