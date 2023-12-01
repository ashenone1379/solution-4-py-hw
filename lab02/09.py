while((n := int(input("输入非负整数n:"))) < 0):
    pass
result1 = 1;result2 = 1

for i in range (1, n+1):
    result1 *= i

i = 1
while i <= n:
    result2 *= i
    i += 1

print(f"for循环: {n}! = {result1}")
print(f"while循环: {n}! = {result2}")