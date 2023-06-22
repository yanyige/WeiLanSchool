import random
count = int(input('plese enter total count:'))
print(count)

total = 0
for i in range(count):
    x, y = random.random(), random.random()
    dist = ((x * x) + (y * y)) ** 0.5
    if (dist <= 1):
        total += 1
print("total=", total, " pi=", total/count*4)
