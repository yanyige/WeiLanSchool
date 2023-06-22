def fib(n):
    if n < 1:
        raise Exception("error!")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


n = int(input('plese enter a number:'))
print('result is', fib(n))


def fib1(n):
    a, b = 1, 1
    for i in range(3, n + 1):
        a, b = b, a + b
    return b


print('result is', fib1(n))
