sign = 1
sum = 0

n = int(input("输入要计算到第几个数："))

for i in range(n):
    sum += sign*(2*i + 1)
    sign = -sign

print(f"S={sum}")