import random

m = random.randint(0,100)
n = random.randint(0,100)
gcd, lcm = 1, 1
print(f"整数1 = {m}, 整数2 = {n}")

if(m*n == 0):
    gcd = 0
    lcm = max(m, n)
else:
    m, n = max(m, n), min(m, n)
    lcm = m*n
    while(r := m%n):
        m = n
        n = r
    gcd = n
    lcm //= gcd

print(f"最大公约数为: {gcd}, 最小公倍数为: {lcm}")